# Habit Tracker with Analytics

A lightweight Python-based **Habit Tracking Application** with streak analytics.  
Users can create, edit, and delete habits, and track progress through daily, weekly, and monthly streak calculations.  

This project was built as part of an applied learning exercise in habit-tracking systems and analytics.

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

## Installation

Clone the repository from GitHub:

```bash
git clone https://github.com/siza94/habit_tracker_app.git
cd habit_tracker_app
```

Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Linux / Mac
venv\Scripts\activate      # On Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Follow the interactive menu prompts to:

Add a new habit

Edit or delete an existing habit

View habit streaks and analytics

Navigate between views or return to the main menu

## Running Tests

This project uses unittest for test coverage.
To run all tests:

```bash
python -m unittest discover tests
```

Developed by Sithsaba Zantsi
