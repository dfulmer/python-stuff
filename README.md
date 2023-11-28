# Python Hello World

Hello world application for Python.

## Set up

Clone the repo

```
git clone [copy from above]
cd [directory from above]
```

build container
```
docker-compose build
```

start container
```
docker-compose up -d
```

## Run the program

```
docker-compose run --rm app python helloworld.py
```

## Run the tests

```
docker-compose run --rm app python -m unittest -v tests.tests
```