# ETL using Shell Scripts - Hands-on Lab

## Overview
This repository contains shell scripts and instructions for an ETL hands-on lab. The exercises involve extracting, transforming, and loading data using various shell commands, which includes working with data in CSV format, transforming text, and loading it into a PostgreSQL database.

### Objectives
After completing this lab, you will be able to:
- Extract data from a delimited file using `cut`.
- Transform text data using commands like `tr`.
- Load data into a PostgreSQL database using shell commands.

## Repository Contents

### Folders and Files:
- **scripts/**:
  - `cp-access-log.sh`: Shell script that downloads a web server access log, extracts the data, transforms it, and loads it into a PostgreSQL database.
  - `csv2db.sh`: Shell script that extracts user information from the `/etc/passwd` file, transforms it into CSV format, and loads it into a PostgreSQL table.

- **lab-instructions/**:
  - `ETL_Lab_Instructions.pdf`: The original PDF document containing the step-by-step instructions for the lab, detailing each exercise.

## Technologies Used
- **Shell Scripting**: Core commands include `cut`, `tr`, `wget`, `gunzip`.
- **PostgreSQL**: Used for data storage and table creation.
- **Skills Network Cloud IDE**: Used for running scripts and interacting with the database.

## Setup and Usage

### Prerequisites:
- **Docker**: Install Docker to run the PostgreSQL database locally.
- **PostgreSQL**: Ensure PostgreSQL is set up and running. 

### Steps to Use the Scripts:

#### 1. Setting Up the Environment
- Start by cloning this repository:
  ```sh
  git clone https://github.com/yourusername/etl-shell-scripting-lab.git
  cd etl-shell-scripting-lab
