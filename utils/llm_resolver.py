import os

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


def get_developer_llm() -> BaseChatModel:
    if "ANTHROPIC_API_KEY" in os.environ:
        return ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0)
    elif "OPENAI_API_KEY" in os.environ:
        return ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    elif "GOOGLE_API_KEY" in os.environ:
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
    else:
        raise Exception("No API key found for any LLM provider")


def get_general_purpose_llm() -> BaseChatModel:
    if "OPENAI_API_KEY" in os.environ:
        return ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    elif "ANTHROPIC_API_KEY" in os.environ:
        return ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0)
    elif "GOOGLE_API_KEY" in os.environ:
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
    else:
        raise Exception("No API key found for any LLM provider")


def get_long_context_llm() -> BaseChatModel:
    if "GOOGLE_API_KEY" in os.environ:
        return ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
    elif "OPENAI_API_KEY" in os.environ:
        return ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    elif "ANTHROPIC_API_KEY" in os.environ:
        return ChatAnthropic(model="claude-3-5-sonnet-latest", temperature=0)
    else:
        raise Exception("No API key found for any LLM provider")
