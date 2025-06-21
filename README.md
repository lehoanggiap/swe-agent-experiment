# SWE Agent Experiment 🤖

This repository demonstrates an automated software engineering workflow using **SWE Agent** to detect, report, and fix bugs automatically.

## Project Overview

This project contains:
1. **FastAPI Calculator API** - A simple REST API with basic mathematical operations
2. **Intentional Bug** - A division by zero vulnerability for demonstration
3. **Automated SWE Agent** - GitHub Actions workflow that detects and fixes issues automatically
4. **Comprehensive Testing** - Test suite that exposes the bugs

## 🐛 The Intentional Bug

The calculator API has a **division by zero bug** in the `/calculate` endpoint:

```python
elif operation == "divide":
    # BUG: No check for division by zero!
    result = a / b  # This will raise ZeroDivisionError when b=0
```

When you try to divide by zero, the API crashes with a 500 error instead of gracefully handling the error.

## 🤖 Real SWE Agent Workflow

The GitHub Actions workflow (`.github/workflows/swe-agent.yml`) uses the **actual SWE Agent from Princeton NLP** to work like a real human software engineer:

1. **Intelligent Issue Detection** 🔍
   - Runs test suite to identify failing tests
   - Performs AST-based static analysis to detect potential bugs
   - Analyzes code patterns that could cause runtime errors
   - Identifies division by zero and other unsafe operations

2. **Automated Issue Creation** 📝
   - Creates detailed GitHub issues with:
     - Complete test output and error traces
     - Static analysis findings with line numbers
     - Steps to reproduce the problems
     - Expected vs actual behavior descriptions
     - Auto-assignment to SWE Agent for resolution

3. **SWE Agent Autonomous Problem Solving** 🧠
   - **Uses GPT-4** to understand the codebase and problem context
   - **Explores files autonomously** like a human engineer would
   - **Analyzes failing tests** to understand what needs to be fixed
   - **Develops sophisticated fixes** beyond simple pattern matching
   - **Tests solutions iteratively** until problems are resolved

4. **Human-like Engineering Process** 👩‍💻
   - Reads and comprehends existing code structure
   - Understands the intent behind failing tests
   - Considers multiple solution approaches
   - Implements the most appropriate and maintainable fix
   - Validates that changes don't break existing functionality

5. **Professional Pull Request Creation** 🔄
   - Creates feature branch with descriptive name
   - Commits changes with detailed technical messages
   - Opens comprehensive PR with:
     - Technical explanation of the fix
     - Analysis of what was broken and why
     - Verification steps for reviewers
     - Links to related issues

This is **not a simple find-and-replace** - it's a sophisticated AI agent that can reason about code, understand context, and solve complex programming problems autonomously.

## 🚀 Getting Started

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/swe-agent-experiment.git
   cd swe-agent-experiment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

4. **Test the API**
   ```bash
   # Test normal operation
   curl -X POST "http://localhost:8000/calculate" \
        -H "Content-Type: application/json" \
        -d '{"a": 10, "b": 2, "operation": "divide"}'
   
   # Test the bug (this will crash!)
   curl -X POST "http://localhost:8000/calculate" \
        -H "Content-Type: application/json" \
        -d '{"a": 10, "b": 0, "operation": "divide"}'
   ```

5. **Run tests**
   ```bash
   pytest test_main.py -v
   ```

### API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /calculate` - Perform calculations
- `GET /history` - View calculation history
- `GET /history/clear` - Clear history

## 🔧 SWE Agent Configuration

The workflow is triggered by:
- **Daily schedule** (8 AM UTC)
- **Manual trigger** (workflow_dispatch)
- **Code changes** (push to main branch)

### Workflow Steps

1. **Environment Setup** - Python 3.11, dependencies
2. **Issue Detection** - Test execution, static analysis
3. **Issue Creation** - Automated GitHub issue with details
4. **Fix Application** - Smart code fixes based on detected issues
5. **Verification** - Test fixes before committing
6. **PR Creation** - Comprehensive pull request with changes

## 🧪 Testing the SWE Agent

To trigger the SWE Agent workflow:

1. **Push the buggy code** (already done - the main.py has the bug)
2. **Workflow runs automatically** and detects the failing test
3. **GitHub issue is created** with bug details
4. **PR is created** with the fix
5. **Review and merge** the automated fix

You can also trigger it manually:
- Go to **Actions** tab in GitHub
- Select **SWE Agent Auto Issue Detection and Fix**
- Click **Run workflow**

## 📁 Project Structure

```
swe-agent-experiment/
├── main.py                    # FastAPI app with intentional bug
├── test_main.py              # Test suite that exposes the bug
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .github/
    └── workflows/
        └── swe-agent.yml     # SWE Agent workflow configuration
```

## 🎯 Expected Outcomes

When the **real SWE Agent** runs, you should see:

1. **GitHub Issue** titled "🤖 SWE Agent: Fix Division by Zero and Test Failures"
   - Detailed problem analysis with test output
   - Static analysis findings
   - Clear steps to reproduce the issue
   - Professional problem description

2. **SWE Agent Working** (in action logs)
   - Agent exploring the codebase
   - Reading and understanding files
   - Analyzing failing tests
   - Developing and testing solutions

3. **Pull Request** titled "🤖 SWE Agent: Fix Division by Zero Bug"
   - Sophisticated code fixes that go beyond simple patterns
   - Proper error handling with HTTP status codes
   - Comprehensive change explanations
   - Professional engineering documentation

4. **High-Quality Fixes**
   - Intelligent error handling that maintains API consistency
   - Updated tests that properly validate the fixes
   - Code that follows best practices
   - Solutions that a human engineer would be proud of

The key difference: **This uses the actual Princeton NLP SWE Agent**, not custom scripts. It can reason about your code and create genuinely intelligent solutions.

## 🛠️ Customization

You can extend this project by:

- Adding more intentional bugs for SWE Agent to find
- Enhancing the fix logic in the workflow
- Adding more sophisticated static analysis
- Integrating with other CI/CD tools
- Adding security scanning
- Implementing performance monitoring

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to:
- Add more bugs for demonstration
- Improve the SWE Agent workflow
- Enhance the fix detection logic
- Add more comprehensive testing

---

**🤖 Powered by SWE Agent** - Automated Software Engineering