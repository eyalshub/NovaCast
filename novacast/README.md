# NovaCast Project

NovaCast is a comprehensive application designed for media processing and chatbot interactions. This project leverages FastAPI for building a high-performance web application, integrating various services for text-to-speech, video processing, and chatbot functionalities.

## Project Structure

The project is organized into several key directories:

- **app/**: Contains the main application code, including API endpoints, core logic, agents, media processing, database models, and services.
- **storage/**: Designated for storing assets, temporary files, and logs.
- **infra/**: Infrastructure as Code (IaC) for cloud deployment, including Kubernetes manifests and Terraform scripts.
- **tests/**: Contains unit and integration tests to ensure the reliability of the application.
- **scripts/**: Utility scripts for running local pipelines and other tasks.
- **docker/**: Docker configurations for containerizing the application.
- **docker-compose.yml**: Defines services and configurations for Docker Compose.
- **Makefile**: Contains build and deployment commands.
- **.env.example**: Example environment configuration.
- **.pre-commit-config.yaml**: Configuration for pre-commit hooks.
- **requirements.txt**: Lists the dependencies required for the project.

## Getting Started

To get started with the NovaCast project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd novacast
   ```

2. **Set Up Environment**:
   Copy the `.env.example` to `.env` and configure your environment variables.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   You can run the FastAPI application using:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API**:
   The API will be available at `http://localhost:8000`. You can access the documentation at `http://localhost:8000/docs`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.