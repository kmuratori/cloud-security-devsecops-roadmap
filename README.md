# Task Board: Git / DevOps Lab

A small Flask + SQLite web app used as a practice target for **Git, CI/CD, DevSecOps and Cloud engineering**.

The app is intentionally simple. The goal of this repository is the workflow around it: version control, automation, security checks, packaging and deployment.

## Status

| Area | Status |
|---|---|
| Git fundamentals (branches, conflicts, `revert`) | Done |
| Docker (multi-stage, non-root, volume, Trivy scan run manually) | Done |
| CI with GitHub Actions (tests, image build, smoke test) | Done |
| Security scanners in CI (dependencies, secrets, SAST) | Planned |
| Cloud deployment | Planned |

## Tools

| Tool | Purpose |
|---|---|
| Git / GitHub | Version control, pull requests |
| Python 3.12 + Flask | Backend and REST API |
| SQLite | Local database |
| pytest | Automated tests |
| Docker | Containerization |
| GitHub Actions | Continuous integration |
| Trivy | Image vulnerability scan (manual for now) |

## Getting started

### Run with Docker

```bash
docker build -t taskboard .
docker run -d             \
  --name taskboard        \
  -v taskboard-data:/data \
  -p 5000:5000            \
  taskboard
```

Open `http://localhost:5000`.

The app stores its database in `/data` (hardcoded path), so the container needs a volume there. The image runs as a non-root user.

### Run the tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Tests use a temporary database and never touch `/data`.

## Continuous integration

`.github/workflows/ci.yml` runs on every pull request and on pushes to `master`:

1. `tests`: installs dependencies and runs `pytest`.
2. `docker-build` (only if `tests` passes): builds the image, then runs `scripts/smoke_test.sh`.

The smoke test starts the container, waits for the API (5 attempts), checks `GET /api/tasks`, and always removes the container.

```bash
./scripts/smoke_test.sh <image>
```

The Dockerfile starts with a `# syntax=` line so the `COPY --exclude` flag works on older Docker versions.

## Repository layout

| Path | Content |
|---|---|
| `app.py`, `templates/` | The application |
| `tests/` | pytest tests |
| `Dockerfile` | Multi-stage image |
| `scripts/` | Automation scripts |
| `.github/workflows/` | CI workflows |
| `labs/` | Docker practice demos |
| `notes/` | Personal learning notes |

## Roadmap

1. **Git fundamentals**: commits, branches, merges, conflicts, `revert`, tags.
2. **GitHub collaboration**: issues, pull requests, reviews, branch protection.
3. **Continuous integration**: tests and checks on every change.
4. **DevSecOps**: dependency, secret and static analysis scans; image scanning in CI; supply-chain basics.
5. **Containers and cloud**: image registry, test deployment, health checks, rollback, cleanup.

Items marked "Planned" above are goals, not features of the repository yet.

## Git workflow

1. Create a branch from `master`.
2. Make one focused change and run the checks locally.
3. Commit with a descriptive message (`feat:`, `docs:`, `ci:`, `test:`).
4. Push and open a pull request.
5. Wait for the checks to pass, then merge.

Undo pushed changes with `git revert`, not `reset` + force push.

---

**Focus:** Git -> CI/CD -> DevSecOps -> Cloud.
**Approach:** learn by implementing, testing, documenting and improving one step at a time.
