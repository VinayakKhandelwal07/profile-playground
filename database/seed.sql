-- seed.sql

-- PROFILE
INSERT INTO profile (name, email, education, github, linkedin, portfolio)
VALUES (
  'Vinayak Khandelwal',
  'khandelwalvinayak84@gamil.com',
  'B.Tech Computer Science & Engineering (AI) - Poornima Institute of Engineering and Technology, Jaipur (2022-2026)',
  'https://github.com/VinayakKhandelwal07',
  'https://www.linkedin.com/in/vinayak-khandelwal-b3216425a/',
  'https://vinayak.dev'
);

-- SKILLS
INSERT INTO skills (name, count) VALUES
('Python', 5),
('Java', 2),
('Django', 4),
('FastAPI', 3),
('Flask', 3),
('RESTful APIs', 3),
('HTML', 3),
('CSS', 3),
('JavaScript', 3),
('PostgreSQL', 3),
('SQLite', 2),
('SQL', 2),
('GitHub', 2),
('Render', 2),
('Jupyter Notebook', 1),
('Google Colab', 1),
('Streamlit', 1),
('Excel', 1);

-- PROJECTS
INSERT INTO projects (title, description, link) VALUES
('StockFlow – Multi-Tenant Staff & Inventory Management System',
 'Built a scalable multi-tenant Django platform with isolated company data, role-based access, secure inventory workflows, request approvals, real-time stock updates, audit logging, and responsive dashboards.',
 'https://github.com/VinayakKhandelwal07/stockflow'),

('Shree Thaal – Full-Stack Ordering App',
 'Developed and deployed a full-stack ordering app using FastAPI and PostgreSQL. Includes customer ordering interface, admin panel for managing orders/products/customers, and real-time top products dashboard.',
 'https://github.com/VinayakKhandelwal07/shree-thaal'),

('Movie Recommendation System (ML + Web App)',
 'Built a content-based movie recommender using cosine similarity on 5000+ titles with TMDB integration. Includes user auth, watchlist, theme toggle UI, and deployed on Render.',
 'https://github.com/VinayakKhandelwal07/movie-recommender');

-- PROJECT SKILLS MAPPING
INSERT INTO project_skills VALUES
(1, 1),
(1, 3),
(1, 7),
(1, 9),
(1, 11),

(2, 1),
(2, 4),
(2, 9),
(2, 10),
(2, 12),

(3, 1),
(3, 5),
(3, 6),
(3, 8),
(3, 14);
