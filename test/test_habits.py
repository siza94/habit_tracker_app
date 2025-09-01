import pytest
from habit_tracker import HabitTracker

def test_create_habit():
    tracker = HabitTracker()
    tracker.create_habit("Exercise", "daily")
    habits = tracker.get_all_habits()
    assert any(h.name == "Exercise" for h in habits)

def test_get_habits_by_periodicity():
    tracker = HabitTracker()
    tracker.create_habit("Read", "weekly")
    tracker.create_habit("Run", "daily")
    weekly = tracker.get_habits_by_periodicity("weekly")
    assert all(h.periodicity == "weekly" for h in weekly)

def test_complete_habit_and_completions():
    tracker = HabitTracker()
    tracker.create_habit("Meditate", "daily")
    habit = tracker.get_all_habits()[0]
    tracker.complete_habit(habit.habit_id)
    completions = tracker.get_habit_completions(habit.habit_id)
    assert len(completions) > 0

def test_longest_streaks():
    tracker = HabitTracker()
    tracker.create_habit("Workout", "daily")
    habit = tracker.get_all_habits()[0]
    tracker.complete_habit(habit.habit_id)
    name, streak = tracker.get_global_longest_streak()
    assert streak >= 0
    streak_for_habit = tracker.get_longest_streak_for_habit(habit.habit_id)
    assert streak_for_habit >= 0
