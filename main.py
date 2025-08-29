from habit_tracker import HabitTracker
from analytics import get_longest_streak, get_current_streak
from visualization import plot_habit_progress

def main():
    tracker = HabitTracker()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Create a new habit")
        print("2. Complete a habit")
        print("3. View all habits")
        print("4. View habit analytics")
        print("5. Generate progress graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (daily/weekly/monthly): ")
            tracker.create_habit(name, periodicity)
            print(f"Habit '{name}' created!")

        elif choice == "2":
            habits = tracker.get_all_habits()
            for habit in habits:
                print(f"{habit.habit_id}: {habit.name} ({habit.periodicity})")
            habit_id = int(input("Enter habit ID to complete: "))
            tracker.complete_habit(habit_id)
            print("Habit completed!")

        elif choice == "3":
            habits = tracker.get_all_habits()
            for habit in habits:
                print(f"{habit.habit_id}: {habit.name} ({habit.periodicity})")

        elif choice == "4":
            print("\nAnalytics Options:")
            print("1. View all habits")
            print("2. View habits by periodicity")
            print("3. View longest streaks")
            print("4. View longest streak for a habit")

            analytics_choice = input("Enter analytics choice: ")

            if analytics_choice == "1":
                habits = tracker.get_all_habits()
                for habit in habits:
                    print(f"{habit.habit_id}: {habit.name} ({habit.periodicity})")

            elif analytics_choice == "2":
                periodicity = input("Enter periodicity (daily/weekly/monthly): ").lower()
                if periodicity not in ['daily', 'weekly', 'monthly']:
                    print("Invalid periodicity!")
                    continue

                habits = tracker.get_habits_by_periodicity(periodicity)
                print(f"\n{periodicity.capitalize()} habits:")
                for habit in habits:
                    print(f"- {habit.name} (ID: {habit.habit_id})")

            elif analytics_choice == "3":
                habit_name, streak = tracker.get_global_longest_streak()
                print(f"\nOverall longest streak: {habit_name} with {streak} days")

            elif analytics_choice == "4":
                habits = tracker.get_all_habits()
                for habit in habits:
                    print(f"{habit.habit_id}: {habit.name}")
                try:
                    habit_id = int(input("Enter habit ID: "))
                    streak = tracker.get_longest_streak_for_habit(habit_id)
                    print(f"Longest streak for this habit: {streak}")
                except ValueError:
                    print("Invalid habit ID!")

        elif choice == "5": 
            habits = tracker.get_all_habits()
            for habit in habits:
                print(f"{habit.habit_id}: {habit.name} ({habit.periodicity})")
            habit_id = int(input("Enter habit ID to graph: "))
            selected_habit = next(h for h in habits if h.habit_id == habit_id)
            completions = [c.isoformat() for c in tracker.get_habit_completions(habit_id)]
            filename = plot_habit_progress(selected_habit.name, completions, show_plot=True)
            print(f"Graph generated and saved as '{filename}'")

        elif choice == "6": 
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()