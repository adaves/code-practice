# Python Comprehensions Practice App

## Project Overview
This is an interactive command-line application for practicing Python coding concepts, starting with comprehensions. It presents exercises, evaluates answers, tracks scores, and is expanding to cover software development, machine learning, and data analysis. The goal is to help the user become a better programmer through daily challenges with adaptive difficulty.

Key features:
- Random exercises from JSON data
- Score tracking in scores.txt
- Planned: Daily mode, category addition, ML/data tasks

## Usage

### Setup
1. Clone the repository (if not already done).
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running a Practice Session
1. Run the main script:
   ```bash
   python code_practice.py
   ```
2. Choose a practice type (e.g., 1 for comprehensions).
3. Answer the prompts with Python code (e.g., list comprehensions).
4. Get feedback and scores. Scores are saved to scores.txt.

### Planned Daily Mode
Run with `--daily` flag (upcoming feature) for one adaptive question per run.

### Adding Categories/Exercises
The app will prompt for new categories and add them to the JSON (upcoming).

## Contributing
Contributions are welcome! To add exercises:
- Edit code_practice_exercises.json or use update_exercise.py.
- Follow TDD: Write tests in tests/ first.
- Submit pull requests or suggest ideas in issues.

Use PEP 8 style, add docstrings (Google style), and run tests with `pytest`.

## Learning Goals
This project is designed for personal growth:
- Master Python fundamentals (comprehensions, loops, classes).
- Practice TDD, documentation, and version control.
- Explore ML (e.g., linear regression with scikit-learn) and data analysis (pandas/numpy).
- Build a history of challenges/answers for LLM context and review. 