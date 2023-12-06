# dockerlab_2
# build docker image using ENV in py file

# commands
- docker build -t <image-name>:<img-version> . --build-arg PORT=$PORT
- docker run -p $PORT:$PORT <imagename>:<version>
- docker images
- docker ps


# if want to delete container use>> docker stop <container id>
                                >> docker rm <container id>

# if want to check logs -
  - docker logs -f <containerid>

# if want to check CPU / MEMORY / STATUS / LIMIT
- docker stats
# if want to check about process inside container
- docker top <containerid>

