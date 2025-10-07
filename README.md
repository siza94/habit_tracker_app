# Habit Tracker with Analytics

A lightweight Python-based **Habit Tracking Application** that makes it easier to keep track of your habits with streak analytics
to see how much progress you have made with each habit.

The Habit Tracker is a command-line application designed to help users build, track, and analyze their habits. Whether you want to establish a daily workout routine, read weekly, or break bad habits, this app provides a structured way to monitor progress and stay accountable.

Users can create, edit, and delete habits, and track progress through daily, weekly, and monthly streak calculations that will keep you
more informed about the habits you are forming.  

This project was built as part of a IU International University of Applied AScience learning project in applying fundamental principles
when building a Python project using object orientated principles.

---

## Features

- Create, edit, and delete habits
- Analytics module:
  * Daily streaks
  * Weekly streaks
  * Monthly streaks
- Menu-based navigation system
  * View specific habit stats
  * Stay on the same view or return to the main menu
- Unit test coverage for habit management and analytics

---

## Tools 

Python 3.7+ - Core programming language

Matplotlib - Data visualization and graph generation

JSON - Lightweight data storage

pytest - Testing framework

Object-Oriented Design - Modular, maintainable code structure

## Installation

Clone the repository from GitHub:

```bash
git clone https://github.com/siza94/habit_tracker_app.git
cd habit_tracker_app
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Main Menu Options

1. Create a New Habit
Enter habit name and select periodicity (daily/weekly/monthly)

Example: "Morning Meditation" with "daily" periodicity

2. Complete a Habit
View all habits and mark them as completed

Tracks completion timestamp automatically

3. View All Habits
Display all tracked habits with their IDs and periodicities

4. Habit Analytics
4.1 View all habits

4.2 Filter habits by periodicity

4.3 View global longest streak across all habits

4.4 View longest streak for a specific habit

5. Generate Progress Graph
Create visual progress charts for any habit

Graphs are saved in the graphs/ directory as PNG files

6. Exit
Safely exit the application

## Running Tests

# Run all tests
```bash
pytest
```

# Run with verbose output
```bash
pytest -v
```

# Run specific test files
```bash
pytest tests/test_habits.py
pytest tests/test_analytics.py
```

Developed by Sithsaba Zantsi
