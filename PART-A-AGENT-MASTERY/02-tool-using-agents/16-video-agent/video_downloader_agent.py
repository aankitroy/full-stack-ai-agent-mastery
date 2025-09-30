#!/usr/bin/env python3
"""
YouTube Video Downloader Agent - Simplest Implementation
=======================================================

Minimal code to download MP4 videos from YouTube URLs using yt-dlp.
Supports public, unlisted, and private videos (with authentication).

Usage:
    python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
    python video_downloader_agent.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --quality "720p"
    
Features:
    - Works with unlisted videos using Android API client
    - Automatic retry on failures
    - Custom output directory support
"""

import argparse
from yt_dlp import YoutubeDL


class VideoDownloaderAgent:
    """Simplest possible YouTube video downloader agent"""
    
    def __init__(self):
        self.name = "YouTube Video Downloader Agent"
    
    def download_video(self, url: str, quality: str = "best", output_dir: str = "./downloads") -> dict:
        """
        Download MP4 video from YouTube URL
        
        Args:
            url: YouTube video URL
            quality: Video quality (best, worst, 720p, 480p, etc.)
        
        Returns:
            dict: Download result with status and info
        """
        print(f"🎬 {self.name}")
        print(f"📹 URL: {url}")
        print(f"🎯 Quality: {quality}")
        print()
        
        try:
            # Create output directory if it doesn't exist
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            # Configure download options with YouTube API workarounds
            opts = {
                'format': quality,
                'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Save to specific directory
                'noplaylist': True,  # Only download single video, not playlist
                # Workarounds for YouTube API changes (2024-2025)
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                },
                'extractor_retries': 3,  # Retry on extraction failures
                'fragment_retries': 3,   # Retry on download failures
                # Use Android client to fix unlisted videos and signature extraction issues
                'extractor_args': {
                    'youtube': {
                        'player_client': ['android', 'web'],  # Try Android API first, then web
                    }
                },
            }
            
            print("⏳ Downloading video...")
            
            # Download the video
            with YoutubeDL(opts) as yt:
                # Get video info first
                info = yt.extract_info(url, download=False)
                video_title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)
                
                print(f"📺 Title: {video_title}")
                print(f"⏱️  Duration: {duration // 60}:{duration % 60:02d}")
                print()
                
                # Actually download
                yt.download([url])
                
                print("✅ Download completed successfully!")
                
                return {
                    "status": "success",
                    "title": video_title,
                    "duration": f"{duration // 60}:{duration % 60:02d}",
                    "filename": f"{video_title}.mp4",
                    "url": url
                }
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "url": url
            }


def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description="Download YouTube videos as MP4")
    parser.add_argument("--url", required=True, help="YouTube video URL")
    parser.add_argument("--quality", default="best", 
                       help="Video quality: best, worst, 720p, 480p, etc.")
    parser.add_argument("--output", default="./downloads",
                       help="Output directory for downloaded videos")
    parser.add_argument("--clear-cache", action="store_true",
                       help="Clear yt-dlp cache before downloading (fixes many YouTube errors)")
    
    args = parser.parse_args()
    
    # Clear cache if requested (fixes many YouTube errors)
    if args.clear_cache:
        print("🧹 Clearing yt-dlp cache...")
        import subprocess
        try:
            subprocess.run(["yt-dlp", "--rm-cache-dir"], check=True, capture_output=True)
            print("✅ Cache cleared successfully!")
        except:
            print("⚠️  Cache clearing failed, but continuing...")
        print()
    
    # Create and run agent
    agent = VideoDownloaderAgent()
    result = agent.download_video(args.url, args.quality, args.output)
    
    if result["status"] == "success":
        print(f"\n🎉 Video saved as: {result['filename']}")
    else:
        print(f"\n💡 Tip: Check if the video is available and URL is correct")


if __name__ == "__main__":
    main()
