"""
Main entry: start database, show login, then main menu and screens.
Run this file from the Employee_Attendance_System folder:
    python main.py
"""

import sys
from pathlib import Path

# Make sure project root is on Python path for imports
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import tkinter as tk
from tkinter import messagebox

from modules.attendance import AttendanceFrame
from modules.dashboard import DashboardFrame
from modules.employees import EmployeesFrame
from modules.login import LoginWindow
from modules.reports import ReportsFrame
from utils.db_connection import init_database


class MainApp:
    """
    Controls login, navigation bar, and which module frame is visible.
    """

    def __init__(self, root):
        self.root = root
        self.content_area = None

    def start(self):
        """
        Build database tables and open the login window.
        """
        try:
            init_database()
        except Exception as e:
            messagebox.showerror("Error", "Could not start database:\n" + str(e))
            self.root.destroy()
            return

        self.show_login()

    def show_login(self):
        """
        Clear window and show admin login.
        """
        self.root.title("Employee Attendance System - Login")
        self.root.geometry("420x300")
        self.root.configure(bg="#e8f4fc")
        for child in self.root.winfo_children():
            child.destroy()
        LoginWindow(self.root, self.open_main_menu)

    def clear_content(self):
        """
        Remove old module from the content area.
        """
        if self.content_area is None:
            return
        for child in self.content_area.winfo_children():
            child.destroy()

    def open_main_menu(self):
        """
        After successful login, show navigation and default dashboard.
        """
        for child in self.root.winfo_children():
            child.destroy()

        self.root.title("Employee Attendance System")
        self.root.geometry("920x620")
        self.root.configure(bg="#f5f5f5")

        nav_bar = tk.Frame(self.root, bg="#e8f4fc", pady=12)
        nav_bar.pack(fill=tk.X)

        tk.Button(
            nav_bar,
            text="Dashboard",
            command=self.show_dashboard,
            bg="#b8d4e8",
            width=12,
        ).pack(side=tk.LEFT, padx=6)

        tk.Button(
            nav_bar,
            text="Employees",
            command=self.show_employees,
            bg="#b8d4e8",
            width=12,
        ).pack(side=tk.LEFT, padx=6)

        tk.Button(
            nav_bar,
            text="Attendance",
            command=self.show_attendance,
            bg="#b8d4e8",
            width=12,
        ).pack(side=tk.LEFT, padx=6)

        tk.Button(
            nav_bar,
            text="Reports",
            command=self.show_reports,
            bg="#b8d4e8",
            width=12,
        ).pack(side=tk.LEFT, padx=6)

        tk.Button(
            nav_bar,
            text="Logout",
            command=self.logout,
            bg="#d0d0d0",
            width=10,
        ).pack(side=tk.RIGHT, padx=10)

        self.content_area = tk.Frame(self.root, bg="#ffffff")
        self.content_area.pack(fill=tk.BOTH, expand=True)
        self.show_dashboard()

    def show_dashboard(self):
        """
        Show dashboard counts.
        """
        self.clear_content()
        DashboardFrame(self.content_area)

    def show_employees(self):
        """
        Show employee management.
        """
        self.clear_content()
        EmployeesFrame(self.content_area)

    def show_attendance(self):
        """
        Show attendance marking.
        """
        self.clear_content()
        AttendanceFrame(self.content_area)

    def show_reports(self):
        """
        Show reports screen.
        """
        self.clear_content()
        ReportsFrame(self.content_area)

    def logout(self):
        """
        Return to login screen.
        """
        if messagebox.askyesno("Logout", "Do you want to logout?"):
            self.content_area = None
            self.show_login()


def main():
    root = tk.Tk()
    app = MainApp(root)
    app.start()
    root.mainloop()


if __name__ == "__main__":
    main()
