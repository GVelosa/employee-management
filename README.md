# Staff Manager

A Human Resources (HR) management system designed to streamline employee registration and role organization. This project focuses on integrating relational databases with a modern UI to manage organizational data efficiently.

> [!IMPORTANT]
> The primary goal of this project is to practice building a full application using **Flet** for the interface and **SQLite** for structured data persistence, focusing on clean data modeling and interaction between entities.

---

## Features

* **User Authentication (Basic):** Platform user registration with validation and database persistence.
* **Employee Management:** Create and manage employees with relationships to departments and job roles.
* **Interactive Registration:** A clean Flet-based form for registering employees and related entities.
* **Relational Data Modeling:** Employees are linked to departments and job roles using foreign keys, ensuring consistency and scalability.
* **Data Organization:** Structured management of personnel records following real-world HR relationships (employee → manager → department).
* **Database Queries:** Retrieve employee-related data such as job title, department, and manager relationships.

---

## Technologies Used

| Technology                        | Description                                                                    |
| :-------------------------------- | :----------------------------------------------------------------------------- |
| [Python](https://www.python.org/) | Core language used for backend logic and database operations.                  |
| [Flet](https://flet.dev/)         | UI framework used to build a responsive graphical interface.                   |
| SQLite                            | Lightweight relational database used for persistent storage and data modeling. |

---

## Database Design

The project uses a **normalized relational database structure** to ensure data consistency and scalability.

### Main Tables:

* **users:** Stores platform authentication data
* **employees:** Stores employee information and hierarchical relationships
* **departments:** Defines organizational units
* **job_titles:** Standardizes roles across the system

### Key Concepts Applied:

* **Normalization:** Avoids redundancy by separating entities into dedicated tables
* **Foreign Keys:** Ensures referential integrity between employees, departments, and roles
* **Self-relationship:** Employees can reference other employees as managers (`manager_id`)
* **Data Consistency:** IDs are used instead of raw text to prevent duplication and typos

---

## What I Learned

By evolving from simple scripts into a structured application, this project helped reinforce:

### 🗄️ Database & Backend Concepts

* **Relational Modeling:** Designing structured relationships between entities like employees, departments, and roles.
* **Data Integrity:** Using constraints (`UNIQUE`, `CHECK`, `FOREIGN KEY`) to ensure reliable data.
* **Separation of Concerns:** Keeping UI and database operations organized and maintainable.
* **Scalability Thinking:** Structuring the database in a way that allows future expansion without major refactoring.

### 🎨 UI Architecture

* **Componentization in Flet:** Breaking down the UI into reusable components for maintainability and clarity.

---

## Future Improvements

* Implement password hashing (security enhancement)
* Create dashboards with employee analytics
* Introduce performance review history tracking
* Improve validation and error handling in UI

---