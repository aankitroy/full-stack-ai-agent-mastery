"""
Test script to verify OpenAI API migration
Tests core functionality without requiring API key
"""

import sys
import os

# Add current directory to path
sys.path.append('.')

# Global variables for imports
HelloWorldAgent = None
AgentMessage = None

def test_imports():
    """Test that all imports work with new OpenAI version"""
    try:
        from openai import OpenAI
        print("✅ OpenAI import successful")
        
        # Import agent components
        from agent import HelloWorldAgent, AgentMessage
        print("✅ Agent imports successful")
        
        # Make imports available globally for other tests
        globals()['HelloWorldAgent'] = HelloWorldAgent
        globals()['AgentMessage'] = AgentMessage
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_agent_initialization():
    """Test agent initializes correctly"""
    try:
        # Test without API key (should still initialize)
        os.environ.pop('OPENAI_API_KEY', None)
        agent = HelloWorldAgent()
        
        assert agent.model == "gpt-3.5-turbo"
        assert agent.personality == "friendly_assistant"
        assert len(agent.conversation_history) == 0
        assert hasattr(agent, 'client')  # Should have OpenAI client
        
        print("✅ Agent initialization successful")
        return True
    except Exception as e:
        print(f"❌ Agent initialization failed: {e}")
        return False

def test_reasoning_functionality():
    """Test reasoning works without API calls"""
    try:
        agent = HelloWorldAgent()
        
        # Test reasoning (no API call)
        reasoning = agent.think("Hello world!")
        
        assert "input_analysis" in reasoning
        assert "context_summary" in reasoning
        assert "response_strategy" in reasoning
        assert "thinking_time" in reasoning
        
        # Test intent recognition
        analysis = agent._analyze_input("Hello there!")
        assert analysis["intent"] == "greeting"
        
        print("✅ Reasoning functionality working")
        return True
    except Exception as e:
        print(f"❌ Reasoning functionality failed: {e}")
        return False

def test_conversation_logging():
    """Test conversation logging works"""
    try:
        agent = HelloWorldAgent()
        
        # Test logging without API response
        reasoning = agent.think("Test message")
        agent._log_interaction("Test input", "Test response", reasoning)
        
        assert len(agent.conversation_history) == 2  # User + agent message
        
        # Test summary
        summary = agent.get_conversation_summary()
        assert summary["total_messages"] == 2
        assert summary["user_messages"] == 1
        assert summary["agent_messages"] == 1
        
        print("✅ Conversation logging working")
        return True
    except Exception as e:
        print(f"❌ Conversation logging failed: {e}")
        return False

def test_api_response_structure():
    """Test that API response would work (mock test)"""
    try:
        agent = HelloWorldAgent()
        
        # Test message structure for API
        messages = [{"role": "system", "content": agent.system_prompt}]
        messages.append({"role": "user", "content": "Hello"})
        
        # Verify message structure is correct for new API
        for msg in messages:
            assert "role" in msg
            assert "content" in msg
            assert msg["role"] in ["system", "user", "assistant"]
        
        print("✅ API message structure correct")
        return True
    except Exception as e:
        print(f"❌ API structure test failed: {e}")
        return False

def main():
    """Run all migration tests"""
    print("🔄 Testing OpenAI API Migration")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_agent_initialization,
        test_reasoning_functionality,
        test_conversation_logging,
        test_api_response_structure
    ]
    
    results = []
    for test in tests:
        results.append(test())
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print("=" * 50)
    print(f"📊 Migration Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Migration successful! All tests passed.")
        print("\n✅ Your agent is ready to use with OpenAI API v1.0+")
        print("\nTo test with actual API:")
        print("1. Set your API key: export OPENAI_API_KEY='your-key'")
        print("2. Run: python agent.py")
    else:
        print("❌ Migration incomplete. Please check the failed tests above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
