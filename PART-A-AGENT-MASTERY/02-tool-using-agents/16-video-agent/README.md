# 🎬 YouTube Video Downloader Agent

> **Tool-Using Agent**: Extract MP4 videos from YouTube URLs using the most reliable method

## 🎯 **What This Agent Does**

Downloads MP4 videos from YouTube URLs with minimal code using `yt-dlp` (the most robust YouTube downloader).

**Agent Type**: Tool-Using Agent (⭐⭐⭐⭐⭐ complexity)  
**Primary Tool**: [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Modern, reliable YouTube downloader

## 🚀 **How to Run**

### **Installation**

```bash
# Navigate to the agent directory
cd PART-A-AGENT-MASTERY/02-tool-using-agents/16-video-agent/

# Install dependencies
pip install -r requirements.txt
```

### **Basic Usage**

```bash
# Download best quality video (recommended)
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --clear-cache

# Download to specific directory
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --output "./my_videos"

# Download specific quality with cache clearing
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --quality "720p" --clear-cache
```

## 📋 **Available Quality Options**

| Quality Option | Description               | Use Case                           |
| -------------- | ------------------------- | ---------------------------------- |
| `best`         | Highest available quality | High-quality archival              |
| `worst`        | Lowest available quality  | Quick downloads, limited bandwidth |
| `720p`         | 720p resolution           | Balanced quality/size              |
| `480p`         | 480p resolution           | Smaller file size                  |
| `1080p`        | 1080p resolution          | High definition                    |

## 💻 **Usage Examples**

### **Successful Download Example**

```bash
# Successfully tested with Notion 3.0 Agents video
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=R1cF4T4lgI4" --clear-cache
# Result: ./downloads/Introducing Notion 3.0： Agents.mp4 (3.3 MB)
```

### **Troubleshooting YouTube Restrictions**

```bash
# If download fails, try with cache clearing
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --clear-cache

# Different quality if specific format unavailable
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --quality "best"
```

### **Batch Processing**

```bash
# Download multiple videos to organized directory
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO1" --output "./educational_content"
python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO2" --output "./educational_content"
```

## 🛠️ **Technical Details**

### **Why yt-dlp?**

Based on research, `yt-dlp` is the **most reliable option** because:

- ✅ **Actively maintained** with frequent updates
- ✅ **Handles YouTube changes** better than alternatives
- ✅ **Supports thousands of sites** beyond just YouTube
- ✅ **Robust error handling** and retry mechanisms
- ✅ **Format flexibility** (MP4, WebM, audio-only, etc.)

### **Agent Architecture**

```python
# Minimal implementation following tool-use pattern
class VideoDownloaderAgent:
    def download_video(self, url: str, quality: str = "best") -> dict:
        # Configure yt-dlp options
        opts = {'format': quality, 'outtmpl': '%(title)s.%(ext)s'}

        # Download with error handling
        with YoutubeDL(opts) as yt:
            yt.download([url])
```

### **Dependencies & YouTube API Fixes**

- `yt-dlp>=2024.1.0` - Latest version handles YouTube API changes
- **Nightly builds recommended**: `pip install -U --pre yt-dlp`

### **YouTube API Workarounds (2024-2025)**

The agent includes fixes for common YouTube issues:

- ✅ **User-Agent Spoofing**: Bypasses bot detection
- ✅ **Cache Clearing**: `--clear-cache` flag removes corrupted cache
- ✅ **Retry Logic**: Handles temporary API failures
- ✅ **Latest yt-dlp**: Uses cutting-edge fixes for YouTube changes

**Common Issues & Solutions:**

- `HTTP Error 403: Forbidden` → Use `--clear-cache` flag
- `Precondition check failed` → Upgrade yt-dlp to nightly version
- `nsig extraction failed` → User-Agent spoofing (built into agent)

## 🎓 **Learning Value**

This agent demonstrates:

- ✅ **Minimal Code Approach**: Maximum functionality with ~80 lines of code
- ✅ **Tool Integration**: Using powerful external libraries (yt-dlp) effectively
- ✅ **Production Robustness**: Handles YouTube API changes and restrictions
- ✅ **Error Handling**: Graceful handling of download failures and API issues
- ✅ **User Interface**: Simple command-line with helpful options
- ✅ **File Operations**: Organized download management with custom directories
- ✅ **Real-World Testing**: Successfully downloads videos (tested with Notion 3.0 video)

## 🔗 **Related Agents**

**Complementary Agents:**

- [YouTube Content Analyzer](../21-youtube-agent/) - Extract transcripts and summaries
- [Audio Agent](../15-audio-agent/) - Extract audio from downloaded videos
- [File System Agent](../04-file-system-agent/) - Organize downloaded files

**Combined Workflow:**

1. Use **Video Downloader Agent** to get MP4 file (`./downloads/video.mp4`)
2. Use **YouTube Content Analyzer** to get transcript and summary
3. Use **File System Agent** to organize files by topic/date

**Example Combined Usage:**

```bash
# Step 1: Download video
python ../16-video-agent/video_downloader_agent.py --url "https://www.youtube.com/watch?v=R1cF4T4lgI4" --clear-cache

# Step 2: Analyze content
python ../21-youtube-agent/youtube_agent.py --url "https://www.youtube.com/watch?v=R1cF4T4lgI4" --action "summarize" --demo
```

## 🤝 **Contributing**

Ways to enhance this agent:

- 🔧 **Add features**: Playlist support, subtitle download, thumbnail extraction
- 🐛 **Fix issues**: Test with different video types and report YouTube API problems
- 📚 **Improve docs**: Add more troubleshooting guides for YouTube restrictions
- 🌍 **Extend support**: Other video platforms (Vimeo, Dailymotion), batch processing
- ⚡ **Performance**: Parallel downloads, progress bars, resume capabilities

## 🛡️ **Known Limitations**

- **YouTube Restrictions**: Some videos are protected and cannot be downloaded
- **API Changes**: YouTube frequently updates APIs, requiring yt-dlp updates
- **Geographic Blocks**: Some content may be restricted in certain regions
- **Copyright Protection**: Commercial content often blocks automated downloads

**Solution**: The agent handles these gracefully and provides clear error messages.

---

_This agent showcases how to build robust, production-ready functionality with minimal code while handling real-world API challenges._
