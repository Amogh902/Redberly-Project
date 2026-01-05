#  CI Pipeline using Jenkins, SonarQube, and Docker

##  Overview

This project implements a **Continuous Integration (CI) pipeline** using **Jenkins**, **SonarQube**, and **Docker**, strictly aligned with the provided problem statement.

The pipeline automatically pulls source code from a GitHub repository, performs static code analysis using SonarQube with **Quality Gate enforcement**, builds a Docker image **only if the quality check passes**, and sends email notifications based on the build status.

---

##  Problem Statement

Set up Jenkins on a local machine and configure a CI pipeline to:

* Pull source code from GitHub
* Perform SonarQube code analysis
* Enforce SonarQube Quality Gates
* Build Docker image only on successful quality check
* Send email notifications for build success, failure, and errors
* Ensure all configurations (URLs, credentials, image tags, recipients, thresholds) are externally configurable and not hardcoded

###  Expected Outcome

A fully automated and configurable CI pipeline that builds Docker images, enforces code quality via SonarQube, and sends email notifications for all build statuses.

---

##  Tools & Technologies

* **Jenkins** – CI automation server
* **GitHub** – Source code management
* **SonarQube** – Static code analysis and Quality Gates
* **Docker** – Container image build
* **AWS EC2 (Ubuntu)** – Jenkins and SonarQube host
* **SMTP (Gmail)** – Email notifications

---

##  Environment Setup & Prerequisites

The following steps were performed to prepare the CI environment:

### 1️ Jenkins Installation

* Jenkins installed on Ubuntu server
* Jenkins service enabled and running

### 2️ Docker Installation

* Docker installed on the same server
* Docker daemon enabled and running

### 3️ Jenkins Docker Permissions

* Jenkins user added to the Docker group to allow Docker commands from pipelines

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

### 4️ Jenkins Plugins Installed

The following Jenkins plugins were installed and configured:

* Git Plugin
* GitHub Plugin
* Pipeline Plugin
* SonarQube Scanner Plugin
* Email Extension Plugin
* Credentials Plugin

---

##  SonarQube Setup (Docker-based)

SonarQube was deployed as a **Docker container** to provide a consistent and isolated code quality analysis service.

### Deployment Details

* SonarQube runs as a Docker container on the Ubuntu server
* Official SonarQube Community Edition Docker image is used
* SonarQube is exposed on port `9000`

```bash
docker run -d \
  --name sonarqube \
  -p 9000:9000 \
  sonarqube:9.9-community
```
![](/images/sonarqube-container-ss.png)

### Jenkins Integration

* Jenkins connects to SonarQube via HTTP (`http://<server-ip>:9000`)
* SonarQube authentication token is generated and stored securely in Jenkins Credentials Store
* SonarQube Scanner is configured as a Jenkins-managed tool
* Jenkins enforces the Quality Gate before proceeding to the Docker image build stage

---

##  Repository Structure

```
.
├── app.py              # Sample application code
├── requirements.txt    # Application dependencies
├── Dockerfile          # Docker image definition
├── Jenkinsfile         # Jenkins CI pipeline
└── README.md           # Project documentation
```

---

##  CI Pipeline Workflow

```
GitHub Repository
        ↓
Jenkins Checkout
        ↓
SonarQube Code Analysis
        ↓
Quality Gate Validation
        ↓ (PASS)
Docker Image Build
        ↓
Email Notification
```

---

##  Jenkins Credentials Configuration

To meet security and configurability requirements, the following credentials were created in Jenkins **Credentials Store**:

### 1️ GitHub Credentials

* Used for secure access to the GitHub repository (if required)

### 2️ SonarQube Token

* Used to authenticate Jenkins with SonarQube server

### 3️ SMTP Credentials

* Used for sending email notifications
* Gmail App Password configured for SMTP authentication

All credentials are referenced securely in the pipeline and are **not hardcoded**.

---

##  Jenkins Pipeline Stages

### 1️ Checkout Code

* Jenkins pulls the source code from the GitHub repository.

### 2️ SonarQube Analysis

* Static code analysis is performed using SonarQube Scanner.
* Jenkins-managed tools are used (no hardcoded paths).

### 3️ Quality Gate Enforcement

* Jenkins waits for the SonarQube Quality Gate result.
* The pipeline **aborts or fails** if the Quality Gate conditions are not met.

### 4️ Docker Image Build

* Docker image is built **only after the Quality Gate passes**.
* The image is built locally on the Jenkins server.

### 5️ Email Notifications

* Email notifications are sent for:

  * Build Success
  * Build Failure
  * Pipeline Aborted (Quality Gate failure or timeout)

---

##  Configuration & Security Best Practices

* No credentials are hardcoded in the Jenkinsfile
* Jenkins Credentials Store is used for all secrets
* URLs, image names, recipients, and thresholds are defined using environment variables
* Pipeline logic remains environment-agnostic

---

##  Jenkinsfile

The CI pipeline is defined using a declarative Jenkinsfile. All configurations such as URLs, credentials, image tags, and recipients are externalized using environment variables and Jenkins credentials.

> Refer to `Jenkinsfile` in the repository for the complete pipeline definition.

---

##  Outputs & Screenshots

The following outputs were captured to demonstrate pipeline execution:

* Jenkins pipeline execution (successful)
 
  ![](/images/jenkins-output-ss.png)

* SonarQube dashboard showing Quality Gate status both SUCCESS and FAILURE
 
  * SUCCESS
  ![](/images/sonarqube-output.png)

  * FAILURE
  ![](/images/sonarqube-output%20fail.png) 

* Email notification received both SUCCESS and FAILURE
 
  * SUCCESS  
  ![](/images/email-recieved.png)

  * FAILURE
  ![](/images/email-recieved_fail.png)

* Docker image created on Jenkins server
 
  ![](/images/dockerimage-created-ss.png)


---

## Sample Application

A simple application is included to validate:

* GitHub code checkout
* SonarQube static analysis
* Conditional Docker image build

---

##  Conclusion

This project demonstrates:

* A fully automated CI pipeline using Jenkins
* Code quality enforcement via SonarQube Quality Gates
* Conditional Docker image creation
* Secure and configurable pipeline design

The implementation strictly adheres to the given problem statement and focuses exclusively on **Continuous Integration (CI)**.

---


