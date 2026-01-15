import json
from pick import pick
from pathlib import Path
import os

class Data:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.data_dir = self.base_dir / "data"
        self.domain: str = self.select_domain()

    def select_domain(self) -> str:
        """Select domain to display"""
        domains = [
            file.stem for file in self.data_dir.glob("*.json")
            if file.name != "ascii.json"
        ]
        title = "CheatBox> Select the cheatsheet to display"
        domain = pick(options=domains, title=title)
        return str(domain[0]) # only return the name

    def read_domain(self):
        """Read the content of the domain"""
        try:
            with open(f"{self.data_dir / self.domain}.json", 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {self.domain}.json: {e}")
            return {} # Return empty dict instead of None to prevent crashes

    def run(self):
        """Runner for data fetch"""
        return self.read_domain()
