"""Agent connection module for OpenAI and Anthropic APIs."""

import os
from abc import ABC, abstractmethod
from typing import Dict, Any

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AgentConnection(ABC):
    """Abstract base class for agent connections."""

    def __init__(self, api_key: str):
        """Initialize agent connection with API key.

        Args:
            api_key: API key for the service

        Raises:
            ValueError: If API key is None or empty
        """
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key

    @abstractmethod
    def query(self, prompt: str) -> str:
        """Query the agent with a prompt.

        Args:
            prompt: The prompt to send to the agent

        Returns:
            The agent's response
        """
        pass


class OpenAIAgent(AgentConnection):
    """OpenAI agent implementation."""

    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """Initialize OpenAI agent.

        Args:
            api_key: OpenAI API key
            model: Model to use (default: gpt-3.5-turbo)
        """
        super().__init__(api_key)
        self.model = model
        self.base_url = "https://api.openai.com/v1/chat/completions"

    def query(self, prompt: str) -> str:
        """Query OpenAI API with a prompt.

        Args:
            prompt: The prompt to send

        Returns:
            The model's response

        Raises:
            requests.RequestException: If API request fails
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 150
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]


class AnthropicAgent(AgentConnection):
    """Anthropic agent implementation."""

    def __init__(self, api_key: str, model: str = "claude-3-haiku-20240307"):
        """Initialize Anthropic agent.

        Args:
            api_key: Anthropic API key
            model: Model to use (default: claude-3-haiku-20240307)
        """
        super().__init__(api_key)
        self.model = model
        self.base_url = "https://api.anthropic.com/v1/messages"

    def query(self, prompt: str) -> str:
        """Query Anthropic API with a prompt.

        Args:
            prompt: The prompt to send

        Returns:
            The model's response

        Raises:
            requests.RequestException: If API request fails
        """
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }

        payload = {
            "model": self.model,
            "max_tokens": 150,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data["content"][0]["text"]


def create_agent_from_env(provider: str) -> AgentConnection:
    """Create an agent from environment variables.

    Args:
        provider: Either 'openai' or 'anthropic'

    Returns:
        Configured agent instance

    Raises:
        ValueError: If provider is unsupported or API key not found
    """
    if provider.lower() == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        return OpenAIAgent(api_key)
    elif provider.lower() == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        return AnthropicAgent(api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider}")