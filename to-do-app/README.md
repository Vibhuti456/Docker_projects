
# To Do Application







## Deployment

To deploy this website on first we need to create a volume and network for effective Deployment.

How to create Volume 

```bash
  docker volume create todo-app
```

How to check the list of volume 

```bash
  docker volume ls
```
Create Network

```bash
  docker network create todo-network
```

How to check the list of network 

```bash
  docker network ls 
```

Run SQL Container with volume and network 

```bash 
  docker run -d \
--name db \
--network todo-network \
-e MYSQL_ROOT_PASSWORD=rootpass \
-e MYSQL_DATABASE=todo \
mysql:5.7
```
How to check running and stopping Container 

```bash 
  docker ps -a 
```
Build a Image

```bash 
  docker build -t todo-app .
```

How to run the flask container 

```bash
  docker run -d \
--name flask-app \
--network todo-network \
-e MYSQL_HOST=db \
-p 5000:5000 \
todo-app
```

How to inspect network to check container info 

```bash 
  docker network inspect todo_network
```

How to check logs in docker 

```bash 
  docker logs <container-id>
```
How to open SQL container 

```bash 
  docker exec -it mysql bash
  mysql -u root -p
```

Give root password of your SQL container and we will get the access of SQL container

#### Create the Database

```bash 
  SHOW DATABASE todo
```
#### Switched to new database 

```bash 
  USE todo
```
#### You will get the task table 

```bash
  SELECT * FROM tasks;
```
Show the data inside the table. 

#### Commands for docker compose file

```bash
  docker compose up -d
```
#### If you face any issue in docker compose up run follow these commands to resolve 

```bash
  docker-compose exec flask-app printenv | grep MYSQL_HOST
```

```bash
  docker exec -it db netstat -tuln | grep 3306
```

#### Steps to Diagnose and Fix

1. Check the Status of All Services: First, check the status of all services in your Docker Compose setup to see what's happening:

```bash
  docker-compose ps
```

Look for the flask-app service and see if it shows as "Exited" or "Up." If it has exited, you'll need to investigate why

2. Check Logs for Flask Application: Inspect the logs for the Flask application to get more details about why it might not be running:

```bash
  docker-compose logs flask
```
3. Start Services Manually: If the flask-app is not running, try starting the services again:

```bash
  docker-compose up -d
```

4. Inspect Container Exit Codes: If flask-app has exited, you can inspect the exit code to determine why it stopped:

```bash
  docker inspect flask-app --format='{{.State.ExitCode}}'
```
An exit code of 0 typically indicates a successful shutdown.
