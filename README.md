# WhatsApp API with FastAPI

This project provides a simple API to send WhatsApp messages using FastAPI and the `pywhatkit` library. It allows you to send both text messages and images to any WhatsApp number.

## Features

- Send WhatsApp messages with a simple API call.
- Send both text and images.
- Health check endpoint to monitor the API status.
- Uses `pywhatkit` to automate sending messages through WhatsApp Web.

## Prerequisites

- Python 3.7+
- A WhatsApp account and a logged-in session on WhatsApp Web.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [<repository-url>](https://github.com/Chitraksh-Sharma/pywhatkit_fast_api.git)
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv_pywhatkit
    source .venv_pywhatkit/bin/activate  # On Windows, use `.venv_pywhatkit\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: If a `requirements.txt` file is not available, you can install the necessary libraries manually:*

    ```bash
    pip install fastapi uvicorn pywhatkit
    ```

## How to Run the Application

To start the FastAPI server, run the following command in your terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be accessible at `http://localhost:8000`.

## API Endpoints

The following endpoints are available:

### Health Check

- **GET /**: Returns a welcome message and basic instructions.
- **GET /health**: Returns the health status of the API.

### Send WhatsApp Message

- **POST /send-whatsapp-text**: Sends a text message to the specified phone number.

  **Request Body:**

  ```json
  {
    "phone": "+911234567890",
    "message": "Hello from the API!"
  }
  ```

- **POST /send-whatsapp-img**: Sends an image to the specified phone number.

  **Request Body:**

  ```json
  {
    "phone": "+911234567890",
    "img_path": "path/to/your/image.png",
    "caption": "This is a cool image!"
  }
  ```

  *Note: The `img_path` should be the absolute or relative path to the image on the server where the API is running.*

## How It Works

This API uses the `pywhatkit` library, which automates sending messages through WhatsApp Web. When you make a request to one of the send endpoints, `pywhatkit` opens a new browser tab, navigates to WhatsApp Web, and sends the message.

**Important:**

- You need to be logged into WhatsApp Web in your default browser for this to work.
- The `wait_time` parameter in the code allows time for WhatsApp Web to load. You may need to adjust this value based on your internet speed.
- The browser tab will close automatically after the message is sent.

## Project Structure

```
.
├── main.py         # The main FastAPI application
├── requirements.txt # Project dependencies
├── .venv_pywhatkit/  # Virtual environment directory
└── README.md       # This file
```
