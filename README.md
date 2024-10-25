## ${{ values.serviceName }} application

### Files
- main.py: a Flask application
- requirements.txt: dependencies for the application
- Dockerfile

### Testing
build and test locally:
- IMAGE_NAME=${{ values.serviceName }}
- docker build -t $IMAGE_NAME .
- docker run -dp 127.0.0.1:8080:8080 $IMAGE_NAME
- curl 127.0.0.1:8080

cleanup after test:
- docker container rm -f $(docker container ls | grep $IMAGE_NAME | awk '{print $1}')
- docker image rm $IMAGE_NAME
