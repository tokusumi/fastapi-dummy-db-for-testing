# fastapi-dummy-db-for-testing

How to create temporary clean Database for each FastAPI unit-test.

## Requirements

* Poetry

## Setup

```bash
$ poetry install
```

## Run testing

```bash
$ poetry run pytest tests
```

Notice that main DB (`test.db`) is created but include no items, even if test passed.
`test_temp.db` was temporary created for only testing and dropped after testing.
