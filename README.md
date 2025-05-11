# FastAPI Deployment with GitHub Actions & AWS ECS

**Deploy_FastAPI_Github_Action_AWS_ECS** is a GitHub repository for automating the deployment of a FastAPI application to AWS ECS using GitHub Actions. It includes CI/CD workflows for building, testing, containerizing, and deploying the application seamlessly.

This repository demonstrates how to deploy a FastAPI application using GitHub Actions for CI/CD and AWS Elastic Container Service (ECS) for hosting. The project includes automated workflows for formatting, testing, building, and deploying the application.

---

## 1. Project Structure

The project is organized as follows:

```
|-- config/
|   |-- __init__.py          # Initialization file for the config module
|   |-- config.py            # Contains MongoDB client configuration
|
|-- model/
|   |-- __init__.py          # Initialization file for the model module
|   |-- model.py             # Implements the Generative AI model logic
|
|-- routes/
|   |-- __init__.py          # Initialization file for the routes module
|   |-- routes.py            # Defines API endpoints for the application
|
|-- tests/
|   |-- __init__.py          # Initialization file for the tests module
|   |-- test_app_routes.py   # Unit tests for the API routes
|
|-- .github/
|   |-- workflows/
|       |-- ci-cd-pipeline.yaml  # GitHub Actions workflow for CI/CD
|
|-- __init__.py              # Root initialization file
|-- app.py                   # Main application entry point
|-- requirements.txt         # Python dependencies
|-- README.md                # Project documentation
|-- .gitignore               # Files and directories to ignore in Git
|-- .env                     # Environment variables (not included in version control)
|-- .dockerignore            # Files and directories to ignore in Docker builds
|-- Dockerfile               # Docker configuration for containerizing the app
|-- setup.py                 # Python package setup file
```

---

## 2. Setting Up the Environment

### Step 1: Create a Virtual Environment
To isolate dependencies, create a virtual environment:

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment
Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Install the required Python packages:

```bash
pip install --no-cache-dir -r requirements.txt
```

---

## 3. Configuring Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE_NAME=your_database_name
MONGODB_SESSION_HISTORY_COLLECTION=your_collection_name
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
```

These variables are used for connecting to MongoDB, accessing OpenAI and Gemini APIs, and deploying to AWS.

---

## 4. Running the Application Locally

To start the FastAPI application locally, use the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

- `--host 0.0.0.0`: Makes the application accessible on all network interfaces.
- `--port 8000`: Specifies the port to run the application.
- `--reload`: Enables auto-reloading during development.

Once the application is running, you can access the API documentation at `http://localhost:8000/docs`.

---

## 5. Building and Running the Docker Container

### Step 1: Build the Docker Image
Build the Docker image for the application:

```bash
docker build -t generative_ai_app:latest .
```

### Step 2: Run the Docker Container
Run the containerized application:

```bash
docker run -d -p 8000:8000 --name generative_ai_app_container generative_ai_app:latest
```

- `-d`: Runs the container in detached mode.
- `-p 8000:8000`: Maps port 8000 of the container to port 8000 on the host machine.

---

## 6. CI/CD Pipeline with GitHub Actions

The project includes a GitHub Actions workflow defined in `.github/workflows/ci-cd-pipeline.yaml`. The pipeline performs the following steps:

1. **Code Formatting Check**: Ensures the code adheres to the Black formatting standard.
2. **Unit Testing**: Runs the tests in `tests/test_app_routes.py` to verify API functionality.
3. **Docker Image Build and Push**: Builds the Docker image and pushes it to Amazon Elastic Container Registry (ECR).
4. **Deployment to AWS ECS**: Updates the ECS task definition and deploys the application to the ECS cluster.

---

## 7. Deployment to AWS ECS

### 7.1 Create a S3 Bucket for the .env File

- Upload the .env file to the S3 bucket to store environment variables.

### 7.2 Create Cluster, Task Definition, & Service in AWS ECS

The application is deployed to AWS ECS using the following steps:

1. **Build and Push Docker Image**:
   - The Docker image is built and pushed to Amazon ECR using the GitHub Actions workflow.

2. **Update ECS Task Definition**:
   - The ECS task definition is updated with the new Docker image.

3. **Deploy to ECS Service**:
   - The updated task definition is deployed to the ECS service.

### 7.3 Configure AWS Credentials in GIThub Secrets

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `AWS_ECR_REPO`
- `LATEST_IMAGE_URI`

---

## 8. Testing the API

Unit tests for the API routes are located in `tests/test_app_routes.py`. To run the tests, use:

```bash
pytest -v tests/test_app_routes.py
```

The tests cover the following scenarios:

- Successful responses from the `/query_response` endpoint.
- Error handling for missing or invalid input.
- Exception handling for model-related errors.
- Structure validation for session history responses.

---

## 9. Additional Notes

- **MongoDB Integration**: The application uses MongoDB to store session history. Ensure that the MongoDB instance is running and accessible.
- **Generative AI Models**: The application supports OpenAI and Gemini models for generating responses. Configure the respective API keys in the `.env` file.
- **Health Check Endpoint**: The `/health` endpoint can be used to verify the application's health.

---

## 10. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 11. Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

## 12. Contact

For any questions or issues, please contact:

**Author**: Amir Aziz  
**Email**: amirds0235@gmail.com