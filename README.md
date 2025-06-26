# 🛠️ SCPMS - Smart Console-Based Personal Management System

![Python](https://img.shields.io/badge/Language-Python-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modular console-based Python application designed for **personal productivity and data management**, featuring multiple tools like registration/login system, personal diary, contact book, to-do list, expense tracker, and utility tools.

---

---

## 1. User Registration & Login System

- 🔸 Register new users with username and password
- 🔸 Secure login with authentication
- 🔸 User data stored in text file
- 🔸 Ensures only registered users access their personal modules

---

## 2. Personal Diary

- 🗓️ Write, view, edit, and delete daily notes
- 📁 Notes stored using file handling with timestamps
- ✍️ Simple string-based entry and search

---

## 3. Contact Book

- 👤 Store contacts with Name, Phone, Email, and Address
- 🔎 Search, edit, delete, or view contacts
- 💾 Data stored in structured format CSV
- 🛠️ Uses Python lists and dictionaries

---

## 4. To-Do List Manager

- 📝 Add tasks with priority
- 📌 View pending tasks, mark completed, or delete
- 💾 Task persistence via file handling

---

## 5. Expense Tracker

- 💸 Record daily expenses with date, amount, and description
- 📊 View total or monthly/daily expense reports
- 📆 Uses `datetime` for date handling
- 💾 File storage for persistence

---

##  6. Utility Tools Section

| Tool                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 🧮 Calculator             | Perform basic arithmetic: +, −, ×, ÷                                        |
| 📏 Unit Converter         | Convert between Length (m/ft), Weight (kg/lb), Temperature (°C/°F)         |
| 🔐 Password Generator     | Generates secure random passwords using Python's `random` module            |

---

## 📁 Project Structure

SCPMS/
├── Contact Book/
│   └── contacts.py
├── data/
├── Expense Tracker/
│   └── expense_tracker.py
├── Personal Diary/
│   └── diary.py
├── to-do-list-manager/
│   └── tasks.py
├── User Registration & Authentication/
│   └── user_auth.py
└── Utility Tools Section/
    ├── calculator.py
    ├── Random_Password_Generator.py
    └── unit_converter.py



