const form = document.querySelector("#task-form");
const input = document.querySelector("#task-title");
const list = document.querySelector("#task-list");
const emptyState = document.querySelector("#empty-state");
const count = document.querySelector("#task-count");
const notice = document.querySelector("#notice");

function showNotice(message = "", isError = false) {
  notice.textContent = message;
  notice.classList.toggle("error", isError);
}

async function api(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.error || "Something went wrong.");
  }
  return response.status === 204 ? null : response.json();
}

function renderTasks(tasks) {
  list.replaceChildren();
  const completed = tasks.filter(task => task.done).length;
  count.textContent = `${tasks.length} task${tasks.length === 1 ? "" : "s"} · ${completed} done`;
  emptyState.hidden = tasks.length > 0;

  for (const task of tasks) {
    const item = document.createElement("li");
    item.className = `task${task.done ? " completed" : ""}`;

    const toggle = document.createElement("button");
    toggle.className = "check";
    toggle.type = "button";
    toggle.setAttribute("aria-label", task.done ? "Mark as not done" : "Mark as done");
    toggle.textContent = task.done ? "✓" : "";
    toggle.addEventListener("click", async () => {
      try {
        await api(`/api/tasks/${task.id}`, { method: "PATCH" });
        await loadTasks();
      } catch (error) { showNotice(error.message, true); }
    });

    const title = document.createElement("span");
    title.className = "task-title";
    title.textContent = task.title;

    const remove = document.createElement("button");
    remove.className = "delete";
    remove.type = "button";
    remove.textContent = "Delete";
    remove.addEventListener("click", async () => {
      try {
        await api(`/api/tasks/${task.id}`, { method: "DELETE" });
        showNotice("Task deleted.");
        await loadTasks();
      } catch (error) { showNotice(error.message, true); }
    });

    item.append(toggle, title, remove);
    list.append(item);
  }
}

async function loadTasks() {
  try {
    renderTasks(await api("/api/tasks"));
  } catch (error) {
    showNotice(`Could not load tasks: ${error.message}`, true);
  }
}

form.addEventListener("submit", async event => {
  event.preventDefault();
  const title = input.value.trim();
  if (!title) return;
  try {
    await api("/api/tasks", {
      method: "POST",
      body: JSON.stringify({ title }),
    });
    input.value = "";
    showNotice("Task added.");
    await loadTasks();
    input.focus();
  } catch (error) {
    showNotice(error.message, true);
  }
});

loadTasks();
