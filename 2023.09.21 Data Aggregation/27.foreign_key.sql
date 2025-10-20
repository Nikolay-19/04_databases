CREATE TABLE employees_projects (
    id INTEGER PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    project_id INTEGER REFERENCES projects
    )
