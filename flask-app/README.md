# Overview
- Template to start a Flask application

# Usage

## Local 
```
export ENV_FILE=env/dev.env
./run.sh
```

## Container
```
docker build . -t flask-app
docker run -p <host-port>:80 -e ENV_FILE='env/prod.env' <image-name>
```
