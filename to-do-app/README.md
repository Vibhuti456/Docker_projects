
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
  docker run --name mysql -e MYSQL_ROOT_PASSWORD=rootpass
```
How to check running and stopping Container 

```bash 
  docker ps -a 
```
Build a Image

```bash 
  docker build -t to-do-app .
```

How to run the flask container 

```bash
  docker run -d --name flask-app --link mysql:db -p 5000:5000 to-do-app
```

How to inspect network to check container info 

```bash 
  docker network inspect todo_network
```

How to open SQL container 

```bash 
  docker exec -it mysql bash
  mysql -u root -p
```

How to check logs in docker 

```bash 
  docker logs <container-id>
```
  

### If any errors occurs SQL related to Password Access and flask container 

SQL command 

```bash 
docker run --rm --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d mysql --skip-grant-tables
``` 

If Table doesn't exist 

```bash 
  docker exec -it mysql bash
  mysql -u root -p 
```
Give root password of your SQL container and we will get the access of SQL container

#### Create the Database

```bash 
  CREATE DATABASE todo
```
#### Switched to new database 

```bash 
  USE todo
```

#### Create a table inside it

```bash
  CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

