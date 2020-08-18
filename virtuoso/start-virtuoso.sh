if [ ! "$(docker ps -q -f name=ddiem-virtuoso)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=ddiem-virtuoso)" ]; then
        # cleanup
        echo "cleaned up virtuoso container"
        docker stop ddiem-virtuoso
        docker rm ddiem-virtuoso
    fi
    # run your container
    echo "running virtuoso container"
    docker-compose up -d
    sleep 15;

elif [ "$(docker ps -q -f name=ddiem-virtuoso)" ]; then
    echo "Virtuoso container already running"
fi