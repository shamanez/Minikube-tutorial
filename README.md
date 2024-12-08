# My Minikube Tutorial

This project demonstrates deploying a Flask application on a Minikube cluster.

## Prerequisites
- Docker
- Minikube
- kubectl

## Setup

1. Clone this repository and navigate to the project directory:
    ```bash
    git clone https://github.com/your-repo/my-minikube-tutorial.git
    cd my-minikube-tutorial
    ```

2. Set proper permissions for script folders:
    ```bash
    chmod +x scripts/*.sh
    ```

3. Start Minikube and deploy the application:
    ```bash
    ./scripts/start.sh
    ```

4. Access the application:
    ```bash
    minikube service hello-world-service --url
    ```

5. Stop and clean up the cluster:
    ```bash
    ./scripts/stop.sh
    ```

### **How It All Works Together**

1. **Start Minikube**
    - Initializes a 3-node cluster
    - Prepares Docker to build the image within Minikube

2. **Build and Deploy**
    - Docker builds the Flask application image
    - Kubernetes resources (ConfigMap, Deployment, Service) are applied

3. **Access the Application**
    - The `LoadBalancer` service exposes the application externally
    - Use the URL provided by Minikube to test the application

4. **Clean Up**
    - Stops Minikube and deletes resources
