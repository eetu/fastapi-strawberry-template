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
pip install -r requirements.txt
```

## Development

To start app

```bash
flask --app flaskr run --debug
```

Call hello world route

```bash
curl http://localhost:5000/hello
```

Call api rest route

```bash
curl --request GET \
  http://localhost:5000/api/
```

Call graphql view

```bash
curl --request POST \
  --url http://localhost:5000/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"query {\n\thello\n}"}'
```

## Testing

Run tests

```bash
python -m pytest

```
