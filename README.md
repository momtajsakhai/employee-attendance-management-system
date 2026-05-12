# Employee Attendance Management System

A small desktop application to manage employees and daily attendance using Python, SQLite, and Tkinter. The code is written in a simple style so you can read it line by line and explain it in interviews.

## Project overview

The app starts with an **admin login**. After login you get a **dashboard** with employee counts, screens to **add/update/delete/search employees**, **mark attendance** for today (with duplicate protection), and **reports** by date or search.

The SQLite database file is created automatically the first time you run the app. It lives in the `database` folder as `attendance.db`.

## Features

- Admin login with fixed username and password (see `modules/login.py`)
- Dashboard: total employees, present today, absent / not marked today
- Employee management: add, update, delete, search, table list
- Attendance: mark Present or Absent for today; one record per employee per day
- Reports: daily report by date; search by employee name or date
- Sample employees inserted on first run
- Basic validation and popup messages for success and errors

## Technologies used

- Python 3
- SQLite3 (file database)
- Tkinter (GUI)

## Installation steps

1. Install [Python 3](https://www.python.org/downloads/) (3.8 or newer). On Windows, enable **"Add python.exe to PATH"** during setup.
2. No extra packages are required; Tkinter and sqlite3 are part of the standard library.
3. Download or copy the whole `Employee_Attendance_System` folder to your computer.

## How to run the project

1. Open a terminal (Command Prompt or PowerShell).
2. Go to the project folder:

   ```bash
   cd path\to\Employee_Attendance_System
   ```

3. Start the application:

   ```bash
   python main.py
   ```

4. Login with:

   - **Username:** `admin`
   - **Password:** `admin123`

## Folder structure

```
Employee_Attendance_System/
├── main.py
├── database/
│   └── attendance.db    (created when you first run the app)
├── modules/
│   ├── login.py
│   ├── dashboard.py
│   ├── employees.py
│   ├── attendance.py
│   └── reports.py
├── utils/
│   └── db_connection.py
├── requirements.txt
└── README.md
```

## Notes for beginners

- Change admin credentials only inside `modules/login.py` for learning demos.
- The database is recreated as an empty file in `database/`; deleting `attendance.db` resets data (sample employees will load again if the employees table is empty).
- Attendance **date** is always **today’s date** on the Attendance screen, stored as `YYYY-MM-DD`.
