FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    langchain \
    langchain-anthropic \
    langgraph \
    flake8 \
    detect-secrets \
    pip-audit \
    pytest

WORKDIR /workspace
