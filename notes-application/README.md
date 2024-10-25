
# Notes Application 




## Deployment

To deploy this website on first we need to create a volume and network for effective Deployment.

How to create Volume

```bash 
  docker volume create notes_db_data
```

How to check the list of volume

```bash
  docker volume ls 
```

Create Network

```bash 
  docker network create notes-network
```

How to check the list of network

```bash
  docker network ls 
```

Run SQL Container with volume and network

```bash 
  docker run -d \
  --name notes-db \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=notes_db \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=userpass \
  -v notes_db_data:/var/lib/mysql \
  --network notes-network \
  mysql:5.7
```

How to check running and stopping Container

```bash 
  docker ps -a 
```

Build a Image

```bash 
  docker build -t notes-app-image .
```

How to run the flask container

```bash 
  docker run -d \
  --name notes-app \
  -p 5000:5000 \
  -e FLASK_ENV=development \
  -e MYSQL_HOST=notes-db \
  -e MYSQL_DATABASE=notes_db \
  -e MYSQL_USER=user \
  -e MYSQL_PASSWORD=userpass \
  -v "$(pwd)/app:/app" \
  --network notes-network \
  notes-app-image
```

How to open SQL container

```bash 
  docker exec -it notes-db mysql -u root -p 
``` 

How to check logs in docker

```bash 
  docker logs <container-id>
```

## Docker Compose Commands 

```bash 
  docker-compose up --build -d 
```


