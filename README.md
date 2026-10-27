# Git Demo — Task Board

A small CRUD web app for practicing Git. It uses **Python + Flask** for the API,
**SQLite** for persistence, and vanilla **HTML/CSS/JavaScript** for the UI.

## Features

- Add a task
- Mark a task as done / not done
- Delete a task
- Store tasks in SQLite between restarts
- Basic input validation and error messages

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

The SQLite database (`tasks.db`) is created automatically and intentionally ignored by Git.

## Suggested Git demo

Use these as demo checkpoints when teaching commits, branches, merges, and conflict resolution.
Start with the whole app as the initial commit, then make each change on its own branch.

```bash
git init
git add .
git commit -m "feat: create task board MVP"

git switch -c feature-task-priority
# Add a priority field to the database/API/UI.
git add .
git commit -m "feat: add task priorities"

git switch main
git switch -c feature-filter-tasks
# Add All / Active / Completed filters in the UI.
git add .
git commit -m "feat: filter tasks by status"

git switch main
git merge feature-task-priority
git merge feature-filter-tasks
```

For a merge-conflict demo, edit the same line in `static/app.js` on two branches,
commit both changes, then merge one branch into the other.

## Project structure

```text
git-demo-app/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── app.js
│   └── style.css
├── .gitignore
└── README.md
```

## API

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/tasks` | List tasks |
| POST | `/api/tasks` | Create a task (`{"title":"..."}`) |
| PATCH | `/api/tasks/<id>` | Toggle done status |
| DELETE | `/api/tasks/<id>` | Delete a task |
