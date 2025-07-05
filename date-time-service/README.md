
# Date-Time Service Microservice 🕰️

This microservice is part of the **Logs Service** domain and is responsible for providing the current server date and time. It allows clients to retrieve the exact time from the server whenever needed.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/Logs-Service)

## Docker Image 🐳
- **Docker Image:** `kamartinez/time`

## Purpose 🎯
The **Date-Time Service** microservice provides the current date and time from the server. Clients can make a request to get the current time whenever they need it, ensuring they are getting the time from the server's environment.

## Architecture Style 🏗️
- **Microservice Architecture**: This service is designed as a standalone microservice, specifically for providing the server's date and time.
- **Design Pattern**: The system follows the **MVC (Model-View-Controller)** design pattern, with clear separation of concerns between the model (data), the view (user interface), and the controller (business logic).

## Technologies 💻
- **Programming Language:** Python
- **Containerization:** Docker (optional)
- **API Integration:** REST APIs for retrieving the server's date and time

## Project Structure 🧑‍💻
The repository is structured as follows:

```
date-time-service/
├── app/                      # Contains the application logic.
│   ├── __init__.py           # Initialization file for the app.
│   ├── routes.py             # Defines the routes for the Date-Time service.
│   └── services.py           # Contains the business logic for fetching the date and time.
│
├── config/                   # Configuration files for setting up the environment.
│   ├── __pycache__/          # Cache files generated during runtime.
│   └── config.py             # Main configuration file for application setup.
│
├── Dockerfile                # Docker configuration for the containerized service.
├── requirements.txt          # Lists the dependencies for the Date-Time service.
└── README.md                 # This file.
```

### Folder Descriptions 📂
- **app/**: Contains the core logic for the application, including routes for handling incoming requests and services that implement the business logic.
- **config/**: Contains configuration files and the necessary setup for the environment in which the service will run.
- **Dockerfile**: Provides a configuration for building the microservice container with Docker, making it easy to deploy across various environments.
- **requirements.txt**: Specifies the Python dependencies necessary for the Date-Time service to run, such as web frameworks and utilities.

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
   - Build the Docker image for the Date-Time service:
     ```bash
     docker build -t kamartinez/time .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 kamartinez/time
     ```

5. **Access the Service:**
   - The service will be accessible on `http://localhost:5000` once the container is running.

## Features ✨
- **Date and Time Retrieval**: Allows clients to securely retrieve the current date and time from the server.
- **Modular Architecture**: The microservice is modular and easily extendable for other time-related functionalities.
- **Docker Integration**: Easily deployable as a Docker container, ensuring a smooth experience across different environments.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
