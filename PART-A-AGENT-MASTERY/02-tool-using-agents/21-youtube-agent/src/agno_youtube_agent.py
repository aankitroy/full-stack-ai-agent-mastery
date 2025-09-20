"""
Agno-Based YouTube Content Analyzer Agent
=========================================

Simple implementation using Agno's built-in YouTube capabilities.
This demonstrates how frameworks simplify agent development.

Usage:
    from agno_youtube_agent import AgnoYouTubeAgent
    agent = AgnoYouTubeAgent()
    agent.analyze_video("https://www.youtube.com/watch?v=VIDEO_ID")
"""

try:
    from agno import Agent
    AGNO_AVAILABLE = True
except ImportError:
    AGNO_AVAILABLE = False


class AgnoYouTubeAgent:
    """
    YouTube Content Analyzer using Agno Framework
    
    Demonstrates how frameworks simplify agent development:
    - Built-in YouTube tools
    - Automatic transcript extraction
    - Simple API for complex operations
    """
    
    def __init__(self):
        """Initialize Agno-based YouTube agent"""
        if not AGNO_AVAILABLE:
            raise ImportError("Agno framework not available. Install with: pip install agno")
        
        # Create Agno agent with YouTube capabilities
        self.agent = Agent(
            name="YouTube Content Analyzer",
            instructions="""
            You are a YouTube Content Analyzer Agent specialized in processing video content.
            
            When given a YouTube URL:
            1. Extract the video transcript automatically
            2. Analyze the content for main themes and key concepts
            3. Generate a comprehensive summary with:
               - Brief overview
               - Key concepts and themes
               - Actionable insights
               - Important timestamps (if available)
            4. Format the output in a clear, structured manner
            
            Always provide valuable insights that help users understand the video content quickly.
            """,
            # Agno automatically includes YouTube tools
            show_tool_calls=True,
            markdown=True
        )
    
    def analyze_video(self, youtube_url: str, format_type: str = "comprehensive") -> str:
        """
        Analyze YouTube video content using Agno's simple interface
        
        Args:
            youtube_url: YouTube video URL
            format_type: Type of analysis (brief, comprehensive, actionable)
        
        Returns:
            Formatted analysis of the video content
        """
        if format_type == "brief":
            prompt = f"Provide a brief summary of this video: {youtube_url}"
        elif format_type == "actionable":
            prompt = f"Extract actionable insights and key takeaways from this video: {youtube_url}"
        else:  # comprehensive
            prompt = f"Provide a comprehensive analysis of this video including themes, concepts, and insights: {youtube_url}"
        
        # Agno handles everything automatically!
        return self.agent.print_response(prompt, markdown=True)
    
    def batch_analyze(self, urls: list, format_type: str = "brief") -> list:
        """Analyze multiple YouTube videos"""
        results = []
        for url in urls:
            print(f"\n📹 Analyzing: {url}")
            result = self.analyze_video(url, format_type)
            results.append({"url": url, "analysis": result})
        return results


# Example usage
if __name__ == "__main__":
    import sys
    
    if not AGNO_AVAILABLE:
        print("❌ Agno framework not installed.")
        print("📦 Install with: pip install agno")
        print("📚 Learn more: https://github.com/agno-agi/agno")
        sys.exit(1)
    
    # Initialize agent
    agent = AgnoYouTubeAgent()
    
    # Test with a YouTube URL
    test_url = "https://www.youtube.com/watch?v=Iv9dewmcFbs"
    
    print("🎬 Agno YouTube Content Analyzer")
    print("=" * 50)
    print(f"Processing: {test_url}")
    print()
    
    # Analyze the video
    result = agent.analyze_video(test_url, format_type="comprehensive")
    print(result)
