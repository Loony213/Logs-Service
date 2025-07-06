
# Visit Counter Service Microservice 👀

This microservice is part of the **Logs Service** domain and is responsible for tracking and counting the number of visits to a specific page. It provides insights into user engagement by counting the visits to pages in your application.

## Repository Link 📁
- [GitHub Repository](https://github.com/Loony213/Logs-Service)

## Docker Image 🐳
- **Docker Image:** `kamartinez/count`

## Purpose 🎯
The **Visit Counter Service** microservice tracks the number of times a specific page or endpoint is visited. By integrating it into your application, you can monitor page visits, helping to gather data for user interaction, content popularity, and engagement.

## Architecture Style 🏗️
- **Microservice Architecture**: This service is designed as a standalone microservice focused solely on counting and tracking page visits.
- **Design Pattern**: The system follows the **MVC (Model-View-Controller)** design pattern, ensuring separation of concerns where the controller handles requests, the service contains the logic for counting visits, and the model interacts with the data.

## Technologies 💻
- **Programming Language:** Python
- **Containerization:** Docker (optional)
- **API Integration:** REST APIs for tracking page visits

## Project Structure 🧑‍💻
The repository is structured as follows:

```
visit-counter-service/
├── app.py                    # Main entry point for running the application.
├── requirements.txt          # Lists the dependencies for the Visit Counter service.
├── Dockerfile                # Docker configuration for building the microservice container.
└── README.md                 # This file.
```

### Folder Descriptions 📂
- **app.py**: The main entry point for the Visit Counter service. It handles the routes for tracking page visits.
- **requirements.txt**: Specifies the Python dependencies necessary for the Visit Counter service to run, such as web frameworks and utilities.
- **Dockerfile**: Provides a configuration for building and deploying the Visit Counter microservice in a Docker container.

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
   - Build the Docker image for the Visit Counter service:
     ```bash
     docker build -t kamartinez/count .
     ```
   - Run the container:
     ```bash
     docker run -p 5000:5000 kamartinez/count
     ```

5. **Access the Service:**
   - The service will be accessible on `http://localhost:5000` once the container is running.

## Features ✨
- **Page Visit Tracking**: Tracks and counts the number of visits to a page or endpoint.
- **Modular Architecture**: The microservice is modular and can easily be extended to track visits to multiple pages or sections.
- **Docker Integration**: The service can be deployed easily as a Docker container for seamless scaling and deployment.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
