FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

USER vscode

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:$HOME/.local/bin"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PYTHONUNBUFFERED 1

WORKDIR /workspace
COPY --chown=vscode . .