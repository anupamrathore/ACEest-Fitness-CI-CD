
# ACEest Fitness & Gym — CI/CD DevOps Project

This repository contains the **ACEest Fitness & Gym** web application and its **end-to-end CI/CD pipeline implementation** using **Flask**, **Docker**, **Jenkins**, and **Kubernetes (Minikube)**.  
It demonstrates automation of **build, test, containerization, and deployment** workflows for a real-world software delivery setup.



**Project Overview**

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



*Application Structure*
<img width="366" height="393" alt="image" src="https://github.com/user-attachments/assets/749c1ec2-2a97-4d4c-bc07-9c1c831947c7" />



**Setup Instructions**

*Clone the Repository*
  - bash: git clone https://github.com/anupamrathore/ACEest-Fitness-CI-CD.git
  - cd ACEest-Fitness-CI-CD

 *Create Virtual Environment (optional)*
  - bash py -3.11 -m venv venv
  - venv\Scripts\activate
  - pip install -r requirements.txt

 *Run Flask App Locally*
  - bash python wsgi.py  (or via Flask CLI)
  - flask run: App will be available at: http://127.0.0.1:5000/

 *Run Tests (Pytest)*
  - bash: py -3.11 -m pytest -q
  - Expected output: 2 passed in 0.23s
      <img width="890" height="455" alt="image" src="https://github.com/user-attachments/assets/5a02c77d-f9e6-473d-90bf-f1f56b13cdb1" />

 *Dockerization*
  - Build Docker Image
  - bash docker build -t aceest/fitness-app:v1 .
  - Run Container: docker run -d --name aceest_test -p 5001:5000 aceest/fitness-app:v1
  - Then visit: http://localhost:5001
      <img width="884" height="464" alt="image" src="https://github.com/user-attachments/assets/df15564c-3994-470b-9133-26cbc24ecbca" />
       <img width="810" height="424" alt="image" src="https://github.com/user-attachments/assets/6f5a70cf-e0d9-4fcd-b6da-d50dce0432dc" />


 *Kubernetes (Minikube)*
   - Start Cluster
   - bash: minikube start --driver=docker --memory=3500 --cpus=2
   - Load Image and Apply Manifests: bash: minikube image load aceest/fitness-app:v1
   - kubectl apply -f k8s/
   - Access Application: bash: minikube service aceest-service --url
   - You’ll see a URL like http://127.0.0.1:57445/ — open it in your browser.
    <img width="854" height="452" alt="image" src="https://github.com/user-attachments/assets/ddbaaef3-97b4-4062-9c6c-269715f73912" />
    <img width="876" height="466" alt="image" src="https://github.com/user-attachments/assets/e179a0d6-266a-4e36-a5bf-4a57aa54e024" />

*CI/CD Pipeline (Jenkins Overview)*
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
      - Then open http://localhost:8080 and create a pipeline job linked to this repo.


  *CI/CD Architecture Overview*

<img width="348" height="372" alt="image" src="https://github.com/user-attachments/assets/234ccf5e-9675-4692-b0a3-df78474915a9" />


 *Key Automation Outcomes*
 - Fully automated testing and containerized builds.
 - Local CI/CD setup with Jenkins + Minikube.
 - Modular and easily extendable pipeline for cloud deployment (AWS/GCP/Azure).
