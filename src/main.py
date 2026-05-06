from agent import FinanceAgent

def main():
    agent = FinanceAgent("data/expenses.csv")

    print("Personal Finance AI Agent Ready (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = agent.handle_query(user_input)
        print("\nAgent:", response, "\n")

if __name__ == "__main__":
    main()