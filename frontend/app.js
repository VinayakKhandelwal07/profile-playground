const BASE_URL = "http://127.0.0.1:8000";

const nameEl = document.getElementById("name");
const emailEl = document.getElementById("email");
const educationEl = document.getElementById("education");
const githubEl = document.getElementById("github");
const linkedinEl = document.getElementById("linkedin");
const portfolioEl = document.getElementById("portfolio");

const projectsListEl = document.getElementById("projectsList");
const messageEl = document.getElementById("message");
const skillInput = document.getElementById("skillInput");
const searchBtn = document.getElementById("searchBtn");
const skillsListEl = document.getElementById("skillsList");

async function fetchProfile() {
  const res = await fetch(`${BASE_URL}/profile`);
  const d = await res.json();

  nameEl.textContent = d.name;
  emailEl.textContent = d.email;
  educationEl.textContent = d.education;
  githubEl.href = d.github;
  linkedinEl.href = d.linkedin;
  portfolioEl.href = d.portfolio;
}

function renderProjects(projects) {
  projectsListEl.innerHTML = "";
  messageEl.textContent = "";

  if (!projects.length) {
    messageEl.textContent = "No projects found.";
    return;
  }

  projects.forEach(p => {
    const card = document.createElement("div");
    card.className = "project-card";

    card.innerHTML = `
      <span class="id">Project #${p.id}</span>
      <h3>${p.title}</h3>
      <button class="expand-btn">+</button>
      <div class="project-details">
        <p>${p.description || "No description available."}</p>
        ${p.link ? `<a href="${p.link}" target="_blank">View Link ↗</a>` : ""}
      </div>
    `;

    const btn = card.querySelector(".expand-btn");
    const details = card.querySelector(".project-details");

    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const open = details.style.display === "block";
      details.style.display = open ? "none" : "block";
      btn.textContent = open ? "+" : "−";
    });

    projectsListEl.appendChild(card);
  });
}

async function fetchProjects(skill = "python") {
  const res = await fetch(`${BASE_URL}/projects?skill=${encodeURIComponent(skill)}`);
  const projects = await res.json();
  renderProjects(projects);
}

async function fetchSearch(query) {
  const res = await fetch(`${BASE_URL}/search?q=${encodeURIComponent(query)}`);
  const data = await res.json();
  renderProjects(data);
}

async function fetchTopSkills() {
  const res = await fetch(`${BASE_URL}/skills/top`);
  const skills = await res.json();

  skillsListEl.innerHTML = "";

  skills.forEach(s => {
    const span = document.createElement("span");
    span.className = "skill-badge";
    span.textContent = s.name;
    skillsListEl.appendChild(span);
  });
}

// Search instantly when typing
skillInput.addEventListener("input", () => {
  const q = skillInput.value.trim();
  if (!q) return fetchProjects("python");
  fetchSearch(q);
});

// Also search on button click
searchBtn.addEventListener("click", () => {
  const q = skillInput.value.trim();
  if (!q) return fetchProjects("python");
  fetchSearch(q);
});

(async function init() {
  await fetchProfile();
  await fetchTopSkills();
  await fetchProjects("python");
})();
