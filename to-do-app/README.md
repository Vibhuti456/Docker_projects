
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
#### You wwill get the task table 

```bash
  SELECT * FROM tasks;
```
Show the data inside the table. 
