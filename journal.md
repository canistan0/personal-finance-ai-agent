# Journal – Personal Finance AI Agent

---

## Step 1 – 24.04

### System Description and Goal

The system is a Personal Finance AI Agent implemented in Python. It allows users to query personal financial data stored in a CSV file using natural language. The agent processes user input, retrieves relevant financial data, performs calculations, and returns structured responses.

### AI / Agent Approach

The system is built as a single intelligent agent that uses external tools. The agent decides which tool to use based on the user’s query and orchestrates the workflow between tools.

### Tools Used

- CSV Reader Tool (loads expense data)
- Calculator Tool (sum, percentage calculations)
- Web Context Tool (provides external financial context)
- Summarizer Tool (generates natural language output)

### Programming Concepts Required

- Object-oriented programming
- File handling (CSV parsing)
- Data structures (lists/dictionaries)
- Conditional logic
- Function modularization
- Exception handling
- Basic algorithmic computations
- Testing with pytest

---

## Step 2 – 08.05

### Updated description of the system based on implementation progress

The system is now working as a simple command-line Personal Finance AI Agent in Python. It can read data from a CSV file, understand basic user questions, and give answers.

The system includes:

- a main program (main.py) where the user types questions
- an agent (agent.py) that processes the input
- tools for reading data, doing calculations, and creating answers
- a CSV file (expenses.csv) with test data

The agent can answer simple questions like:

- total spending on food or transport
- percentage of spending (for example 15%)

The system shows the full process:
user input → agent → tools → result

---

### Refined list of programming concepts actually used

The system uses these programming concepts:

- classes (object-oriented programming)
- reading files (CSV file)
- lists and dictionaries
- if statements (decision making)
- functions (separate tools)
- filtering data (by category)
- basic calculations (sum, percentage)
- string handling (user input)
- error handling (missing file)
- testing with pytest

---

### Explanation of how these concepts are applied

The system uses a class called FinanceAgent to control the program.
The CSV file is read using a tool, and each row is saved as a dictionary. All data is stored in a list.The agent checks the user input using simple keywords like “food” or “transport”. Based on this, it decides what to do.

Functions are used to separate tasks:

- one function reads data
- one does calculations
- one creates the final message

The calculator tool adds numbers and calculates percentages.The program also converts user input to lowercase to make it easier to understand.Error handling is used if the CSV file is missing.Basic tests are written using pytest to check that the system works correctly.

---

### Description of how tools are integrated into the system

The system uses different tools that work together.
The process is:

1. The user types a question
2. The agent reads the question
3. The agent chooses the correct tools
   - CSV Reader → gets data
   - Calculator → does math
   - Web tool → gives extra info (simple version)
   - Summarizer → creates the answer
4. The agent combines the results
5. The final answer is shown to the user

Each tool works separately, so it is easy to test and change them.This makes the system simple and organized.

---

## Step 3 – 15.05

### Description of the testing process

Testing was done during development of the system. Each tool was tested separately before testing the full program.

The testing checked:

- if the CSV file loads correctly
- if calculations are correct
- if the agent understands simple questions
- if the system handles wrong input safely

The tests were written using pytest.

---

### Test scenarios and explanation

#### 1. CSV Reader Test

Purpose:
Check if the CSV file is loaded correctly.

Test:

- load `expenses.csv`

Expected result:

- data is loaded into a list
- each row contains date, category, and amount

---

#### 2. Calculator Test

Purpose:
Check if calculations work correctly.

Test:

- input values: 10 and 20

Expected result:

- total = 30

---

#### 3. Agent Test

Purpose:
Check if the agent answers user questions correctly.

Test examples:

- “How much did I spend on food?”
- “How much transport spending?”
- “What is 15% of food spending?”

Expected result:

- correct answer is returned

---

#### 4. Invalid Input Test

Purpose:
Check how the system handles unknown input.

Test:

- random text input

Expected result:

- system shows a message like:
  “Query not understood”

---

### Summary of testing results

The tests were successful.

The system:

- loads data correctly
- performs calculations correctly
- answers supported questions
- handles invalid input without crashing

The modular structure made testing easier.

---

### Deployment preparation

The system can be run locally as a command-line application.

Requirements:

- Python 3
- required libraries from `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
```
