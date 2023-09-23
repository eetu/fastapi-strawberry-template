# Python Flask with Strawberry template

## Install

install [pyenv, pyenv-virtual](https://github.com/pyenv/pyenv) (with auto activation)

Create virtual env, template was created with python 3.11.5

```bash
pyenv virtualenv flask-strawberry-template
```

Install dependencies

```bash
pip install flask[async] strawberry-graphql pytest pytest-asyncio pylint black

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
