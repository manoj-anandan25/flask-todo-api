## Flask To-Do List API  
durga mookambike padmavathi mariammma sharadamba bhagavathi
A simple and clean RESTful API built using Flask and SQLAlchemy to manage a To-Do list. It supports creating, reading, updating, and deleting tasks using SQLite as the backend database.

---

 Tech Stack

- Python
- Flask
- SQLAlchemy (ORM)
- SQLite (Database)
  
---

 Features

- View all to-do items
- View a specific to-do by ID
- Add a new to-do
- Update a to-do (full update via `PUT`, partial via `PATCH`)
- Delete a to-do

---

 Project Structure

```

flask-todo-api/
├── app.py
├── data.db (auto-created after running)
└── README.md

````

---

 Getting Started

 1. Clone the repository
```bash
git clone https://github.com/your-username/flask-todo-api.git
cd flask-todo-api
````

 2. Install dependencies

```bash
pip install Flask Flask-SQLAlchemy
```

 3. Run the application

```bash
python app.py
```

 4. Open browser

```
http://127.0.0.1:5000/
```

---

API Endpoints

Base Route

```
GET /
→ "OM NAMO MOOKAMBIKE"
```

 Get all To-Dos

```
GET /todos
```

 Get a To-Do by ID

```
GET /todos/<id>
```

Create a To-Do

```
POST /todos
Body: {
  "task": "Buy groceries",
  "done": false
}
```

 Delete a To-Do

```
DELETE /todos/<id>
```

 Update (Full) a To-Do

```
PUT /todos/<id>
Body: {
  "task": "Clean room",
  "done": true
}
```

 Update (Partial) a To-Do

```
PATCH /todos/<id>
Body: {
  "task": "Go jogging"
}
```

---

 Example To-Do JSON

```json
{
  "id": 1,
  "task": "Study Flask",
  "done": false
}
```



