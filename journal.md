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
