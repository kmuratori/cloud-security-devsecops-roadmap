from flask import Flask, jsonify, request, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path(__file__).with_name("tasks.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/tasks")
def list_tasks():
    with get_db() as db:
        rows = db.execute(
            "SELECT id, title, done, created_at FROM tasks ORDER BY id DESC"
        ).fetchall()
    return jsonify([dict(row) for row in rows])

@app.post("/api/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify(error="Task title is required."), 400
    if len(title) > 160:
        return jsonify(error="Task title must be 160 characters or fewer."), 400
    with get_db() as db:
        cursor = db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        row = db.execute(
            "SELECT id, title, done, created_at FROM tasks WHERE id = ?",
            (cursor.lastrowid,)
        ).fetchone()
    return jsonify(dict(row)), 201

@app.patch("/api/tasks/<int:task_id>")
def toggle_task(task_id):
    with get_db() as db:
        row = db.execute("SELECT done FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if row is None:
            return jsonify(error="Task not found."), 404
        new_done = 0 if row["done"] else 1
        db.execute("UPDATE tasks SET done = ? WHERE id = ?", (new_done, task_id))
        updated = db.execute(
            "SELECT id, title, done, created_at FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()
    return jsonify(dict(updated))

@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    with get_db() as db:
        cursor = db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            return jsonify(error="Task not found."), 404
    return "", 204

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
