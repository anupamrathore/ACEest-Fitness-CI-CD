
# ACEest Fitness & Gym — CI/CD DevOps Project

This repository contains the **ACEest Fitness & Gym** web application and its **end-to-end CI/CD pipeline implementation** using **Flask**, **Docker**, **Jenkins**, and **Kubernetes (Minikube)**.  
It demonstrates automation of **build, test, containerization, and deployment** workflows for a real-world software delivery setup.



###Project Overview

**Goal:**  
To design and implement a **fully automated CI/CD pipeline** for a Python Flask-based gym management application — including testing, containerization, image management, and Kubernetes deployment.

**Tools & Technologies:**
- **Version Control:** Git + GitHub  
- **Build & CI Server:** Jenkins  
- **Testing:** Pytest  
- **Code Quality:** SonarQube (optional integration)  
- **Containerization:** Docker  
- **Orchestration:** Minikube (Kubernetes)  
- **Language:** Python 3.11 (Flask Framework)  



###Application Structure

<img width="401" height="389" alt="image" src="https://github.com/user-attachments/assets/031185bf-9320-4226-9e90-166020db9af8" />


###Setup Instructions

###Clone the Repository
```bash
git clone https://github.com/anupamrathore/ACEest-Fitness-CI-CD.git
cd ACEest-Fitness-CI-CD

###Create Virtual Environment (optional)
     - bash py -3.11 -m venv venv
     - venv\Scripts\activate
     - pip install -r requirements.txt

###Run Flask App Locally
    - bash python wsgi.py
    # or via Flask CLI
    - flask run: App will be available at: http://127.0.0.1:5000/

###Run Tests (Pytest)
    - bash: py -3.11 -m pytest -q
    - Expected output: 2 passed in 0.23s

     <img width="891" height="482" alt="image" src="https://github.com/user-attachments/assets/9ffb411d-f305-41a9-b831-bb9d7591ca43" />


###Dockerization
      - Build Docker Image
      - bash docker build -t aceest/fitness-app:v1 .
      - Run Container: docker run -d --name aceest_test -p 5001:5000 aceest/fitness-app:v1
      - Then visit: http://localhost:5001

      <img width="882" height="500" alt="image" src="https://github.com/user-attachments/assets/f0d93e5f-9bbf-41d0-abf7-5a3937303e35" />

###Kubernetes (Minikube)
      - Start Cluster
      - bash: minikube start --driver=docker --memory=3500 --cpus=2
      - Load Image and Apply Manifests: bash: minikube image load aceest/fitness-app:v1
      - kubectl apply -f k8s/
      - Access Application: bash: minikube service aceest-service --url
      - You’ll see a URL like http://127.0.0.1:57445/ — open it in your browser.

       <img width="854" height="478" alt="image" src="https://github.com/user-attachments/assets/6f2fb70b-da71-4700-8f61-c0ec2eec523e" />

       <img width="879" height="494" alt="image" src="https://github.com/user-attachments/assets/6fbfd428-839e-433d-b475-a2ef427551ed" />


###CI/CD Pipeline (Jenkins Overview)
     - Jenkinsfile Stages
     - Checkout Code from GitHub
     - Install Dependencies & Run Tests using Pytest
     - Build Docker Image with version tagging
     - Push Image to Docker Hub (optional)
     - Deploy to Kubernetes (via Minikube)
     - Run Jenkins in Docker (Optional)
           - bash: Copy code: docker run -d --name jenkins -p 8080:8080 -p 50000:50000 \
           - bash: -v jenkins_home:/var/jenkins_home \
           - bash: -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
               Then open http://localhost:8080 and create a pipeline job linked to this repo.


###CI/CD Architecture Overview

<img width="348" height="372" alt="image" src="https://github.com/user-attachments/assets/234ccf5e-9675-4692-b0a3-df78474915a9" />


###Key Automation Outcomes
    - Fully automated testing and containerized builds.
    - Local CI/CD setup with Jenkins + Minikube.
    - Modular and easily extendable pipeline for cloud deployment (AWS/GCP/Azure).
