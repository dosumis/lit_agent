"""Unit tests for agent connection module."""

import pytest
from unittest.mock import Mock, patch
from lit_agent.agent_connection import AgentConnection, OpenAIAgent, AnthropicAgent


@pytest.mark.unit
class TestAgentConnection:
    """Test the base AgentConnection class."""

    def test_agent_connection_is_abstract(self):
        """Test that AgentConnection cannot be instantiated directly."""
        with pytest.raises(TypeError):
            AgentConnection()

    def test_agent_connection_requires_api_key(self):
        """Test that concrete agents require an API key."""
        with pytest.raises(ValueError, match="API key is required"):
            OpenAIAgent(api_key=None)

        with pytest.raises(ValueError, match="API key is required"):
            AnthropicAgent(api_key=None)


@pytest.mark.unit
class TestOpenAIAgent:
    """Test the OpenAI agent implementation."""

    def test_openai_agent_initialization(self):
        """Test OpenAI agent can be initialized with valid API key."""
        agent = OpenAIAgent(api_key="test-key")
        assert agent.api_key == "test-key"
        assert agent.model == "gpt-3.5-turbo"  # default model

    def test_openai_agent_custom_model(self):
        """Test OpenAI agent can use custom model."""
        agent = OpenAIAgent(api_key="test-key", model="gpt-4")
        assert agent.model == "gpt-4"

    @patch('requests.post')
    def test_openai_agent_query(self, mock_post):
        """Test OpenAI agent can make queries."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Hello world example response"}}]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        agent = OpenAIAgent(api_key="test-key")
        response = agent.query("Hello world coding example")

        assert response == "Hello world example response"
        mock_post.assert_called_once()


@pytest.mark.unit
class TestAnthropicAgent:
    """Test the Anthropic agent implementation."""

    def test_anthropic_agent_initialization(self):
        """Test Anthropic agent can be initialized with valid API key."""
        agent = AnthropicAgent(api_key="test-key")
        assert agent.api_key == "test-key"
        assert agent.model == "claude-3-haiku-20240307"  # default model

    def test_anthropic_agent_custom_model(self):
        """Test Anthropic agent can use custom model."""
        agent = AnthropicAgent(api_key="test-key", model="claude-3-opus-20240229")
        assert agent.model == "claude-3-opus-20240229"

    @patch('requests.post')
    def test_anthropic_agent_query(self, mock_post):
        """Test Anthropic agent can make queries."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "content": [{"text": "Hello world example response"}]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        agent = AnthropicAgent(api_key="test-key")
        response = agent.query("Hello world coding example")

        assert response == "Hello world example response"
        mock_post.assert_called_once()


@pytest.mark.unit
class TestAgentFactory:
    """Test the agent factory functionality."""

    @patch.dict('os.environ', {'OPENAI_API_KEY': 'test-openai-key'})
    def test_create_openai_agent_from_env(self):
        """Test creating OpenAI agent from environment variables."""
        from lit_agent.agent_connection import create_agent_from_env

        agent = create_agent_from_env('openai')
        assert isinstance(agent, OpenAIAgent)
        assert agent.api_key == 'test-openai-key'

    @patch.dict('os.environ', {'ANTHROPIC_API_KEY': 'test-anthropic-key'})
    def test_create_anthropic_agent_from_env(self):
        """Test creating Anthropic agent from environment variables."""
        from lit_agent.agent_connection import create_agent_from_env

        agent = create_agent_from_env('anthropic')
        assert isinstance(agent, AnthropicAgent)
        assert agent.api_key == 'test-anthropic-key'

    def test_create_agent_invalid_provider(self):
        """Test creating agent with invalid provider raises error."""
        from lit_agent.agent_connection import create_agent_from_env

        with pytest.raises(ValueError, match="Unsupported provider"):
            create_agent_from_env('invalid')