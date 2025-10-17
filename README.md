# Data-Streaming-Pipeline

Realtime Streaming Pipeline to learn about the streaming process using Kafka, Airflow, and Spark.

Data from randomuser API, u can get the API  [here](https://randomuser.me/api/)

## Overview

This project demonstrates a real-time data streaming pipeline that integrates the following technologies:

- **Apache Kafka**: Used for real-time data ingestion and message brokering.
- **Apache Airflow**: Orchestrates the pipeline and schedules tasks.
- **Apache Spark**: Processes and analyzes the streaming data in real time.
## Data pipeline arrchitecture

![](./img/Architecture.png)

## Features

- Real-time data ingestion using Kafka producers and consumers.
- Data processing and transformation using Spark Streaming.
- Workflow orchestration and monitoring with Airflow.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.8 or higher
- Docker and Docker Compose
- Java (for Spark and Kafka)
- Apache Airflow CLI (optional)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Data-Streaming-Pipeline.git
   cd Data-Streaming-Pipeline
   ```

2. **Set up the environment**:
   Ensure you have Docker and Docker Compose installed. Then, build and start the services:
   ```bash
   make pull 
   make up
   ```

3. **Start the Airflow scheduler and webserver**:
   Access the Airflow UI at `http://localhost:8080` after starting the services.

4. **Run the Spark Streaming job**:
   Submit the Spark job to process the Kafka stream:
   ```bash
   make spark-submit
   ```

## Usage

1. **Produce messages to Kafka**:
   Use a Kafka producer to send messages to the topic:
   ```bash
   kafka-console-producer --broker-list localhost:9092 --topic <your-topic>
   ```

2. **Monitor the pipeline**:
   - Check the Airflow UI for task status.
   - View Spark logs for processing details.

3. **Consume processed messages**:
   Use a Kafka consumer to read processed messages:
   ```bash
   kafka-console-consumer --bootstrap-server localhost:9092 --topic <processed-topic> --from-beginning
   ```

## Architecture Details

The data pipeline follows these steps:

1. **Data Ingestion**:
   - Data is fetched from the Random User API and sent to Kafka topics using Kafka producers.
   - Kafka acts as a message broker, ensuring reliable delivery of messages.

2. **Data Processing**:
   - Spark Streaming consumes messages from Kafka topics.
   - The data is transformed and enriched in real-time.

3. **Workflow Orchestration**:
   - Airflow schedules and monitors the pipeline tasks.
   - DAGs (Directed Acyclic Graphs) define the task dependencies and execution order.

4. **Data Output**:
   - Processed data is sent to another Kafka topic or stored in a database for further analysis.

## Sample Data

### Input Data (from Random User API):
```json
{
  "results": [
    {
      "gender": "female",
      "name": {
        "title": "Miss",
        "first": "Jennie",
        "last": "Nichols"
      },
      "location": {
        "street": {
          "number": 8929,
          "name": "Valwood Pkwy",
        },
        "city": "Billings",
        "state": "Michigan",
        "country": "United States",
        "postcode": "63104",
        "coordinates": {
          "latitude": "-69.8246",
          "longitude": "134.8719"
        },
        "timezone": {
          "offset": "+9:30",
          "description": "Adelaide, Darwin"
        }
      },
      "email": "jennie.nichols@example.com",
      "login": {
        "uuid": "7a0eed16-9430-4d68-901f-c0d4c1c3bf00",
        "username": "yellowpeacock117",
        "password": "addison",
        "salt": "sld1yGtd",
        "md5": "ab54ac4c0be9480ae8fa5e9e2a5196a3",
        "sha1": "edcf2ce613cbdea349133c52dc2f3b83168dc51b",
        "sha256": "48df5229235ada28389b91e60a935e4f9b73eb4bdb855ef9258a1751f10bdc5d"
      },
      "dob": {
        "date": "1992-03-08T15:13:16.688Z",
        "age": 30
      },
      "registered": {
        "date": "2007-07-09T05:51:59.390Z",
        "age": 14
      },
      "phone": "(272) 790-0888",
      "cell": "(489) 330-2385",
      "id": {
        "name": "SSN",
        "value": "405-88-3636"
      },
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/75.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/75.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/75.jpg"
      },
      "nat": "US"
    }
  ],
  "info": {
    "seed": "56d27f4a53bd5441",
    "results": 1,
    "page": 1,
    "version": "1.4"
  }
}
```

### Processed Data (after Spark Transformation):
```json
{
  "first_name": "Alma",
  "last_name": "Larsen",
  "gender": "female",
  "address": "4433 Faaborgvej, Ishoej, Midtjylland, Denmark",
  "post_code": 49531,
  "email": "alma.larsen@example.com",
  "username": "whitepanda327",
  "dob": "1956-11-02T19:51:23.675Z",
  "registered_date": "2016-08-23T00:33:01.866Z",
  "phone": "92001097",
  "picture": "https://randomuser.me/api/portraits/med/women/10.jpg"
}
```

## Troubleshooting

- **Kafka Broker Not Reachable**:
  Ensure Kafka is running and accessible at `localhost:9092`.
- **Airflow Scheduler Issues**:
  Restart the Airflow scheduler using:
  ```bash
  airflow scheduler
  ```
- **Spark Job Fails**:
  Check the logs for detailed error messages and ensure all dependencies are installed.

## Testing

1. **Unit Tests**:
   - Write unit tests for individual components (e.g., Kafka producer, Spark transformations).

2. **Integration Tests**:
   - Test the end-to-end pipeline by simulating data ingestion and verifying the output.

3. **Run Tests**:
   - Use the following command to execute tests:
   ```bash
   make test
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Random User API](https://randomuser.me/api/) for providing sample data.
- Open-source contributors for Kafka, Spark, and Airflow.


