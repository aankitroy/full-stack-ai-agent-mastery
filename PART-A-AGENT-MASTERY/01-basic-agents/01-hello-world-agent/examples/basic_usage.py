"""
Basic usage examples for the Hello World Agent
Demonstrates simple interactions and core functionality
"""

import sys
sys.path.append('..')
from agent import HelloWorldAgent

def basic_conversation_example():
    """Example of a basic conversation with the agent"""
    print("🤖 Basic Conversation Example")
    print("=" * 50)
    
    # Create agent
    agent = HelloWorldAgent(personality="friendly_assistant")
    
    # Simple conversation
    messages = [
        "Hello!",
        "How are you doing today?",
        "Can you tell me what you can do?",
        "Thanks for the help!"
    ]
    
    for message in messages:
        print(f"User: {message}")
        response = agent.respond(message)
        print(f"Agent: {response}")
        print("-" * 30)

def personality_comparison():
    """Compare different agent personalities"""
    print("\n🎭 Personality Comparison")
    print("=" * 50)
    
    personalities = ["friendly_assistant", "technical_expert", "creative_companion"]
    test_message = "Tell me about artificial intelligence"
    
    for personality in personalities:
        print(f"\n{personality.replace('_', ' ').title()}:")
        agent = HelloWorldAgent(personality=personality)
        response = agent.respond(test_message)
        print(f"Response: {response[:100]}...")

def conversation_analysis():
    """Analyze conversation patterns and statistics"""
    print("\n📊 Conversation Analysis")
    print("=" * 50)
    
    agent = HelloWorldAgent()
    
    # Have a longer conversation
    conversation = [
        "Hi there!",
        "I'm working on a Python project",
        "Can you help me understand functions?",
        "What about classes and objects?",
        "Thanks, that's very helpful!"
    ]
    
    for msg in conversation:
        agent.respond(msg)
    
    # Show analysis
    summary = agent.get_conversation_summary()
    print("Conversation Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    basic_conversation_example()
    personality_comparison()
    conversation_analysis()
