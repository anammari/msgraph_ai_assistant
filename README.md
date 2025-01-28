# Microsoft Graph AI Assistant

Transform the way you interact with your Microsoft 365 data! This AI-powered assistant lets you chat naturally with your emails, calendar events, and contacts, all through a simple and intuitive interface. Whether you're summarizing your inbox, checking your meetings, or finding important SharePoint files, this app brings the power of AI to your Microsoft 365 workflow. Built with cutting-edge Retrieval-Augmented Generation (RAG) and function calling, it’s your personal assistant for smarter, faster productivity.

## Docker Setup

This guide provides instructions for:
1. **Building, Tagging, and Pushing Docker Images** to Docker Hub (_for developers_).
2. **Pulling and Running the Images** using Docker Compose (_for users_).

---

## **1. Developer Perspective: Build, Tag, and Push Docker Images**

Follow these steps to build, tag, and push the Docker images to Docker Hub.

### **Prerequisites**
- Docker installed on your machine.
- A Docker Hub account.
- Docker logged in (`docker login`).
- A public repository with the name `msgraph_ai_assistant` has been created in Docker Hub.

### **Steps**

1. **Build the Docker Images**:
   - Build the `flask-api` image:
     ```bash
     docker build --platform linux/amd64 -t flask-api -f Dockerfile.flask .
     ```
   - Build the `streamlit-gui` image:
     ```bash
     docker build --platform linux/amd64 -t streamlit-gui -f Dockerfile.streamlit .
     ```

2. **Tag the Images**:
   - Tag the `flask-api` image:
     ```bash
     docker tag flask-api <your-docker-hub-username>/msgraph_ai_assistant:flask-api-amd64
     ```
   - Tag the `streamlit-gui` image:
     ```bash
     docker tag streamlit-gui <your-docker-hub-username>/msgraph_ai_assistant:streamlit-gui-amd64
     ```

3. **Push the Images to Docker Hub**:
   - Push the `flask-api` image:
     ```bash
     docker push <your-docker-hub-username>/msgraph_ai_assistant:flask-api-amd64
     ```
   - Push the `streamlit-gui` image:
     ```bash
     docker push <your-docker-hub-username>/msgraph_ai_assistant:streamlit-gui-amd64
     ```

4. **Verify the Images on Docker Hub**:
   - Go to your Docker Hub repository: [https://hub.docker.com/r/your-docker-hub-username/msgraph_ai_assistant](https://hub.docker.com/r/ahmadammari/msgraph_ai_assistant).
   - Ensure the images `flask-api-amd64` and `streamlit-gui-amd64` are listed.

---

## **2. User Perspective: Pull and Run the Images Using Docker Compose**

Follow these steps to pull and run the Docker images on another machine using Docker Compose.

### **Prerequisites**
- Docker and Docker Compose installed on the target machine.
- A `docker-compose.yml` file (provided below).

### **Steps**

1. **Create a `docker-compose.yml` File**:
  - Create a file named `docker-compose.yml` with the following content:
     ```yaml
     version: '3.8'

     services:
       flask_api:
         image: <your-docker-hub-username>/msgraph_ai_assistant:flask-api-amd64
         container_name: flask_api
         environment:
           - FLASK_ENV=development
         ports:
           - "5000:5000"
         volumes:
           - ./config.cfg:/app/config.cfg

       streamlit_gui:
         image: <your-docker-hub-username>/msgraph_ai_assistant:streamlit-gui-amd64
         container_name: streamlit_gui
         environment:
           - BASE_URL=http://flask_api:5000
         ports:
           - "8501:8501"
         volumes:
           - ./config.cfg:/app/config.cfg
         depends_on:
           - flask_api
     ```

  - **Alternatively**: If you haven't built your own Flask and Streamlit Docker images as in the above steps, you can simply use the pre-existing `docker-compose.yml` file in this repository:

    ```yaml
     version: '3.8'

     services:
       flask_api:
         image: ahmadammari/msgraph_ai_assistant:flask-api-amd64
         container_name: flask_api
         environment:
          - FLASK_ENV=development
         ports:
          - "5000:5000"
         volumes:
          - ./config.cfg:/app/config.cfg

       streamlit_gui:
         image: ahmadammari/msgraph_ai_assistant:streamlit-gui-amd64
         container_name: streamlit_gui
         environment:
          - BASE_URL=http://flask_api:5000
         ports:
          - "8501:8501"
         volumes:
          - ./config.cfg:/app/config.cfg
         depends_on:
          - flask_api
    ```

2. **Pull the Images**:
   - Run the following command to pull the images from Docker Hub:
     ```bash
     docker-compose pull
     ```

3. **Run the Containers**:
   - Start the containers in detached mode:
     ```bash
     docker-compose up -d
     ```

4. **Access the Services**:
   - **Flask REST API**: Accessible at `http://localhost:5000`.
   - **Streamlit GUI**: Accessible at `http://localhost:8501`.

5. **Stop the Containers**:
   - When you’re done, stop the containers:
     ```bash
     docker-compose down
     ```

---

## **Configuration File (`config.cfg`)**

The application requires a `config.cfg` file for secrets (e.g., Azure App registration, Gemini API key). This file is mounted into the containers using a volume.

### **Option 1: Use `configure_app.py` to Auto-Generate `config.cfg`**

1. **Run the Configuration Script**:
   - Execute the following command to run the `configure_app.py` script:
     ```bash
     python configure_app.py
     ```
   - Follow the prompts to input your Azure App registration details and Gemini API key.

2. **Verify the File**:
   - A `config.cfg` file will be created in the current directory with the provided details.

### **Option 2: Manually Create `config.cfg`**

1. **Create the File**:
   - Create a file named `config.cfg` in the same directory as `docker-compose.yml`.

2. **Add the Following Content**:
   - Replace placeholders with actual values:
     ```
     [azure]
     clientId = your-client-id
     clientSecret = your-client-secret
     tenantId = your-tenant-id
     userId = your-user-id

     [gemini]
     google_api_key = your-gemini-api-key
     ```

---

## **Troubleshooting**

1. **Permission Denied**:
   - Ensure you’re logged in to Docker Hub (`docker login`).
   - Verify the repository name and tag are correct.

2. **Port Conflicts**:
   - Ensure ports `5000` (Flask) and `8501` (Streamlit) are not in use.

3. **Missing `config.cfg`**:
   - Ensure the `config.cfg` file exists and is correctly formatted.

---

## **Repository Structure**

```
msgraph_ai_assistant/
├── Dockerfile.flask
├── Dockerfile.streamlit
├── docker-compose.yml
├── config.cfg
├── configure_app.py
├── app.py
├── rag_gui.py
└── requirements.txt
```

---

## **Contact**

For questions or issues, contact [Ahmad Ammari](mailto:ammariect@gmail.com).
