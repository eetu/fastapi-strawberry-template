# Python Flask with Strawberry template

## Install

Create virtualenv

```bash
python -m venv .venv # template was tested with python 3.11.x but should work with version that supports ASGI
```

activate virtualenv

```bash
source .venv/bin/activate.fish # for fish shell
```

Install dependencies

```bash
make install
```

## Development

To start development server

```bash
make dev
```

Query graphql

```bash
curl --request POST \
  --url http://localhost:8000/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"query {message}"}'
```

## Testing

Run linter

```bash
make lint
make lint_fix # reformat code
```

Run tests

```bash
make test

```
