
# Shopping Cart Website

# Development 




## Deployment

To deploy this website on first we need to create a volume and network for effective Deployment.

# How to create Volume 

```bash
  docker volume create mysql-data
```

# How to check the list of volume 

```bash
  docker volume ls
```
# Create Network

```bash
  docker network create shopping_network
```

# How to check the list of network 

```bash
  docker network ls 
```

# Run SQL Container with volume and network 

```bash 
  docker run --name mysql-db --network shopping_network -e MYSQL_ROOT_PASSWORD=password -v mysql-data:/var/lib/mysql -d mysql:5.7
```
# How to check running and stopping Container 

```bash 
  docker ps -a 
```
# Build a Image

```bash 
  docker build -t flask-shopping-cart .
```

# How to run the flask container 

```bash
  docker run --name flask-app --network shopping_network -p 5000:5000 -d flask-shopping-cart
```

# How to inspect network to check container info 

```bash 
  docker network inspect shopping_network
```

# How to open SQL container 

```bash 
  docker exec -it mysql-db mysql -u root -p
```

# How to check logs in docker 

```bash 
  docker logs <container-id>
```
  

