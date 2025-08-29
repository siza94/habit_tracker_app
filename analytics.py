from datetime import datetime, timedelta


def get_longest_streak(completions, periodicity):
    """Calculate the longest streak for a habit.

    Args:
        completions: List of datetime objects
        periodicity: 'daily', 'weekly', or 'monthly'
    """
    if not completions:
        return 0

    completions_sorted = sorted(completions)
    streaks = []
    current_streak = 1

    for i in range(1, len(completions_sorted)):
        prev = completions_sorted[i - 1]
        curr = completions_sorted[i]

        if periodicity == 'daily':
            expected = prev + timedelta(days=1)
            is_streak = curr.date() == expected.date()
        elif periodicity == 'weekly':
            expected = prev + timedelta(weeks=1)
            is_streak = curr.date() == expected.date()
        elif periodicity == 'monthly':
            # Check if same day next month (approximate)
            is_streak = (
                    curr.day == prev.day and
                    (curr.year == prev.year and curr.month == prev.month + 1) or
                    (curr.year == prev.year + 1 and curr.month == 1 and prev.month == 12)
            )
        else:
            raise ValueError("Periodicity must be 'daily', 'weekly', or 'monthly'")

        if is_streak:
            current_streak += 1
        else:
            streaks.append(current_streak)
            current_streak = 1

    streaks.append(current_streak)
    return max(streaks) if streaks else 0


def get_current_streak(completions, periodicity):
    """Calculate the current active streak for a habit."""
    if not completions:
        return 0

    completions_sorted = sorted(completions, reverse=True)
    current_streak = 1
    today = datetime.now().date()

    for i in range(1, len(completions_sorted)):
        prev = completions_sorted[i - 1]
        curr = completions_sorted[i]

        if periodicity == 'daily':
            expected = prev + timedelta(days=1)
            is_streak = curr.date() == expected.date()
        elif periodicity == 'weekly':
            expected = prev + timedelta(weeks=1)
            is_streak = curr.date() == expected.date()
        elif periodicity == 'monthly':
            is_streak = (
                    curr.day == prev.day and
                    (curr.year == prev.year and curr.month == prev.month + 1) or
                    (curr.year == prev.year + 1 and curr.month == 1 and prev.month == 12)
            )
        else:
            raise ValueError("Periodicity must be 'daily', 'weekly', or 'monthly'")

        if is_streak:
            current_streak += 1
        else:
            break

    last_completion = completions_sorted[0].date()
    if periodicity == 'daily' and (today - last_completion).days > 1:
        return 0
    elif periodicity == 'weekly' and (today - last_completion).days > 7:
        return 0
    elif periodicity == 'monthly' and last_completion < today - timedelta(days=30):
        return 0

    return current_streak


def get_all_longest_streaks(habits, tracker):
    """Get longest streaks for all habits.

    Args:
        habits: List of Habit objects
        tracker: HabitTracker instance

    Returns:
        Dictionary of {habit_name: longest_streak}
    """
    streaks = {}
    for habit in habits:
        completions = tracker.get_habit_completions(habit.habit_id)
        streaks[habit.name] = get_longest_streak(completions, habit.periodicity)
    return streaks


def get_global_longest_streak(habits, tracker):
    """Get the maximum streak across all habits.

    Args:
        habits: List of Habit objects
        tracker: HabitTracker instance

    Returns:
        Tuple of (habit_name, streak_length)
    """
    streaks = get_all_longest_streaks(habits, tracker)
    return max(streaks.items(), key=lambda x: x[1], default=(None, 0))