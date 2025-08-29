import json
from datetime import datetime
from pathlib import Path

class JSONStorage:
    def __init__(self, file_path="habits.json"):
        self.file_path = Path(file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create the JSON file if it doesn't exist with proper structure."""
        if not self.file_path.exists():
            initial_data = {
                "habits": [],
                "completions": [],
                "analytics_settings": {
                    "graph_directory": "graphs",
                    "default_periodicities": ["daily", "weekly", "monthly"]
                }
            }
            self.file_path.write_text(json.dumps(initial_data, indent=4))

    def _load_data(self):
        """Load and validate data from the JSON file."""
        with open(self.file_path, "r") as file:
            data = json.load(file)
            
            if "habits" not in data:
                data["habits"] = []
            if "completions" not in data:
                data["completions"] = []
            if "analytics_settings" not in data:
                data["analytics_settings"] = {
                    "graph_directory": "graphs",
                    "default_periodicities": ["daily", "weekly", "monthly"]
                }
                
            return data

    def _save_data(self, data):
        """Save data to the JSON file with validation."""
        if not all(key in data for key in ["habits", "completions", "analytics_settings"]):
            raise ValueError("Invalid data structure")
            
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_habit(self, name, periodicity):
        """Add a new habit with validation.
        
        Args:
            name (str): Name of the habit
            periodicity (str): One of 'daily', 'weekly', or 'monthly'
            
        Raises:
            ValueError: If periodicity is invalid
        """
        if periodicity not in ["daily", "weekly", "monthly"]:
            raise ValueError("Periodicity must be 'daily', 'weekly', or 'monthly'")
            
        data = self._load_data()
        habit = {
            "id": len(data["habits"]) + 1,
            "name": name,
            "periodicity": periodicity,
            "created_at": datetime.now().isoformat(),
            "description": "",  
            "target_streak": 0 
        }
        data["habits"].append(habit)
        self._save_data(data)
        return habit["id"]  

    def complete_habit(self, habit_id):
        """Mark a habit as completed with validation.
        
        Args:
            habit_id (int): ID of the habit to complete
            
        Returns:
            bool: True if successful, False if habit doesn't exist
        """
        data = self._load_data()
        
        
        if not any(h["id"] == habit_id for h in data["habits"]):
            return False
            
        completion = {
            "habit_id": habit_id,
            "completed_at": datetime.now().isoformat()
        }
        data["completions"].append(completion)
        self._save_data(data)
        return True

    def get_habits(self, periodicity=None):
        """Retrieve habits, optionally filtered by periodicity.
        
        Args:
            periodicity (str, optional): Filter by 'daily', 'weekly', or 'monthly'
            
        Returns:
            list: List of habit dictionaries
        """
        data = self._load_data()
        if periodicity:
            return [h for h in data["habits"] if h["periodicity"] == periodicity]
        return data["habits"]

    def get_completions(self, habit_id, limit=None):
        """Retrieve completions for a specific habit.
        
        Args:
            habit_id (int): ID of the habit
            limit (int, optional): Maximum number of completions to return
            
        Returns:
            list: List of completion timestamps (ISO format)
        """
        data = self._load_data()
        completions = [
            c["completed_at"] 
            for c in data["completions"] 
            if c["habit_id"] == habit_id
        ]
        return completions[:limit] if limit else completions

    def get_habit_by_id(self, habit_id):
        """Get a specific habit by its ID.
        
        Args:
            habit_id (int): ID of the habit
            
        Returns:
            dict: Habit data or None if not found
        """
        data = self._load_data()
        for habit in data["habits"]:
            if habit["id"] == habit_id:
                return habit
        return None

    def update_habit(self, habit_id, **kwargs):
        """Update habit properties.
        
        Args:
            habit_id (int): ID of the habit to update
            **kwargs: Fields to update (name, periodicity, description, etc.)
            
        Returns:
            bool: True if successful, False if habit doesn't exist
        """
        data = self._load_data()
        for habit in data["habits"]:
            if habit["id"] == habit_id:
                for key, value in kwargs.items():
                    if key in habit:
                        habit[key] = value
                self._save_data(data)
                return True
        return False

    def delete_habit(self, habit_id):
        """Delete a habit and its completions.
        
        Args:
            habit_id (int): ID of the habit to delete
            
        Returns:
            bool: True if successful, False if habit doesn't exist
        """
        data = self._load_data()
        
        habits = [h for h in data["habits"] if h["id"] != habit_id]
        if len(habits) == len(data["habits"]):
            return False
            
        completions = [c for c in data["completions"] if c["habit_id"] != habit_id]
        
        data["habits"] = habits
        data["completions"] = completions
        self._save_data(data)
        return True

    def get_analytics_settings(self):
        """Get analytics configuration.
        
        Returns:
            dict: Analytics settings including graph directory
        """
        data = self._load_data()
        return data.get("analytics_settings", {})

    def get_habits_by_periodicity(self, periodicity):
        """Retrieve all habits with a specific periodicity.

        Args:
            periodicity: 'daily', 'weekly', or 'monthly'

        Returns:
            List of habit dictionaries matching the periodicity
        """
        data = self._load_data()
        return [habit for habit in data['habits'] if habit['periodicity'] == periodicity]