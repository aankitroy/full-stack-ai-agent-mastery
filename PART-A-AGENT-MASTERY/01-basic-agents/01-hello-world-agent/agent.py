"""
Hello World Agent - The simplest possible agent implementation
Learning focus: Basic agent loop and reasoning patterns
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from openai import OpenAI
from dataclasses import dataclass

@dataclass
class AgentMessage:
    """Structured message format for agent communication"""
    content: str
    timestamp: datetime
    message_type: str  # 'user', 'agent', 'system'
    metadata: Optional[Dict] = None

class HelloWorldAgent:
    """
    A basic conversational agent demonstrating core agent concepts:
    1. State management (conversation history)
    2. Reasoning loop (input -> think -> respond)
    3. Context awareness
    4. Personality/role definition
    """
    
    def __init__(self, model="gpt-3.5-turbo", personality="friendly_assistant"):
        self.model = model
        self.personality = personality
        self.conversation_history: List[AgentMessage] = []
        self.agent_stats = {
            "messages_processed": 0,
            "average_response_time": 0,
            "topics_discussed": set()
        }
        
        # Initialize OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.client = OpenAI(api_key=api_key)
        else:
            # For testing without API key, set client to None
            self.client = None
        
        # Agent personality and role definition
        self.system_prompt = self._get_personality_prompt(personality)
    
    def _get_personality_prompt(self, personality: str) -> str:
        """Define the agent's personality and behavior"""
        personalities = {
            "friendly_assistant": """
            You are a helpful, friendly AI assistant. You:
            - Greet users warmly and remember context from the conversation
            - Ask follow-up questions to be more helpful
            - Admit when you don't know something
            - Keep responses concise but informative
            - Show genuine interest in helping the user
            """,
            "technical_expert": """
            You are a technical expert AI assistant. You:
            - Provide detailed, accurate technical information
            - Ask clarifying questions about technical requirements
            - Suggest best practices and alternatives
            - Explain complex concepts clearly
            """,
            "creative_companion": """
            You are a creative AI companion. You:
            - Think outside the box and suggest creative solutions
            - Ask thought-provoking questions
            - Encourage exploration and experimentation
            - Share interesting connections and ideas
            """
        }
        return personalities.get(personality, personalities["friendly_assistant"])
    
    def think(self, user_input: str) -> Dict:
        """
        Agent reasoning step - analyze input and plan response
        This is where the 'intelligence' happens
        """
        start_time = datetime.now()
        
        # Simple reasoning: categorize the input
        reasoning = {
            "input_analysis": self._analyze_input(user_input),
            "context_summary": self._summarize_context(),
            "response_strategy": self._plan_response(user_input),
            "thinking_time": 0  # Will be calculated at the end
        }
        
        reasoning["thinking_time"] = (datetime.now() - start_time).total_seconds()
        return reasoning
    
    def _analyze_input(self, text: str) -> Dict:
        """Analyze user input to understand intent and content"""
        text_lower = text.lower()
        
        analysis = {
            "intent": "unknown",
            "entities": [],
            "sentiment": "neutral",
            "topics": []
        }
        
        # Simple rule-based analysis (in production, you'd use NLP models)
        if any(greeting in text_lower for greeting in ["hello", "hi", "hey", "good morning", "good afternoon"]):
            analysis["intent"] = "greeting"
        elif "?" in text:
            analysis["intent"] = "question"
        elif any(word in text_lower for word in ["bye", "goodbye", "see you", "farewell"]):
            analysis["intent"] = "farewell"
        elif any(word in text_lower for word in ["thank", "thanks", "appreciate"]):
            analysis["intent"] = "gratitude"
        else:
            analysis["intent"] = "conversation"
        
        # Extract simple topics (keywords)
        topics = [word for word in text_lower.split() if len(word) > 3]
        analysis["topics"] = topics[:3]  # Keep top 3 topics
        
        return analysis
    
    def _summarize_context(self) -> str:
        """Summarize recent conversation context"""
        if not self.conversation_history:
            return "No previous context"
        
        recent_messages = self.conversation_history[-3:]  # Last 3 messages
        topics = set()
        
        for msg in recent_messages:
            if msg.metadata and "topics" in msg.metadata:
                topics.update(msg.metadata["topics"])
        
        return f"Recent topics: {', '.join(topics) if topics else 'General conversation'}"
    
    def _plan_response(self, user_input: str) -> str:
        """Plan the response strategy based on input analysis"""
        analysis = self._analyze_input(user_input)
        
        strategies = {
            "greeting": "Respond warmly and ask how I can help",
            "question": "Provide helpful information and ask follow-up if needed",
            "farewell": "Say goodbye politely and offer future assistance",
            "gratitude": "Acknowledge thanks and offer continued help",
            "conversation": "Engage naturally and keep conversation flowing"
        }
        
        return strategies.get(analysis["intent"], "Respond helpfully and naturally")
    
    def respond(self, user_input: str) -> str:
        """
        Generate agent response using LLM
        This is where the actual response generation happens
        """
        # Think about the input first
        reasoning = self.think(user_input)
        
        # Build conversation context for LLM
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        for msg in self.conversation_history[-5:]:  # Last 5 messages for context
            role = "user" if msg.message_type == "user" else "assistant"
            messages.append({"role": role, "content": msg.content})
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Check if client is available
            if self.client is None:
                error_response = "OpenAI API key not provided. Please set OPENAI_API_KEY environment variable."
                self._log_interaction(user_input, error_response, reasoning, error=True)
                return error_response
            
            # Generate response using LLM
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            
            agent_response = response.choices[0].message.content.strip()
            
            # Log the interaction
            self._log_interaction(user_input, agent_response, reasoning)
            
            return agent_response
            
        except Exception as e:
            error_response = f"I apologize, but I encountered an error: {str(e)}. Please try again."
            self._log_interaction(user_input, error_response, reasoning, error=True)
            return error_response
    
    def _log_interaction(self, user_input: str, agent_response: str, reasoning: Dict, error: bool = False):
        """Log the interaction for learning and improvement"""
        # Add user message
        user_msg = AgentMessage(
            content=user_input,
            timestamp=datetime.now(),
            message_type="user",
            metadata={
                "analysis": reasoning["input_analysis"],
                "topics": reasoning["input_analysis"]["topics"]
            }
        )
        self.conversation_history.append(user_msg)
        
        # Add agent response
        agent_msg = AgentMessage(
            content=agent_response,
            timestamp=datetime.now(),
            message_type="agent",
            metadata={
                "reasoning": reasoning,
                "error": error,
                "response_time": reasoning["thinking_time"]
            }
        )
        self.conversation_history.append(agent_msg)
        
        # Update stats
        self.agent_stats["messages_processed"] += 1
        self.agent_stats["topics_discussed"].update(reasoning["input_analysis"]["topics"])
        
        # Calculate running average response time
        total_time = sum(
            msg.metadata.get("response_time", 0) 
            for msg in self.conversation_history 
            if msg.message_type == "agent" and msg.metadata
        )
        agent_messages = sum(1 for msg in self.conversation_history if msg.message_type == "agent")
        if agent_messages > 0:
            self.agent_stats["average_response_time"] = total_time / agent_messages
    
    def get_conversation_summary(self) -> Dict:
        """Get summary of the conversation for analysis"""
        return {
            "total_messages": len(self.conversation_history),
            "user_messages": sum(1 for msg in self.conversation_history if msg.message_type == "user"),
            "agent_messages": sum(1 for msg in self.conversation_history if msg.message_type == "agent"),
            "topics_discussed": list(self.agent_stats["topics_discussed"]),
            "average_response_time": round(self.agent_stats["average_response_time"], 2),
            "conversation_duration": (
                self.conversation_history[-1].timestamp - self.conversation_history[0].timestamp
            ).total_seconds() if self.conversation_history else 0
        }
    
    def reset_conversation(self):
        """Clear conversation history and stats"""
        self.conversation_history = []
        self.agent_stats = {
            "messages_processed": 0,
            "average_response_time": 0,
            "topics_discussed": set()
        }

# Convenience function for quick testing
def chat_with_agent(personality="friendly_assistant"):
    """Interactive chat session with the agent"""
    agent = HelloWorldAgent(personality=personality)
    
    print(f"🤖 Hello! I'm your {personality.replace('_', ' ')} agent.")
    print("Type 'quit' to end the conversation, 'stats' to see conversation statistics.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("🤖 Goodbye! It was nice talking with you!")
            break
        
        if user_input.lower() == 'stats':
            stats = agent.get_conversation_summary()
            print(f"\n📊 Conversation Statistics:")
            for key, value in stats.items():
                print(f"   {key}: {value}")
            print()
            continue
        
        if user_input:
            response = agent.respond(user_input)
            print(f"🤖 {response}\n")

if __name__ == "__main__":
    chat_with_agent()
