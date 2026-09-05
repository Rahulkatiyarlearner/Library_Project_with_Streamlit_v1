import markdown

readme_content = """# 📚 Library Management System (Streamlit & Python SQLite App)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://libraryabc.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, full-stack **Library Management System web application** built with **Python**, **Streamlit**, and **SQLite**. Designed with a clean 3-tier architecture, this application streamlines library operations including book cataloging, member registration, ISBN validation, book issuing, return workflows, and dynamic fine calculation.

🚀 **Live Demo:** [Try the ABC Library App Here](https://libraryabc.streamlit.app/)

---

## 📌 Key Features

* **🔐 Admin Authentication:** Secure session-state login management for library administrators.
* **👤 Member Management:** Register members with automated 8-digit unique ID generation and input validation.
* **📚 Book Catalog & ISBN Validation:** Add catalog items with 13-digit ISBN regex formatting and serial tracking.
* **🔄 Issue & Return Workflow:** Track active book loans, process returns, and search library inventory in real-time.
* **💰 Automatic Fine Calculation:** Auto-compute overdue penalties beyond the standard 14-day borrowing period.
* **📊 Interactive Dashboard:** View real-time library records using Pandas DataFrames and Streamlit UI components.

---

## 🏗️ Project Architecture

```text
ABC Library/
│
├── data/                      # Data Access Layer
│   ├── database_manager.py    # SQLite connection manager with auto-rollback context manager
│   ├── library_database.py     # SQL queries for library inventory & issue transactions
│   └── member_database.py      # SQL queries for library member accounts
│
├── Services/                  # Business Logic Layer
│   ├── library_services.py    # Book validation rules, fine logic, and DataFrame processing
│   └── member_services.py     # Member registration and verification logic
│
├── UI/                        # Presentation Layer
│   ├── login_screen.py        # Streamlit login interface & session handling
│   └── main_screen.py         # Main dashboard, sidebar navigation, and forms
│
└── main.py                    # Application entry point
