import pytest
from datetime import datetime, timedelta
from analytics import *

class DummyHabit:
    def __init__(self, habit_id, name, periodicity):
        self.habit_id = habit_id
        self.name = name
        self.periodicity = periodicity

class DummyTracker:
    def __init__(self, completions_map):
        self.completions_map = completions_map
    def get_habit_completions(self, habit_id):
        return self.completions_map.get(habit_id, [])

def test_longest_streak_daily():
    today = datetime.now()
    completions = [today - timedelta(days=i) for i in range(3)]
    assert get_longest_streak(completions, "daily") == 3

def test_longest_streak_weekly():
    today = datetime.now()
    completions = [today - timedelta(weeks=i) for i in range(4)]
    assert get_longest_streak(completions, "weekly") == 4

def test_longest_streak_monthly():
    completions = [
        datetime(2025, 1, 10),
        datetime(2025, 2, 10),
        datetime(2025, 3, 10),
    ]
    assert get_longest_streak(completions, "monthly") == 3

def test_longest_streak_empty():
    assert get_longest_streak([], "daily") == 0

def test_current_streak_daily_active():
    today = datetime.now()
    completions = [today - timedelta(days=i) for i in range(3)]
    assert get_current_streak(completions, "daily") == 3

def test_current_streak_daily_broken():
    today = datetime.now()
    completions = [today - timedelta(days=0), today - timedelta(days=2)]
    assert get_current_streak(completions, "daily") == 0

def test_current_streak_weekly_active():
    today = datetime.now()
    completions = [today - timedelta(weeks=i) for i in range(2)]
    assert get_current_streak(completions, "weekly") == 2

def test_current_streak_monthly_inactive():
    today = datetime.now()
    old_completion = today - timedelta(days=60)
    assert get_current_streak([old_completion], "monthly") == 0

def test_all_longest_streaks_and_global():
    today = datetime.now()
    habit1 = DummyHabit(1, "Exercise", "daily")
    habit2 = DummyHabit(2, "Read", "weekly")
    habits = [habit1, habit2]

    completions_map = {
        1: [today - timedelta(days=i) for i in range(2)],   # streak of 2
        2: [today - timedelta(weeks=i) for i in range(3)],  # streak of 3
    }
    tracker = DummyTracker(completions_map)

    streaks = get_all_longest_streaks(habits, tracker)
    assert streaks["Exercise"] == 2
    assert streaks["Read"] == 3

    name, streak = get_global_longest_streak(habits, tracker)
    assert name == "Read"
    assert streak == 3
