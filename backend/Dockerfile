FROM python:3.13-alpine AS builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --link-mode=copy --compile-bytecode

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --compile-bytecode --no-editable

FROM python:3.13-alpine

# Use the non-root user to run our application
ARG USER=nonroot
RUN adduser -D $USER
USER nonroot

COPY --from=builder --chown=app:app /app/.venv /app/.venv

ENTRYPOINT [ "/app/.venv/bin/pathways" ]
