# Exchagne Rate API ETL

## Introduction
This repository contains an ETL (Extract, Transform, Load) project implemented using Apache Airflow for data extraction from an exchange rate API and exporting the data into an Excel sheet.

## Prerequisites
Ensure the following prerequisites are fulfilled before starting with the project setup:
1. **Install WSL and Ubuntu on Windows**
2. **Install Python**
3. **Install Apache Airflow**

## Setup Instructions
Follow these steps to initialize the project and run it using Apache Airflow:

1. **Initialize Airflow**
2. **Start Airflow and Open UI**
3. **Create User and Password**

## Project Configuration
After setting up Apache Airflow, proceed with the project configuration:

1. **Create a DAG Folder**
   - Location: `\\wsl.localhost\Ubuntu\home\usman\airflow\dags`
2. **Create Python Files**
3. **Import Necessary Libraries**
4. **Initiate Default Arguments**
5. **Initiate DAG**

## Data Handling
Implement the data extraction and loading functions within your Python file:

1. **Data Extraction Function**
   - Fetch data from the exchange rate API.
2. **Load Function**
   - Export rate exchange data into an Excel sheet.
3. **Call Extract and Load Functions**

## Running the DAG
Execute the DAG in Apache Airflow to start the data extraction and loading process:
1. **Run DAG in Airflow**

## Usage
Once everything is set up, manage and monitor your ETL workflow through the Airflow UI.

## run the following command
1. **sudo apt install python3-pip**
2. **pip3 install apache-airflow**
3. **airflow db init**
4. **airflow webserver -p 8080 & airflow scheduler**

