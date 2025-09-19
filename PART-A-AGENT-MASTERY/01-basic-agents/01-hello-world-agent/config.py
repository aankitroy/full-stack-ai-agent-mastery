"""Configuration settings for the Hello World Agent"""

import os
from typing import Dict, Any

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-3.5-turbo"

# Agent Configuration
DEFAULT_PERSONALITY = "friendly_assistant"
MAX_CONVERSATION_HISTORY = 10
DEFAULT_RESPONSE_TIMEOUT = 30

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_CONVERSATIONS = True

# Performance Settings
MAX_TOKENS = 150
TEMPERATURE = 0.7

# Available personalities
PERSONALITIES: Dict[str, str] = {
    "friendly_assistant": "Helpful and warm conversational partner",
    "technical_expert": "Knowledgeable technical specialist",
    "creative_companion": "Imaginative and inspiring creative partner"
}
