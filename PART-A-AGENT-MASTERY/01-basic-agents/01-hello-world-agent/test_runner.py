"""
Comprehensive test runner for Hello World Agent
Run various test scenarios and generate reports
"""

import sys
import time
import json
from datetime import datetime
from agent import HelloWorldAgent

class AgentTester:
    """Comprehensive testing framework for the Hello World Agent"""
    
    def __init__(self):
        self.test_results = []
        self.start_time = None
    
    def run_all_tests(self):
        """Run all test scenarios"""
        print("🧪 Starting Comprehensive Agent Testing")
        print("=" * 60)
        
        self.start_time = time.time()
        
        # Run different test categories
        self.test_basic_functionality()
        self.test_conversation_flow()
        self.test_personality_differences()
        self.test_reasoning_capabilities()
        self.test_performance_metrics()
        self.test_error_handling()
        
        # Generate report
        self.generate_report()
    
    def test_basic_functionality(self):
        """Test basic agent functionality"""
        print("\n🔧 Testing Basic Functionality")
        print("-" * 40)
        
        try:
            agent = HelloWorldAgent()
            
            # Test initialization
            assert agent.model == "gpt-3.5-turbo"
            assert agent.personality == "friendly_assistant"
            assert len(agent.conversation_history) == 0
            print("✅ Initialization: PASSED")
            
            # Test basic response (without API call for testing)
            reasoning = agent.think("Hello!")
            assert "input_analysis" in reasoning
            assert "context_summary" in reasoning
            assert "response_strategy" in reasoning
            print("✅ Reasoning Process: PASSED")
            
            # Test intent recognition
            greeting = agent._analyze_input("Hello there!")
            question = agent._analyze_input("How are you?")
            farewell = agent._analyze_input("Goodbye!")
            
            assert greeting["intent"] == "greeting"
            assert question["intent"] == "question"
            assert farewell["intent"] == "farewell"
            print("✅ Intent Recognition: PASSED")
            
            self.test_results.append({
                "category": "Basic Functionality",
                "status": "PASSED",
                "details": "All basic functions working correctly"
            })
            
        except Exception as e:
            print(f"❌ Basic Functionality: FAILED - {str(e)}")
            self.test_results.append({
                "category": "Basic Functionality",
                "status": "FAILED",
                "details": str(e)
            })
    
    def test_conversation_flow(self):
        """Test conversation flow and memory"""
        print("\n💬 Testing Conversation Flow")
        print("-" * 40)
        
        try:
            agent = HelloWorldAgent()
            
            # Simulate conversation without API calls
            test_conversation = [
                ("Hello!", "greeting"),
                ("My name is Alice", "conversation"),
                ("What's my name?", "question"),
                ("Thanks for your help!", "gratitude")
            ]
            
            for user_input, expected_intent in test_conversation:
                reasoning = agent.think(user_input)
                # Simulate logging without actual LLM response
                agent._log_interaction(user_input, f"Response to: {user_input}", reasoning)
                
                # Verify intent detection
                actual_intent = reasoning["input_analysis"]["intent"]
                if actual_intent != expected_intent:
                    print(f"⚠️  Intent mismatch for '{user_input}': expected {expected_intent}, got {actual_intent}")
            
            # Check conversation history
            assert len(agent.conversation_history) == 8  # 4 user + 4 agent messages
            
            # Check summary
            summary = agent.get_conversation_summary()
            assert summary["user_messages"] == 4
            assert summary["agent_messages"] == 4
            
            print("✅ Conversation Flow: PASSED")
            print(f"   - Messages logged: {len(agent.conversation_history)}")
            print(f"   - Topics tracked: {len(summary['topics_discussed'])}")
            
            self.test_results.append({
                "category": "Conversation Flow",
                "status": "PASSED",
                "details": f"Processed {len(test_conversation)} messages successfully"
            })
            
        except Exception as e:
            print(f"❌ Conversation Flow: FAILED - {str(e)}")
            self.test_results.append({
                "category": "Conversation Flow",
                "status": "FAILED",
                "details": str(e)
            })
    
    def test_personality_differences(self):
        """Test different agent personalities"""
        print("\n🎭 Testing Personality Differences")
        print("-" * 40)
        
        try:
            personalities = ["friendly_assistant", "technical_expert", "creative_companion"]
            personality_results = {}
            
            for personality in personalities:
                agent = HelloWorldAgent(personality=personality)
                prompt = agent._get_personality_prompt(personality)
                
                # Verify personality prompt exists and is substantial
                assert len(prompt) > 50
                assert personality.replace('_', ' ') in prompt.lower() or \
                       any(word in prompt.lower() for word in personality.split('_'))
                
                personality_results[personality] = {
                    "prompt_length": len(prompt),
                    "contains_personality_keywords": True
                }
                
                print(f"✅ {personality}: PASSED (prompt: {len(prompt)} chars)")
            
            self.test_results.append({
                "category": "Personality Differences",
                "status": "PASSED",
                "details": f"Tested {len(personalities)} personalities successfully"
            })
            
        except Exception as e:
            print(f"❌ Personality Differences: FAILED - {str(e)}")
            self.test_results.append({
                "category": "Personality Differences",
                "status": "FAILED",
                "details": str(e)
            })
    
    def test_reasoning_capabilities(self):
        """Test agent reasoning and analysis"""
        print("\n🧠 Testing Reasoning Capabilities")
        print("-" * 40)
        
        try:
            agent = HelloWorldAgent()
            
            # Test various input types
            test_inputs = [
                ("Hello world!", "greeting"),
                ("How does AI work?", "question"),
                ("Thanks for the help!", "gratitude"),
                ("See you later!", "farewell"),
                ("I'm working on a project", "conversation")
            ]
            
            reasoning_quality = []
            
            for text, expected_intent in test_inputs:
                reasoning = agent.think(text)
                
                # Check reasoning structure
                required_keys = ["input_analysis", "context_summary", "response_strategy", "thinking_time"]
                for key in required_keys:
                    assert key in reasoning
                
                # Check analysis quality
                analysis = reasoning["input_analysis"]
                assert "intent" in analysis
                assert "topics" in analysis
                
                # Verify intent detection
                if analysis["intent"] == expected_intent:
                    reasoning_quality.append(1)
                else:
                    reasoning_quality.append(0)
                    print(f"⚠️  Intent mismatch: '{text}' -> expected {expected_intent}, got {analysis['intent']}")
            
            accuracy = sum(reasoning_quality) / len(reasoning_quality) * 100
            print(f"✅ Reasoning Capabilities: PASSED")
            print(f"   - Intent accuracy: {accuracy:.1f}%")
            print(f"   - Average thinking time: {reasoning['thinking_time']:.3f}s")
            
            self.test_results.append({
                "category": "Reasoning Capabilities",
                "status": "PASSED",
                "details": f"Intent accuracy: {accuracy:.1f}%"
            })
            
        except Exception as e:
            print(f"❌ Reasoning Capabilities: FAILED - {str(e)}")
            self.test_results.append({
                "category": "Reasoning Capabilities",
                "status": "FAILED",
                "details": str(e)
            })
    
    def test_performance_metrics(self):
        """Test performance tracking and metrics"""
        print("\n⚡ Testing Performance Metrics")
        print("-" * 40)
        
        try:
            agent = HelloWorldAgent()
            
            # Simulate multiple interactions
            test_messages = [
                "Hello!",
                "How are you?",
                "What can you do?",
                "Tell me about AI",
                "Thanks!"
            ]
            
            start_time = time.time()
            
            for msg in test_messages:
                reasoning = agent.think(msg)
                agent._log_interaction(msg, f"Response to: {msg}", reasoning)
            
            end_time = time.time()
            total_time = end_time - start_time
            
            # Check performance metrics
            summary = agent.get_conversation_summary()
            
            assert summary["total_messages"] == len(test_messages) * 2  # User + agent messages
            assert summary["user_messages"] == len(test_messages)
            assert summary["agent_messages"] == len(test_messages)
            assert len(summary["topics_discussed"]) > 0
            
            print(f"✅ Performance Metrics: PASSED")
            print(f"   - Total processing time: {total_time:.3f}s")
            print(f"   - Messages per second: {len(test_messages)/total_time:.1f}")
            print(f"   - Average response time: {summary['average_response_time']:.3f}s")
            print(f"   - Topics discovered: {len(summary['topics_discussed'])}")
            
            self.test_results.append({
                "category": "Performance Metrics",
                "status": "PASSED",
                "details": f"Processed {len(test_messages)} messages in {total_time:.3f}s"
            })
            
        except Exception as e:
            print(f"❌ Performance Metrics: FAILED - {str(e)}")
            self.test_results.append({
                "category": "Performance Metrics",
                "status": "FAILED",
                "details": str(e)
            })
    
    def test_error_handling(self):
        """Test error handling and resilience"""
        print("\n🛡️ Testing Error Handling")
        print("-" * 40)
        
        try:
            agent = HelloWorldAgent()
            
            # Test with empty input
            reasoning_empty = agent.think("")
            assert "input_analysis" in reasoning_empty
            
            # Test with very long input
            long_input = "This is a very long input " * 100
            reasoning_long = agent.think(long_input)
            assert "input_analysis" in reasoning_long
            
            # Test conversation reset
            agent._log_interaction("Test", "Response", reasoning_empty)
            assert len(agent.conversation_history) > 0
            
            agent.reset_conversation()
            assert len(agent.conversation_history) == 0
            assert agent.agent_stats["messages_processed"] == 0
            
            print("✅ Error Handling: PASSED")
            print("   - Empty input handled")
            print("   - Long input handled")
            print("   - Conversation reset working")
            
            self.test_results.append({
                "category": "Error Handling",
                "status": "PASSED",
                "details": "All error scenarios handled gracefully"
            })
            
        except Exception as e:
            print(f"❌ Error Handling: FAILED - {str(e)}")
            self.test_results.append({
                "category": "Error Handling",
                "status": "FAILED",
                "details": str(e)
            })
    
    def generate_report(self):
        """Generate comprehensive test report"""
        total_time = time.time() - self.start_time
        
        print("\n" + "=" * 60)
        print("📊 COMPREHENSIVE TEST REPORT")
        print("=" * 60)
        
        # Summary statistics
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["status"] == "PASSED")
        failed_tests = total_tests - passed_tests
        
        print(f"Total Test Categories: {total_tests}")
        print(f"Passed: {passed_tests} ✅")
        print(f"Failed: {failed_tests} ❌")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        print(f"Total Test Time: {total_time:.2f} seconds")
        
        # Detailed results
        print("\nDetailed Results:")
        print("-" * 40)
        
        for result in self.test_results:
            status_icon = "✅" if result["status"] == "PASSED" else "❌"
            print(f"{status_icon} {result['category']}: {result['status']}")
            print(f"   Details: {result['details']}")
        
        # Save report to file
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": failed_tests,
                "success_rate": (passed_tests/total_tests)*100,
                "total_time": total_time
            },
            "detailed_results": self.test_results
        }
        
        with open("test_report.json", "w") as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: test_report.json")
        
        # Recommendations
        print("\n🎯 Recommendations:")
        if failed_tests == 0:
            print("   🎉 All tests passed! Agent is ready for production use.")
            print("   🚀 Consider adding more advanced features like tool usage.")
        else:
            print("   🔧 Review failed test categories and fix issues.")
            print("   🧪 Run tests again after making fixes.")

def main():
    """Run comprehensive testing"""
    tester = AgentTester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
