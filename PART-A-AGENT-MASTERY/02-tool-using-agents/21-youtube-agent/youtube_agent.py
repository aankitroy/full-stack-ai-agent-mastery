#!/usr/bin/env python3
"""
YouTube Content Analyzer Agent - Agno Framework
===============================================

Simple parameterized YouTube agent using Agno's built-in capabilities.

Usage:
    python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
    python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --action "analyze"
    python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --action "extract key points"
"""

import argparse
from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv

load_dotenv()


def create_youtube_agent():
    """Create and configure the YouTube agent"""
    return Agent(
        tools=[YouTubeTools()],
        description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    )


def main():
    """Command line interface for YouTube agent"""
    parser = argparse.ArgumentParser(description="YouTube Content Analyzer using Agno")
    parser.add_argument("--url", required=True, help="YouTube video URL")
    parser.add_argument("--action", default="summarize", 
                       help="Action to perform: summarize, analyze, extract key points, etc.")
    parser.add_argument("--demo", action="store_true", 
                       help="Run in demo mode (no API key required)")
    
    args = parser.parse_args()
    
    print("🎬 YouTube Content Analyzer Agent (Agno Framework)")
    print("=" * 60)
    print(f"📹 URL: {args.url}")
    print(f"🎯 Action: {args.action}")
    
    if args.demo:
        print("🎭 Mode: Demo (simulated response)")
        print()
        demo_response(args.url, args.action)
    else:
        print("🚀 Mode: Production (requires OPENAI_API_KEY)")
        print()
        
        try:
            # Create agent
            agent = create_youtube_agent()
            
            # Create prompt based on action
            prompt = f"{args.action} this video {args.url}"
            
            # Process with Agno's simple interface
            print("⏳ Processing with Agno framework...")
            agent.print_response(prompt, markdown=True)
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print("\n💡 Try demo mode: python youtube_agent.py --url 'URL' --demo")


def demo_response(url: str, action: str):
    """Demo mode response without API calls"""
    import re
    
    # Extract video ID
    match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([^&\s]+)', url)
    video_id = match.group(1) if match else "unknown"
    
    print(f"⏳ Processing {action} for video {video_id}...")
    print()
    
    responses = {
        "summarize": f"""
## 📺 Video Summary

**Video ID**: {video_id}

This video provides educational content about AI agent development, covering key concepts like:

• **Agent Architecture**: Perception, Reasoning, and Action layers
• **Tool Integration**: How agents use external capabilities  
• **Framework Selection**: Choosing the right tools for your project
• **Practical Implementation**: Real-world coding examples

**Key Takeaway**: Understanding agent fundamentals is essential for building effective AI systems.
        """,
        
        "analyze": f"""
## 🔍 Content Analysis

**Video ID**: {video_id}

### Content Classification:
- **Type**: Educational/Technical
- **Complexity**: Intermediate level
- **Target Audience**: Developers, AI enthusiasts

### Main Themes:
1. AI Agent Architecture and Design
2. Tool Integration Patterns
3. Framework Comparison and Selection
4. Practical Implementation Strategies

### Learning Value: High - Provides solid foundation for agent development
        """,
        
        "extract key points": f"""
## 💡 Key Points

**Video ID**: {video_id}

### 🎯 Essential Concepts:
• Agents = Perception + Reasoning + Action + Memory + Environment
• Tools extend agent capabilities beyond basic LLM responses
• Framework choice impacts development speed and complexity
• Real-world applications require robust error handling

### ⚡ Actionable Items:
• Study agent architecture patterns
• Practice with different frameworks
• Build your own tool-using agents
• Join the AI agent development community
        """
    }
    
    # Find the best matching response
    response_key = action.lower()
    for key in responses.keys():
        if key in response_key:
            response_key = key
            break
    
    response = responses.get(response_key, responses["summarize"])
    print(response)


if __name__ == "__main__":
    main()