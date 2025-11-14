# High Reliability Math Operations Project

A small, well-tested Python module designed to demonstrate high-reliability software engineering practices. This project focuses on:

- **Clean, modular code**
- **Comprehensive exception handling**
- **Automated testing with pytest**
- **100% test coverage**
- **Deterministic behavior**
- **Reproducible results**

---

## 🚀 Project Overview

This project implements a set of mathematical utility functions with a strong emphasis on:

- **Reliability:** Functions produce predictable outputs.
- **Error handling:** Each function handles invalid inputs safely.
- **Automation:** Full unit tests ensure correctness and coverage.
- **High-reliability system design principles** similar to aerospace, finance, or safety-critical systems.

---

## 📂 Project Structure

high_reliability_project/
│
├── src/
│ ├── main.py
│ ├── init.py
│ └── core/
│ ├── math_ops.py
│ └── init.py
│
├── tests/
│ ├── test_main.py
│ └── test_math_ops.py
│
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🧮 Implemented Functions

### Arithmetic

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b, ndigits=None)`

### Statistics

- `mean(values)`
- `median(values)`
- `variance(values, sample=False)`

---

## ⚠️ Error Handling & Reliability

Each function is designed to **fail safely**:

| Function | Error Cases Handled     |
| -------- | ----------------------- |
| add      | non-numeric inputs      |
| subtract | none                    |
| multiply | none                    |
| divide   | zero-division, rounding |
| mean     | empty input             |
| median   | empty input             |
| variance | less than 2 values      |

---

## 🧪 Testing Strategy

We use **pytest + pytest-cov** to ensure high reliability:

- Valid input tests
- Error/exception tests
- Edge-case tests
- Full testing of `main.py` and `math_ops.py`
- **100% test coverage achieved**

---

## 🟩 Coverage Report

TOTAL: 37 statements
MISSED: 0
COVERAGE: 100%

yaml
Copy code

---

## ⚙️ Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/Pruthvish77/high_reliability_project.git
cd high_reliability_project
Create a virtual environment:

bash
Copy code
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
▶️ Running the Demo
bash
Copy code
python src/main.py
🧪 Running Tests
bash
Copy code
pytest --cov=src --cov-report=term-missing
📘 Assumptions
Inputs are numeric unless otherwise stated

No external libraries used for math (Python standard library only)

Statistical functions operate on list-like numeric sequences

Rounding uses Python’s built-in round()

🎯 Why This Project Meets High-Reliability Standards
Clean, deterministic functions

Full exception coverage

18 automated tests

100% test coverage

Clear error messages

No undefined or implicit behavior

Modular, easily testable logic

```
