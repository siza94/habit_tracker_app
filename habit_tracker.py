from datetime import datetime
from storage import JSONStorage

class Habit:
    def __init__(self, habit_id, name, periodicity, created_at):
        self.habit_id = habit_id
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.fromisoformat(created_at)

    def __repr__(self):
        return f"Habit(id={self.habit_id}, name={self.name}, periodicity={self.periodicity})"

class HabitTracker:
    def __init__(self):
        self.storage = JSONStorage()

    def create_habit(self, name, periodicity):
        """Create a new habit."""
        self.storage.add_habit(name, periodicity)

    def complete_habit(self, habit_id):
        """Mark a habit as completed."""
        self.storage.complete_habit(habit_id)

    def get_all_habits(self):
        """Retrieve all habits."""
        return [
            Habit(habit["id"], habit["name"], habit["periodicity"], habit["created_at"])
            for habit in self.storage.get_habits()
        ]

    def get_habit_completions(self, habit_id):
        """Retrieve all completions for a habit."""
        return [
            datetime.fromisoformat(completion)
            for completion in self.storage.get_completions(habit_id)
        ]

    def get_habits_by_periodicity(self, periodicity):
        """Retrieve habits filtered by periodicity (e.g., 'daily', 'weekly')."""
        return [
            Habit(habit["id"], habit["name"], habit["periodicity"], habit["created_at"])
            for habit in self.storage.get_habits()
            if habit["periodicity"].lower() == periodicity.lower()
        ]

    def get_global_longest_streak(self):
        """Return the habit with the longest streak across all habits."""
        habits = self.get_all_habits()
        longest_streak = 0
        top_habit = None

        for habit in habits:
            completions = self.get_habit_completions(habit.habit_id)
            streak = self._calculate_streak(completions, habit.periodicity)
            if streak > longest_streak:
                longest_streak = streak
                top_habit = habit

        if top_habit:
            return top_habit.name, longest_streak
        else:
            return None, 0

    def _calculate_streak(self, completions, periodicity):
        """Calculate the current streak based on completions and periodicity."""
        if not completions:
            return 0

        completions.sort(reverse=True)
        streak = 1
        today = datetime.now()

        for i in range(1, len(completions)):
            diff = (completions[i - 1] - completions[i]).days

            if periodicity == "daily" and diff == 1:
                streak += 1
            elif periodicity == "weekly" and diff <= 7:
                streak += 1
            else:
                break

        # Check if most recent completion was today/yesterday/week
        latest = completions[0]
        if (periodicity == "daily" and (today - latest).days > 1) or \
           (periodicity == "weekly" and (today - latest).days > 7):
            streak = 0

        return streak

    def get_longest_streak_for_habit(self, habit_id):
        """Return the longest streak for a given habit."""
        habit = next((h for h in self.get_all_habits() if h.habit_id == habit_id), None)
        if not habit:
            return 0
        completions = self.get_habit_completions(habit_id)
        return self._calculate_streak(completions, habit.periodicity)
