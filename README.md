# Apache Airflow Docker Compose

This Docker Compose file sets up Apache Airflow along with its dependencies like PostgreSQL and Redis.

## Requirements
- Docker
- Docker Compose

## Usage
1. Clone this repository.
2. Navigate to the directory containing docker-compose.yaml.
3. Run the following command: 

`mkdir -p ./dags ./logs ./plugins ./config`

`echo -e "AIRFLOW_UID=$(id -u)" > .env`

`docker compose up airflow-init`

`docker-compose up -d`

5. Access Airflow UI at http://localhost:8080.

## Services
- **PostgreSQL:** Database backend for Airflow.
- **Redis:** Backend for Celery, used for task queueing.
- **Webserver:** Apache Airflow Webserver.
- **Scheduler:** Apache Airflow Scheduler.

## Volumes
- **postgres-db-volume:** Volume to persist PostgreSQL data.

## Notes
- This setup uses Apache Airflow version 2.9.1.


