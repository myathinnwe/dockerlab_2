# dockerlab_2
# build docker image using ENV in py file

# commands
- docker build -t <image-name>:<img-version> . --build-arg PORT=$PORT
- docker run -p $PORT:$PORT <imagename>:<version>
- docker images
- docker ps
