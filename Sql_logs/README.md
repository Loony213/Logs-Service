
# SQL Logs Microservice 📝

This microservice is part of the **Logs Service** domain and is responsible for generating logs of SQL database operations. It logs SQL activities such as inserts, updates, and deletions to help monitor and track database changes.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/Logs-Service)

## Docker Image 🐳
- **Docker Image:** `kamartinez/sql-logs`

## Purpose 🎯
The **SQL Logs** microservice provides the functionality of logging SQL database operations (e.g., inserts, updates, and deletions). It helps monitor and keep track of database activities for auditing, troubleshooting, and system performance analysis.

## Architecture Style 🏗️
- **Microservice Architecture**: This service is designed as a standalone microservice, focusing specifically on logging database operations.
- **Design Pattern**: The system follows the **MVC (Model-View-Controller)** design pattern, ensuring clear separation between the data (model), logic (controller), and user-facing features (view).

## Technologies 💻
- **Programming Language:** Python
- **Containerization:** Docker (optional)
- **Database Interaction:** SQL Server (via TinyTds)
- **API Integration:** REST APIs for logging database operations

## Project Structure 🧑‍💻
The repository is structured as follows:

```
Sql_logs/
├── config/                   # Configuration files for setting up the environment.
│   └── config.py             # Main configuration file for application setup.
│
├── logs/                     # Contains the core logic for logging database operations.
│   ├── .env                  # Environment variables file for sensitive information.
│   ├── config.py             # Configuration settings for the logging service.
│   ├── logs_processor.py     # Logic for processing and storing logs.
│   ├── .gitignore            # Ignores files and folders from being tracked by Git.
│   └── hola.html             # HTML file for basic testing or monitoring.
│
├── app.py                    # Main entry point to run the application.
├── Dockerfile                # Docker configuration for building the microservice container.
├── requirements.txt          # Lists the dependencies for the SQL Logs service.
└── README.md                 # This file.
```

### Folder Descriptions 📂
- **config/**: Contains configuration files necessary for setting up the environment in which the service will run.
- **logs/**: This folder contains the core logic for processing and storing SQL logs. It includes configuration files and processing scripts that handle the database operations logging.
- **app.py**: The main entry point of the application, responsible for setting up routes and managing service operations.
- **Dockerfile**: Provides a configuration for building and deploying the SQL Logs microservice in a Docker container.
- **requirements.txt**: Specifies the Python dependencies necessary for the SQL Logs service to run.

## How to Deploy ⚙️
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Loony213/Logs-Service.git
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Service:**
   - After installing the dependencies, you can start the application:
     ```bash
     python app.py
     ```

4. **Docker Deployment:**
   - Build the Docker image for the SQL Logs service:
     ```bash
     docker build -t kamartinez/sql-logs .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 kamartinez/sql-logs
     ```

5. **Access the Service:**
   - The service will be accessible on `http://localhost:5000` once the container is running.

## Features ✨
- **SQL Logging**: Logs SQL database operations (insert, update, delete) for auditing, monitoring, and troubleshooting purposes.
- **Modular Architecture**: The microservice is modular and easily extendable for other types of logging.
- **Database Integration**: Interacts with SQL Server for capturing logs of database operations.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
