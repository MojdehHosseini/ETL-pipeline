# ETL Pipeline with Kafka Setup

## Overview
This repository contains an end-to-end ETL pipeline setup that includes scripts for processing toll data, server access logs, and configuring Apache Kafka. The project is designed to handle data extraction, transformation, and loading (ETL) as well as facilitate real-time data streaming and batch processing.

## Contents
- **Airflow DAGs**: Files to orchestrate ETL processes.
- **Python Scripts**: Automation and data processing scripts.
- **Configuration Files**: Docker and Kafka setup.
- **SQL Scripts**: Schema creation and analytical queries.
- **Data Files**: Sample data used for testing and demonstrations.
- **Diagrams**: ERD and cube diagrams for database structure and analysis.

## Repository Structure
- `dags/`: Contains Apache Airflow DAG files for orchestrating ETL jobs.
  - `ETL_Dag_bash`: Bash script for ETL DAG setup.
- `scripts/`: Python scripts used for various ETL processes.
  - `ETL_toll_data.py`: ETL script for toll data.
  - `ETL_Server_Access_Log_Processing.py`: ETL script for server access logs.
  - `mysqlconnect.py`: Python script to connect to MySQL databases.
  - `automation.py`: Automation tasks for database connections.
- `config/`: Configuration files.
  - `docker-compose.yml`: Docker Compose configuration to set up the environment.
  - `kafka_2.13-3.8.0.tgz`: Apache Kafka setup files.
- `sql/`: SQL scripts for creating schemas and running analytical queries.
  - `create_schema.sql`: Script to create the data warehouse schema.
  - `sales_queries.sql`: Analytical queries for sales data.
- `data/`: Sample data for testing purposes.
  - `electronics.csv`: Sample CSV data for electronics products.
- `diagrams/`: Database structure diagrams.
  - `softcart_ERD.jpg`: Entity Relationship Diagram of the data model.
  - `cube.jpg`: Cube representation for analytics.

## Technologies Used
- **Python**: Core programming language for ETL scripts.
- **Apache Kafka**: Real-time data streaming and processing.
- **Docker**: Containerization of the environment using Docker Compose.
- **Airflow**: Orchestration tool for managing ETL workflows.
- **MySQL**: Database management.
- **PostgreSQL**: Data warehousing.

## Setup Instructions

### Prerequisites
- **Docker** and **Docker Compose**: Install Docker to run the containers.
- **Python**: Version 3.8 or higher.
- **Apache Airflow**: Used to schedule and manage the ETL DAGs.

### Steps
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/etl-pipeline-kafka-setup.git
