# RPN Calculator API

## Project Structure

```md
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── operations.py
│   ├── export_csv.py
│   ├── utils.py
│   ├── schemas.py
├── tests
│   ├── __init__.py
│   ├── test_operations.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
├── requirements.txt
```

## Description
This project is an API for evaluating expressions in Reverse Polish Notation (RPN) and storing the results in a Redis database. The API also provides functionality to export the stored operations and results to a CSV file.

## Features
- Evaluate RPN expressions
- Store operations and results in Redis
- Export stored operations and results to a CSV file
- Swagger and redoc documentation
- unit tests of some operations

## Prerequisites
Make sure you have the following installed:
- Docker
- Docker Compose
- Git

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/foutejordan/rpn_service.git
cd rpn_service
```

### Step 2: Create a .env File

Create a .env file in the root directory of the project and add the following environment variables:
- REDIS_HOST=redis
- REDIS_PORT=6379

### Step 3: Build and Run the Services

Use Docker Compose to build and start the services:
```bash
docker compose up --build
```
This command will:

- Build the python Docker image specified in the Dockerfile.
- Start the containers for the python API and Redis services as defined in the docker-compose.yml file.

### Step 4: Access the API

After starting the services, you can access the API documentation at the following URLs:

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## Endpoints
### Evaluate RPN Expression

- URL: /evaluate/
- Method: POST
- Request Body
```json
{
  "npi_expression": "3 4 + 2 * 7 /"
}
```
- Response example
```json
{
  "result": 2.0,
  "execution_time": 0.000123
}
```

### Export Operations to CSV
- URL: /export-csv/
- Method: GET
- Response: A CSV file with the stored operations and results.

