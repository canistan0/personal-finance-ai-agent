from tools.csv_reader import load_expenses
from tools.calculator import sum_amounts, percentage
from tools.summarizer import summarize
from tools.web_search import get_context

class FinanceAgent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = load_expenses(file_path)

    def get_by_category(self, category):
        return [item for item in self.data if item["category"] == category]

    def handle_query(self, query):
        query = query.lower()

        if "spend" in query and "food" in query:
            food = self.get_by_category("food")
            total = sum_amounts(food)
            context = get_context("food spending")
            return summarize("food", total) + "\n" + context

        if "transport" in query:
            transport = self.get_by_category("transport")
            total = sum_amounts(transport)
            return summarize("transport", total)

        if "percentage" in query or "%" in query:
            food = self.get_by_category("food")
            total = sum_amounts(food)
            return f"15% of food spending is {percentage(total, 15):.2f}"

        return "Query not understood. Try asking about food or transport spending."