cp ./deploy/docker-compose.yml .
docker swarm init
docker stack deploy -c docker-compose.yml eorder
rm -f ./docker-compose.yml
