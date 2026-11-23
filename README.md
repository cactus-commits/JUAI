# JUAI

## Setup projket structure

### 1. Initialize the project

Create the root project (a workspace root without its own package):

```bash
uv init --no-package --python 3.13
```

### 2. Create workspace packages

Separate packages for the backend and frontend, so they can be dockerized independently:

```bash
uv init --package backend
uv init --package frontend
```

### 3. Add dependencies

Add the dependencies in each package's `pyproject.toml`, and also in the root `pyproject.toml`.

### 4. Install everything

```bash
uv sync --all-packages
```