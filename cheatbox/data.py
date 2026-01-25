import json
from pick import pick
from pathlib import Path
import os
from difflib import SequenceMatcher

class Data:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.data_dir = self.base_dir / "data"
        self.domain: str = self.select_domain()

    def fuzzy_search(self, query: str, options: list, threshold: float = 0.3) -> list:
        """
        Fuzzy search implementation for matching cheats
        Returns list of (score, option) tuples sorted by relevance
        """
        results = []
        query_lower = query.lower()

        for option in options:
            option_lower = option.lower()

            # Check for exact substring match (highest priority)
            if query_lower in option_lower:
                score = 1.0
            else:
                # Use SequenceMatcher for fuzzy matching
                score = SequenceMatcher(None, query_lower, option_lower).ratio()

            if score >= threshold:
                results.append((score, option))

        # Sort by score descending
        results.sort(reverse=True, key=lambda x: x[0])
        return [option for score, option in results]

    def select_domain(self) -> str:
        """Select domain to display with search option"""
        domains = sorted([
            file.stem for file in self.data_dir.glob("*.json")
            if file.name != "ascii.json"
        ])

        # Add search option at the top
        options_with_search = ["🔍 Search Cheatsheets..."] + domains

        title = "CheatBox> Select the cheatsheet"
        selected, index = pick(
            options=options_with_search,
            title=title,
            indicator="→"
        )

        # If search option selected, prompt for query
        if index == 0:
            import typer
            query = typer.prompt("Enter search query")
            results = self.fuzzy_search(query, domains, threshold=0.3)

            if not results:
                typer.echo(f"❌ No cheatsheets found matching '{query}'")
                # Recurse to show menu again
                return self.select_domain()

            if len(results) == 1:
                return results[0]

            # Multiple results, let user pick
            selected_result, _ = pick(
                options=results,
                title=f"🔍 Search results for '{query}'",
                indicator="→"
            )
            return selected_result

        return str(selected)  # Return the selected domain

    def read_domain(self):
        """Read the content of the domain"""
        try:
            with open(f"{self.data_dir / self.domain}.json", 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {self.domain}.json: {e}")
            return {}  # Return empty dict instead of None to prevent crashes

    def run(self):
        """Runner for data fetch"""
        return self.read_domain()
