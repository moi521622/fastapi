FROM python:3.11-buster

# Fix typo in the environment variable
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# Install Poetry
RUN pip install poetry

# Copy the dependency files
COPY pyproject.toml* poetry.lock* ./

# Configure Poetry to use in-project virtualenvs
RUN poetry config virtualenvs.in-project true

# Install dependencies if pyproject.toml exists
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# Empty entrypoint
ENTRYPOINT ["poetry","run","uvicorn","api.main:app","--host","0.0.0.0","--reload"]
