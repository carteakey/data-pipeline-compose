# data-pipeline-compose
Docker Compose for big data processing using Hadoop, Hive, PySpark, Spark, Jupyter, and Airflow. 

This Docker Compose setup is designed to provide a full-fledged environment for data processing and analytics, including data storage, processing, workflow, and analysis.

It serves as a good starting point to create an easy-to-deploy learning environment for data enthusiasts. 

Sensible defaults and project structure are used, and the services are configured to seamlessly interact with each other.

Example Project: [world-energy-stats](https://github.com/carteakey/world-energy-stats)

## Running Locally

Spin up all services.
```bash
docker compose up -d
```

Check status of services.
```bash
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"
```

Stop and remove everything (Warning - all data will be erased).
```bash
docker compose down --volumes --remove-orphans
```

Get Token for Jupyter server.
```bash
docker exec spark-notebook jupyter server list
```

Run Hive.
```
docker exec -it hive-server hive
```

## Services

| Service | Component | Description | URL |
|---------|-----------|-------------|-----|
| **Hadoop** | | | |
| | `namenode` | NameNode, managing metadata. | localhost:9870, localhost:9010 |
| | `datanode` | DataNode, storing data. | localhost:9864 |
| | `resourcemanager` | ResourceManager, managing resources. | localhost:8088 |
| | `nodemanager1` | NodeManager, managing containers on a node. | localhost:8042 |
| | `historyserver` | HistoryServer, providing application history UI. | localhost:8188 |
| **Spark** | | | |
| | `spark-master` | Spark Master, managing Spark resources. | localhost:8080, localhost:7077 |
| | `spark-worker-1` | Spark Worker, executing Spark tasks. | localhost:8081 |
| | `spark-worker-2` | Another Spark Worker. | localhost:8083 |
| **Hive** | | | |
| | `hive-server` | Hive Server, providing JDBC interface. | localhost:10000 |
| | `hive-metastore` | Hive Metastore, storing metadata. | localhost:9083 |
| | `hive-metastore-postgresql` | PostgreSQL for Hive Metastore, backend DB. | - |
| **Airflow** | | | |
| | `airflow-webserver` | Airflow Webserver, monitoring and managing workflows. | localhost:8082 |
| | `airflow-scheduler` | Airflow Scheduler, scheduling jobs. | - |
| | `airflow-worker` | Airflow Worker, executing tasks. | - |
| | `airflow-triggerer` | Airflow Triggerer, handling triggers. | - |
| | `airflow-init` | Airflow Initializer, setting up Airflow. | - |
| | `airflow-cli` | Airflow CLI, command-line interface. | - |
| | `flower` | Flower, monitoring Celery clusters. | localhost:5555 |
| | `postgres` | PostgreSQL for Airflow, backend DB. | - |
| | `redis` | Redis, message broker for Airflow. | - |
| **Other Services** | | | |
| | `docker-proxy` | Socat-based proxy for Docker daemon. | localhost:2376 |
| | `spark-notebook` | Jupyter Notebook for PySpark and analysis. | localhost:8888 |

Note that services without exposed ports do not have URLs listed.


## FAQ

#### Why 2 environment files?
- The .env file will be used by docker-compose to adjust the environment of the docker-compose command itself. (Specifically for airflow)

- The docker-compose.env is defined as an env_file inside the yaml and will take environment variables from the file and inject them into the container. (For Hadoop & Hive)

#### Looks like you just mashed up all services in 1 compose file. 
- That is correct, the point is to just streamline the initial configuration process without the usual setup hassles e.g. incompatible versions, port conflicts, integration between services, mounting volumes - making it easier to get a data environment up and running, especially for beginners.

#### What's the docker-proxy for?
- To allow Airflow to run docker commands.

