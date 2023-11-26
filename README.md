# Voice Translation Web Application

## Overview

Welcome to the Voice Translation Web Application! This project enables real-time voice translation during video calls, allowing users to communicate in different languages seamlessly.

The project consists of a Django backend providing API services and a React frontend for the user interface. The backend and frontend are organized into clear directories, and the project utilizes Vite for fast development and efficient builds.

## Features

- **Real-time Communication:** Video calls with instant voice translation.
- **User Authentication:** Secure user authentication using Django's built-in system.
- **Translation Services:** Integration with external services for speech recognition and translation.
- **WebSocket Support:** Real-time communication between users for voice translation.
- **Responsive UI:** A user-friendly interface accessible on different devices.

## Project Structure

```plaintext
voice_translation_web_app/
│
├── backend/
│   ├── voice_translation_api/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── migrations/
│   │   ├── translation/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── manage.py
│   │   └── requirements.txt
│   │
│   └── ...
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Home.jsx
│   │   │   ├── VideoCall.jsx
│   │   │   └── ...
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── ...
│   │   ├── services/
│   │   │   ├── ApiService.js
│   │   │   └── WebSocketService.js
│   │   ├── App.jsx
│   │   └── main.js
│   │
│   └── ...
│
├── ai_ml/
│   └── ...
│
├── media/
│   └── ...
│
├── static/
│   └── ...
│
├── templates/
│   └── index.html
│
├── .env
├── .gitignore
├── package.json
├── README.md
├── Dockerfile
└── ...
Setup Instructions
Backend:
Navigate to the backend directory.
Create a virtual environment: python -m venv venv.
Activate the virtual environment:
On Windows: .\venv\Scripts\activate.
On Unix or MacOS: source venv/bin/activate.
Install dependencies: pip install -r requirements.txt.
Run migrations: python manage.py migrate.
Start the Django development server: python manage.py runserver.
Frontend:
Navigate to the frontend directory.
Install dependencies: npm install.
Run the Vite development server: npm run dev.
AI/ML Models (Optional):
Place AI/ML models in the ai_ml directory.
Media and Static Files:
Configure settings in Django to handle media and static files.
Docker (Optional):
Create a Dockerfile and build the Docker image.
Contributions
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

License
This project is licensed under the MIT License.
