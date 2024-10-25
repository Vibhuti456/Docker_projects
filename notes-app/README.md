# Notes Application 


## Deployment
To deploy this website on first we need to create a volume and network for effective Deployment.

How to create Volume

```bash
  docker volume create note-apps
```

How to check the list of volume

```bash 
  docker volume ls 
```

Create Network

```bash 
  docker network create notes-apps
```

How to check the list of network

```bash
  docker network ls
```

Run SQL Container with volume and network

```bash 
  docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=notes_db -v mysql_data:/var/lib/mysql -p 3306:3306 -d mysql:5.7
```

How to check running and stopping Container

```bash 
  docker ps -a 
```

Build a Image

```bash 
  docker build -t notes-app .
```

How to run the flask container

```bash 
  docker run --name flask-container --link mysql-container:mysql -e MYSQL_HOST=mysql -e MYSQL_USER=root -e MYSQL_PASSWORD=root -e MYSQL_DATABASE=notes_db -p 5000:5000 -d notes-app
``` 

How to check logs in docker

```bash 
  docker logs <container-id>
```

Create the notes Table

Once both containers are up and running, you need to create the notes table in the MySQL database. You can do this by accessing the MySQL container and executing the SQL command as described earlier:

```bash 
  docker exec -it mysql-container mysql -u root -p
``` 

Enter the password root.

```bash
  USE notes_db;
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL
);
```




