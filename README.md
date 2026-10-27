# Git / DevOps Lab - Task Board

A small web application used as a practice target for **Git, DevOps, DevSecOps, and Cloud engineering**.

The application is intentionally simple. The main goal of this repository is to practice the workflows surrounding software development: version control, collaboration, automation, security testing, packaging, and deployment.

## Goals

- Practice Git fundamentals using a real, multi-file project.
- Learn branching strategies, commits, merges, conflict resolution, and tags.
- Use GitHub issues, pull requests, code reviews, and branch protection.
- Introduce continuous integration and automated testing.
- Explore DevSecOps practices by integrating security checks into development workflows.
- Learn the fundamentals of software packaging, containers, and cloud deployment.
- Document experiments, technical decisions, errors, and lessons learned.
- Build a practical portfolio demonstrating continuous learning in DevOps, DevSecOps, and Cloud.

## Tools

| Tool | Purpose |
|---|---|
| Git | Version control, branching, merging, and history |
| GitHub | Remote repository, issues, pull requests, reviews, and Wiki |
| Python + Flask | Backend application and REST API |
| SQLite | Lightweight local database |
| HTML, CSS, JavaScript | Frontend |
| Python `venv` + `pip` | Environment isolation and dependency management |
| GitHub Actions | Continuous integration and automation - planned |
| Security scanners | Dependency analysis, secret detection, and static analysis - planned |
| Docker | Containerization - planned |
| Cloud platform | Deployment and infrastructure experiments - planned |

Tools will be introduced progressively according to the learning objectives of each stage.

## Getting Started

### Prerequisites

- Git
- Python 3.10 or newer
- A GitHub account for remote repository and collaboration exercises

### Run the application

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

The application uses SQLite for local persistence. Its database file is generated locally and excluded from version control.

## Lab Roadmap

### 1. Git Fundamentals

**Objective:** Understand how Git tracks changes and how developers collaborate.

- Initialize and configure a repository.
- Stage and commit changes.
- Inspect history with `git log`.
- Compare changes using `git diff` and `git show`.
- Create, switch, merge, and delete branches.
- Resolve merge conflicts.
- Undo changes safely with `git revert`.
- Create tags and understand releases.
- Practice working with a remote repository.

### 2. GitHub Collaboration

**Objective:** Adopt a structured development workflow.

- Create issues with clear goals and acceptance criteria.
- Use feature branches for individual changes.
- Open pull requests.
- Review code before merging.
- Protect the main branch.
- Require reviews and successful automated checks.
- Use descriptive commit messages and maintain a readable history.

### 3. Continuous Integration

**Objective:** Automate checks whenever code changes.

- Create a GitHub Actions workflow.
- Run automated tests on pull requests.
- Check syntax, formatting, and code quality.
- Understand workflow triggers, jobs, steps, and artifacts.
- Investigate failed runs and fix the underlying problems.
- Prevent changes from being merged when required checks fail.

### 4. DevSecOps

**Objective:** Integrate security into the software development lifecycle.

- Scan dependencies for known vulnerabilities.
- Detect accidentally committed secrets.
- Introduce static application security testing (SAST).
- Review and remediate security findings.
- Scan container images for vulnerabilities.
- Understand software supply-chain security.
- Integrate appropriate security checks into CI pipelines.

### 5. Containers and Cloud

**Objective:** Progress from a local application to a repeatable deployment workflow.

- Containerize the application with Docker.
- Manage configuration through environment variables.
- Understand image building, tagging, and registry workflows.
- Introduce cloud deployment in a test environment.
- Explore deployment automation and environment separation.
- Document logs, health checks, rollback procedures, and resource cleanup.

These stages form a roadmap; they are not claims that the corresponding infrastructure or automation is already implemented.

## Suggested Git Workflow

Use this cycle for each exercise:

1. Define the objective and acceptance criteria.
2. Create an issue.
3. Create a branch from `main`.
4. Implement one focused change.
5. Run relevant checks locally.
6. Review the diff.
7. Commit with a descriptive message.
8. Push the branch and open a pull request.
9. Review the changes and automated checks.
10. Merge and update the local repository.

Example:

```bash
git switch main
git pull --ff-only
git switch -c chore/add-basic-tests

# Implement the change
git status
git diff
git add .
git commit -m "test: add basic API tests"
git push -u origin chore/add-basic-tests
```

Complete the workflow by opening a pull request on GitHub.

## Suggested Exercises

- Create a feature branch and merge it into `main`.
- Produce and resolve a merge conflict.
- Compare `git merge` and `git rebase`.
- Undo a commit using `git revert`.
- Create a version tag.
- Configure branch protection and required checks.
- Add a CI workflow and investigate a failing run.
- Introduce a dependency scanner and document its findings.
- Add secret detection and learn how to respond to an exposed credential.
- Containerize the application and scan the resulting image.
- Build a deployment workflow for a test environment.

Use a disposable branch or test repository when practicing destructive Git operations.

## Repository Scope

The initial project provides a minimal Flask and SQLite application as a target for development and automation exercises.

The starter repository does not yet include a configured CI/CD pipeline, security scanners, container image, or cloud deployment. These components will be introduced incrementally as part of the lab.

The application is the practice target; the primary learning objective is the engineering workflow around it.

## Documentation and Resources

This README provides the project overview, goals, and learning roadmap.

The GitHub Wiki will contain more detailed documentation as the project grows, including:

- Useful Git commands and recovery procedures.
- Setup instructions and troubleshooting.
- GitHub Actions and CI/CD workflow explanations.
- DevSecOps tools, configurations, and findings.
- Docker and cloud deployment notes.
- References, tutorials, and personal learning notes.

Additional resources and commands will be added progressively as each topic is explored.

---

 **Project focus:** Git -> Automation -> DevSecOps -> Cloud.

**Approach:** Learn by implementing, testing, reviewing, documenting, and improving one step at a time.
