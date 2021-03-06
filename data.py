import datetime
from typing import Optional, List


class NewRecipe:
    def __init__(
            self,
            name: str,
            ingredients: List['Ingredient'],
            prep: str,
            recipe: str
    ):
        self.name = name
        self.ingredients = ingredients
        self.prep = prep
        self.recipe = recipe


class RecipeEntry(NewRecipe):
    def __init__(self, recipe_id: int, name: str, ingredients: List['Ingredient'], prep: str, recipe: str):
        super().__init__(name, ingredients, prep, recipe)
        self.recipe_id = recipe_id

    def to_json(self):
        return {
            "recipe_id": self.recipe_id,
            "name": self.name,
            "ingredients": [i.to_json() for i in self.ingredients],
            "prep": self.prep,
            "recipe": self.recipe
        }


class FullRecipe(RecipeEntry):
    def __init__(
            self,
            recipe_id: int,
            name: str,
            ingredients: List['Ingredient'],
            prep: str,
            recipe: str,
            history: List['HistoryEntryForRecipe'],
            schedule: List['ScheduleEntryForRecipe']
    ):
        super().__init__(recipe_id, name, ingredients, prep, recipe)
        self.history = history
        self.schedule = schedule

    def to_json(self):
        return {
            "recipe_id": self.recipe_id,
            "name": self.name,
            "ingredients": [i.to_json() for i in self.ingredients],
            "prep": self.prep,
            "recipe": self.recipe,
            "history": [h.to_json() for h in self.history],
            "schedule": [s.to_json() for s in self.schedule]
        }


class Ingredient:
    def __init__(self, amount: str, item: str):
        self.amount = amount
        self.item = item

    def to_json(self):
        return {
            "amount": self.amount,
            "item": self.item
        }


class HistoryEntryForRecipe:
    def __init__(
            self,
            date: datetime.date,
            start_time: Optional[datetime.datetime],
            end_time: Optional[datetime.datetime]
    ):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def to_json(self):
        return {
            "date": self.date.isoformat(),
            "start_time": self.start_time.isoformat() if self.start_time is not None else None,
            "end_time": self.end_time.isoformat() if self.end_time is not None else None
        }


class ScheduleEntryForRecipe:
    def __init__(self, date: datetime.date):
        self.date = date

    def to_json(self):
        return {
            "date": self.date.isoformat()
        }


class ScheduleEntry(ScheduleEntryForRecipe):
    def __init__(self, date: datetime.date, recipe: RecipeEntry):
        super().__init__(date)
        self.recipe = recipe

    def to_json(self):
        return {
            "recipe": self.recipe.to_json()
        }


class HistoryEntry(HistoryEntryForRecipe):
    def __init__(
            self,
            date: datetime.date,
            start_time: Optional[datetime.datetime],
            end_time: Optional[datetime.datetime],
            recipe: RecipeEntry
    ):
        super().__init__(date, start_time, end_time)
        self.recipe = recipe

    def to_json(self):
        return {
            "start_time": self.start_time.isoformat() if self.start_time is not None else None,
            "end_time": self.end_time.isoformat() if self.end_time is not None else None,
            "recipe": self.recipe.to_json()
        }
