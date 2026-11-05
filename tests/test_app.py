import app

def test_create_and_list_tasks(tmp_path, monkeypatch):
  # Redirect database to a temporary directory
  db_path = tmp_path / "tasks.db"
  monkeypatch.setattr(app, "DB_PATH", db_path)

  # Initialize database
  app.init_db()

  client = app.app.test_client()

  # Create a task
  response = client.post("/api/tasks", json={
    "title": "Learn pytest"
  })

  assert response.status_code == 201

  # List tasks
  response = client.get("/api/tasks")

  assert response.status_code == 201

  tasks = response.get_json()
  assert any(task["title"] == "Learn pytest" for task in tasks)
