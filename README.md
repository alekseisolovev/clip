# Clip

Video Q&A with LLMs.

## Prerequisites

Before running the app, create an `.env` file in the project's root directory and add your Google API key.
```bash
GOOGLE_API_KEY="AI..."
```

## Running the App

To run the Streamlit app using Docker Compose, follow these steps.

1. In the project directory, build and start the service:
    ```bash
    docker-compose up --build app
    ```
2. Open your browser and go to: `http://localhost:8501/`

3. To stop the app, press `Ctrl+C` in the terminal.
