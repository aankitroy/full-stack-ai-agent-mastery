"""
Unit tests for Hello World Agent
Testing basic functionality and edge cases
"""

import unittest
from datetime import datetime
import sys
sys.path.append('.')

from agent import HelloWorldAgent, AgentMessage

class TestHelloWorldAgent(unittest.TestCase):
    
    def setUp(self):
        """Set up test agent before each test"""
        self.agent = HelloWorldAgent(personality="friendly_assistant")
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.model, "gpt-3.5-turbo")
        self.assertEqual(self.agent.personality, "friendly_assistant")
        self.assertEqual(len(self.agent.conversation_history), 0)
    
    def test_input_analysis(self):
        """Test input analysis functionality"""
        # Test greeting detection
        greeting_analysis = self.agent._analyze_input("Hello there!")
        self.assertEqual(greeting_analysis["intent"], "greeting")
        
        # Test question detection
        question_analysis = self.agent._analyze_input("How are you?")
        self.assertEqual(question_analysis["intent"], "question")
        
        # Test farewell detection
        farewell_analysis = self.agent._analyze_input("Goodbye!")
        self.assertEqual(farewell_analysis["intent"], "farewell")
    
    def test_conversation_logging(self):
        """Test conversation history is properly logged"""
        initial_count = len(self.agent.conversation_history)
        
        # Simulate a response (without actual LLM call for testing)
        reasoning = self.agent.think("Test message")
        self.agent._log_interaction("Test message", "Test response", reasoning)
        
        # Should have added 2 messages (user + agent)
        self.assertEqual(len(self.agent.conversation_history), initial_count + 2)
    
    def test_conversation_summary(self):
        """Test conversation summary functionality"""
        # Add some test messages
        test_reasoning = {"input_analysis": {"topics": ["test"]}, "thinking_time": 0.1}
        
        self.agent._log_interaction("Hello", "Hi there!", test_reasoning)
        self.agent._log_interaction("How are you?", "I'm doing well!", test_reasoning)
        
        summary = self.agent.get_conversation_summary()
        
        self.assertEqual(summary["user_messages"], 2)
        self.assertEqual(summary["agent_messages"], 2)
        self.assertEqual(summary["total_messages"], 4)
    
    def test_personality_prompts(self):
        """Test different personality configurations"""
        personalities = ["friendly_assistant", "technical_expert", "creative_companion"]
        
        for personality in personalities:
            agent = HelloWorldAgent(personality=personality)
            prompt = agent._get_personality_prompt(personality)
            self.assertIsInstance(prompt, str)
            self.assertTrue(len(prompt) > 50)  # Should be substantial content
    
    def test_context_summarization(self):
        """Test context summarization with conversation history"""
        # Empty history
        context = self.agent._summarize_context()
        self.assertEqual(context, "No previous context")
        
        # Add some history
        msg1 = AgentMessage("Hello", datetime.now(), "user", {"topics": ["greeting"]})
        msg2 = AgentMessage("How are you?", datetime.now(), "user", {"topics": ["question"]})
        
        self.agent.conversation_history.extend([msg1, msg2])
        context = self.agent._summarize_context()
        self.assertIn("greeting", context)
    
    def test_conversation_reset(self):
        """Test conversation reset functionality"""
        # Add some conversation history
        test_reasoning = {"input_analysis": {"topics": ["test"]}, "thinking_time": 0.1}
        self.agent._log_interaction("Test", "Response", test_reasoning)
        
        # Verify history exists
        self.assertGreater(len(self.agent.conversation_history), 0)
        
        # Reset and verify
        self.agent.reset_conversation()
        self.assertEqual(len(self.agent.conversation_history), 0)
        self.assertEqual(self.agent.agent_stats["messages_processed"], 0)
    
    def test_error_handling(self):
        """Test agent handles errors gracefully"""
        # This test would need to mock the OpenAI API to force an error
        # For now, we test the error logging structure
        error_reasoning = {"input_analysis": {"topics": []}, "thinking_time": 0}
        
        self.agent._log_interaction(
            "Test input", 
            "Error response", 
            error_reasoning, 
            error=True
        )
        
        # Check that error was logged
        last_message = self.agent.conversation_history[-1]
        self.assertTrue(last_message.metadata.get("error", False))

if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
