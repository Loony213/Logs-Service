
# Logs Service Microservices 📊

This repository is part of the **Logs Service** domain, which contains microservices designed for logging and monitoring various operations. The domain consists of several microservices that provide different logging and tracking functionalities, including logging SQL database operations, fetching server time, and counting page visits.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/Logs-Service)

## Microservices Overview 🚀
### 1. **SQLLogs**
   - Purpose: Logs SQL database operations, such as inserts, updates, and deletes, for tracking database activities.

### 2. **DateTime Service**
   - Purpose: Provides the current server date and time, allowing clients to fetch the time whenever needed.

### 3. **Visit Counter Service**
   - Purpose: Tracks and counts page visits, providing insights into how many times a specific page has been visited.

## Architecture Style 🏗️
- **Microservice Architecture**: Each functionality is encapsulated into its own microservice, allowing independent scalability, maintenance, and development.
- **Design Pattern**: The system follows a **modular design**, allowing each service to operate independently while being part of a larger system. Services interact through well-defined APIs, ensuring loose coupling between services.

## Technologies 💻
- **Programming Language**: Each microservice is implemented using appropriate technologies and languages (e.g., Node.js, Ruby, etc.).
- **Containerization**: Docker is used to package the microservices, making them portable and easy to deploy across different environments.
- **Service Communication**: The microservices communicate using REST APIs, which allows them to be easily integrated into any larger system or application.

## Project Structure 🧑‍💻
The repository is structured as follows:

```
Logs-Service/
├── .github/workflows/         # Contains the GitHub Actions workflows for CI/CD automation.
│   └── new.yml                # Configuration for automated workflows.
│
├── Sql_logs/                  # Microservice to log SQL database operations.
│   └── requirements.txt       # Lists the dependencies for the SQL logs service.
│
├── date-time-service/         # Microservice for retrieving the server's current date and time.
│   └── Dockerfile             # Docker configuration for building the DateTime service container.
│
├── visit-counter-service/     # Microservice to track and count page visits.
│   └── Dockerfile             # Docker configuration for building the Visit Counter service container.
│
├── README.md                  # This file.
└── requirements.txt           # Lists general dependencies for the entire project.
```

### Folder Descriptions 📂
- **.github/workflows/**: Contains configuration files for automated CI/CD workflows using GitHub Actions.
- **Sql_logs/**: The microservice that logs SQL operations (like insert, update, and delete) to track database activities.
- **date-time-service/**: Provides functionality to get the server's current date and time.
- **visit-counter-service/**: Keeps track of page visits, helping measure user engagement with the website.
- **requirements.txt**: Specifies the dependencies needed for the services to run.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/Logs-Service.git
   ```

2. **Install Dependencies:**
   - Navigate to each service directory (e.g., `Sql_logs/`, `date-time-service/`, `visit-counter-service/`) and install the required dependencies listed in the `requirements.txt` file or Dockerfile.

3. **Run the Microservices:**
   - After setting up the dependencies, you can run each service individually or use Docker to deploy them in containers.
   - Example for Docker:
     ```bash
     docker build -t kamartinez/sql-logs .
     docker run -p 5000:5000 kamartinez/sql-logs
     ```

4. **Access the Services:**
   - The services will be accessible on `http://localhost:5000` (or a different port depending on your configuration) once they are running.

## Features ✨
- **SQL Logging**: Logs SQL database operations like insertions, updates, and deletions for tracking purposes.
- **Date and Time Retrieval**: Provides the current server date and time on demand.
- **Page Visit Tracking**: Tracks and counts page visits, offering insights into website usage and traffic patterns.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
