# Bookstore Admin

This project is a Back-Office Bookstore Admin for small–medium bookstores in Thailand, focused on fast selling, accurate inventory, and simple print workflows with text-only documents/labels.

## Architecture

- **Backend:** FastAPI (Python) + Firebase Realtime Database
- **Frontend:** React + Vite + Tailwind CSS (Dark Mode)
- **Authentication:** Firebase Authentication
- **Build/Run:** Docker + docker-compose

## Setup and Usage

### Prerequisites

- Docker and docker-compose
- A Firebase project with Realtime Database and Authentication enabled

### 1. Configure Firebase

1.  **Create a Firebase Project:** Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project.
2.  **Enable Realtime Database:** Inside your project, go to "Build" > "Realtime Database" and create a new database.
3.  **Enable Authentication:** Go to "Authentication" and enable it. Choose the "Email/Password" sign-in method.
4.  **Get Service Account Key:**
    *   In your Firebase project, click the gear icon next to "Project Overview" and select **Project settings**.
    *   Go to the **Service accounts** tab.
    *   Click **"Generate new private key"**.
    *   A JSON file will be downloaded. Rename this file to `firebase-credentials.json` and place it in the `backend` directory.

### 2. Configure Frontend

1.  Go to your Firebase project settings and in the "General" tab, scroll down to "Your apps".
2.  Click the web icon (`</>`) to create a new web app.
3.  Copy the `firebaseConfig` object and paste it into `frontend/src/firebase.js`.

### 3. Run the Application

1.  Open a terminal and navigate to the root of the project.
2.  Run the following command to build and start the services:

    ```bash
    docker-compose up -d
    ```

3.  The application will be available at the following URLs:
    *   **Frontend:** `http://localhost:5173`
    *   **Backend API:** `http://localhost:8000/docs`

### 4. Seed the Database

To populate the database with some initial sample data, run the following command:

```bash
docker-compose exec backend python seed.py
```

This will create a few sample books and authors in your Firebase Realtime Database.
