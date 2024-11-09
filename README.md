# Vultr-Cloud-Innovate-Hackathon---Phase-2-Submission
Vultr Cloud Innovate Hackathon - Phase 2 Submission- project building
Smart Agriculture and Plant Care: AI-Powered Cultivation and Disease Management
This repository contains the codebase for an AI-powered platform designed to assist farmers, gardeners, and plant nurseries in optimizing plant cultivation and disease management. Leveraging cloud infrastructure and machine learning models, this platform provides personalized recommendations for plant care and early disease detection.


Features:
AI-Powered Cultivation Recommendations: Tailored suggestions for irrigation, nutrient management, and planting schedules.
Disease Detection: Early disease identification through image analysis.
User Customization: Reminders for plant care, optimal plant placement, and sustainability tips.
Architecture Overview
This project utilizes several services from Vultr for storage, compute, and scalability:

Vultr Kubernetes Engine (VKE): Manages machine learning models and backend services.
Vultr Load Balancer: Ensures high availability and performance across different regions.
Vultr Block Storage: Used for scalable storage of datasets and backups.
Prerequisites
Node.js and npm for frontend and backend setup.
Python 3.8+ for machine learning model development.
Docker and kubectl for containerization and Kubernetes deployment.
Vultr Account with access to Object Storage, Kubernetes Engine, and Load Balancer services.
Git for version control.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/AryanAthreya/Vultr-Cloud-Innovate-Hackathon---Phase-2-Submission.git

Backend Setup

Navigate to the backend directory:

bash
Copy code
cd backend
Install dependencies:

bash
Copy code
npm install
Frontend Setup

Navigate to the frontend directory:

bash
Copy code
cd ../frontend
Install dependencies:

bash
Copy code
npm install
Machine Learning Model Setup

Navigate to the model directory:

bash
Copy code
cd ../model
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Environment Configuration
Create an .env file in the root directory and set up the following environment variables:

plaintext
Copy code
# Vultr API credentials
VULTR_API_KEY=your_vultr_api_key

# Database configuration
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

# Object Storage
VULTR_OBJECT_STORAGE_ENDPOINT=your_vultr_object_storage_endpoint
VULTR_OBJECT_STORAGE_BUCKET=your_bucket_name

# Kubernetes and Load Balancer
K8S_CLUSTER_NAME=your_kubernetes_cluster_name
LOAD_BALANCER_NAME=your_load_balancer_name
Usage
Start the Backend Server

bash
Copy code
cd backend
npm start
Start the Frontend Application

bash
Copy code
cd ../frontend
npm start
Testing the Machine Learning Model

For local testing of the disease detection model, use sample images in the model/test_images directory:

bash
Copy code
cd ../model
python test_model.py --image_path=test_images/sample_image.jpg
API Endpoints
POST /api/upload: Uploads an image for disease analysis.
GET /api/recommendations: Fetches personalized plant care recommendations.
GET /api/history: Retrieves user data and previous analysis.
For detailed API documentation, see the API.md file in this repository.

Deployment
Dockerize the Application

Build Docker images for both backend and frontend:

bash
Copy code
docker build -t backend:latest ./backend
docker build -t frontend:latest ./frontend
Push these images to a container registry (e.g., Docker Hub).

Kubernetes Deployment on Vultr

Create a Kubernetes cluster on Vultr and configure your local kubectl to access it.

Deploy the application using Kubernetes manifests in the k8s directory:

bash
Copy code
kubectl apply -f k8s
Setup Vultr Load Balancer

Configure a Vultr Load Balancer and connect it to the Kubernetes cluster to manage incoming traffic.
