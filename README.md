# Task Management Web App

A full-stack task management application with a **FastAPI** backend and a **React** frontend.  
Features include user authentication, CRUD operations for tasks, and a responsive UI.  

---

## 🚀 Tech Stack
- **Backend:** FastAPI, PostgreSQL, Alembic (migrations), Postman (API testing)
- **Frontend:** React
- **Other Tools:** Git, Docker (optional)

---

## 📂 Project Structure
```
task-manager/
│── backend/        # FastAPI backend
│   ├── app/        # Application code
│   ├── alembic/    # Database migrations
│   └── requirements.txt
│
│── frontend/       # React frontend
│   ├── src/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

---

### 2. Backend Setup (FastAPI + PostgreSQL)
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database in `.env` (example):
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/taskdb
   ```

5. Run Alembic migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
   Backend runs on: `http://127.0.0.1:8000`

---

### 3. Frontend Setup (React)
1. Navigate to the frontend folder:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```
   Frontend runs on: `http://localhost:3000`

---

## 🔗 API Documentation
Once the backend is running, interactive API docs are available at:  
- Swagger UI → `http://127.0.0.1:8000/docs`  
- ReDoc → `http://127.0.0.1:8000/redoc`

---

## 📝 Features
- User authentication (sign up, login)
- Task CRUD (create, read, update, delete)
- Responsive React frontend
- PostgreSQL database with migrations

---

## 🤝 Contributing
Feel free to fork this repo and submit pull requests.  

---

## 📜 License
This project is licensed under the MIT License.
