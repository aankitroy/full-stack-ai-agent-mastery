# 🎬 YouTube Content Analyzer Agent

> **Tool-Using Agent**: Extract transcripts from YouTube URLs and provide intelligent summaries using Agno framework

## 🎯 **What This Agent Does**

This agent demonstrates the **Tool Use Design Pattern** by integrating with YouTube to:

- Extract video transcripts automatically
- Analyze content for main themes and concepts
- Generate summaries in different formats
- Provide actionable insights from video content

**Agent Type**: Tool-Using Agent (⭐⭐⭐⭐ complexity)  
**Framework**: [Agno](https://github.com/agno-agi/agno) with built-in YouTube tools

## 🚀 **How to Run**

### **Installation**

```bash
# Navigate to the agent directory
cd PART-A-AGENT-MASTERY/02-tool-using-agents/21-youtube-agent/

# Install dependencies
pip install -r requirements.txt
```

### **Demo Mode (No API Key Required)**

```bash
# Basic summarization
python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --demo

# Content analysis
python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --action "analyze" --demo

# Extract key points
python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --action "extract key points" --demo
```

### **Production Mode (Requires OpenAI API Key)**

```bash
# Set your API key
export OPENAI_API_KEY=your_openai_api_key

# Run with real AI processing
python youtube_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --action "summarize"
```

## 📋 **Available Actions**

| Action                     | Description                  | Example Output                      |
| -------------------------- | ---------------------------- | ----------------------------------- |
| `summarize`                | Create concise video summary | Main points and key takeaways       |
| `analyze`                  | Detailed content analysis    | Themes, complexity, target audience |
| `extract key points`       | Bullet-point key concepts    | Essential concepts and action items |
| `find actionable insights` | Focus on practical takeaways | What viewers should do next         |

## 💻 **Usage Examples**

### **Educational Content**

```bash
python youtube_agent.py --url "https://www.youtube.com/watch?v=EDUCATION_VIDEO" --action "extract key points" --demo
```

### **Business/Tech Talks**

```bash
python youtube_agent.py --url "https://www.youtube.com/watch?v=TECH_TALK" --action "find actionable insights" --demo
```

### **General Summarization**

```bash
python youtube_agent.py --url "https://www.youtube.com/watch?v=ANY_VIDEO" --demo
```

## 🛠️ **Technical Details**

### **Framework Integration**

Built with [Agno framework](https://github.com/agno-agi/agno) using:

- `Agent` class for core functionality
- `YouTubeTools()` for built-in YouTube integration
- Simple `agent.print_response()` interface

### **Agent Architecture**

Follows **Lesson 1 fundamentals**:

- **Perception Layer**: URL parsing and transcript extraction
- **Reasoning Layer**: Content analysis and response strategy
- **Action Layer**: Summary generation and formatting

### **Dependencies**

- `agno>=2.0.7` - Main framework with YouTube tools
- `youtube-transcript-api>=1.2.2` - Fallback transcript extraction
- `openai>=1.3.0` - AI model integration

## 🎓 **Learning Value**

This agent demonstrates:

- ✅ **Tool Integration**: How agents use external APIs and services
- ✅ **Framework Benefits**: How Agno simplifies complex operations
- ✅ **Parameterization**: Building flexible, reusable agent interfaces
- ✅ **Error Handling**: Graceful handling of API failures and edge cases
- ✅ **User Experience**: Simple command-line interface design

## 🔗 **Related Concepts**

**From Agent Fundamentals:**

- [Tool Use Design Pattern](../../../ai-agents-for-beginners/04-tool-use/README.md)
- [Agent Architecture](../../00-agent-fundamentals/lesson-1-introduction/README.md)

**Related Agents:**

- [Content Generation Agent](../../01-basic-agents/05-generation-agent/)
- [Summarization Agent](../../01-basic-agents/03-summarization-agent/)
- [Research Team](../../05-multi-agent-systems/06-research-team/)

## 🤝 **Contributing**

Ways to enhance this agent:

- 🔧 **Add features**: Batch processing, different output formats
- 🐛 **Fix issues**: Test with various video types and report problems
- 📚 **Improve docs**: Add more usage examples and edge cases
- 🌍 **Extend support**: Multi-language videos, private videos

---

_This agent showcases the power of modern AI frameworks like Agno for building practical, tool-using agents with minimal code._
