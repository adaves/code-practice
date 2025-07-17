import json
from datetime import datetime
import random
import ast

class CodePractice:
    def __init__(self):
        """Initializes the CodePractice instance by loading exercises and scores."""
        self.exercises = self._load_exercises()
        self.scores = self._load_scores()
        
    def _load_exercises(self):
        """Loads exercises from the JSON file.

        Returns:
            dict: Dictionary of practice types and their exercises.
        """
        with open('code_practice_exercises.json', 'r') as f:
            return json.load(f)['practice_types']
            
    def _load_scores(self):
        """Loads previous scores from scores.txt.

        Returns:
            list: List of score lines, or empty if file not found.
        """
        try:
            with open('scores.txt', 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return []
            
    def _save_score(self, practice_type, daily_score, overall_score):
        """Saves the session score to scores.txt.

        Args:
            practice_type (str): The type of practice (e.g., 'comprehensions').
            daily_score (float): The score for this session.
            overall_score (float): The updated overall score.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        score_line = f"{timestamp}, Type: {practice_type}, Daily Score: {daily_score}%, Overall Score: {overall_score}%\n"
        with open('scores.txt', 'a') as f:
            f.write(score_line)
            
    def _evaluate_answer(self, user_answer, exercise):
        """Evaluates the user's answer against test cases.

        Args:
            user_answer (str): The user's code submission.
            exercise (dict): The exercise data with test cases.

        Returns:
            bool: True if all test cases pass, False otherwise.
        """
        try:
            local_ns = {}  # Restricted namespace for exec
            
            # Update with first test case input if present
            if exercise['test_cases'][0]['input']:
                local_ns.update(exercise['test_cases'][0]['input'])
            
            exec(f"result = {user_answer}", {}, local_ns)  # Execute user code
            user_result = local_ns['result']
            
            # Check each test case
            for test_case in exercise['test_cases']:
                if test_case['input']:
                    local_ns.update(test_case['input'])
                    exec(f"result = {user_answer}", {}, local_ns)
                    user_result = local_ns['result']
                
                if user_result != test_case['expected_output']:
                    return False
            return True
            
        except Exception as e:
            print(f"Error evaluating answer: {str(e)}")
            return False
            
    def practice_session(self, practice_type=None, num_questions=5, max_attempts=3):
        """Runs an interactive practice session.

        Args:
            practice_type (str, optional): Specific practice type. If None, user chooses.
            num_questions (int): Number of questions to ask. Defaults to 5.
            max_attempts (int): Max attempts per question. Defaults to 3.
        """
        if practice_type is None:
            # Let user choose practice type
            available_types = list(self.exercises.keys())
            print("\nAvailable practice types:")
            for i, p_type in enumerate(available_types, 1):
                print(f"{i}. {p_type}")
            choice = int(input("\nChoose practice type (enter number): ")) - 1
            practice_type = available_types[choice]
        
        exercises = self.exercises[practice_type]['exercises']
        selected_exercises = random.sample(exercises, min(num_questions, len(exercises)))  # Random selection
        
        correct = 0
        history = []  # Temp list for session history
        for i, exercise in enumerate(selected_exercises, 1):
            print(f"\nQuestion {i}/{num_questions}:")
            print(exercise['prompt'])
            
            if exercise['test_cases'][0]['input']:
                print(f"Input data: {exercise['test_cases'][0]['input']}")
            
            attempts = 0
            while attempts < max_attempts:
                user_answer = input("Your answer: ").strip()
                is_correct = self._evaluate_answer(user_answer, exercise)
                # Record attempt
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                history.append({
                    'timestamp': timestamp,
                    'practice_type': practice_type,
                    'exercise_id': exercise['id'],
                    'prompt': exercise['prompt'],
                    'user_answer': user_answer,
                    'correct': is_correct
                })
                if is_correct:
                    print("Correct!")
                    correct += 1
                    break
                else:
                    attempts += 1
                    if attempts < max_attempts:
                        print(f"Incorrect. You have {max_attempts - attempts} attempts remaining. Try again!")
                    else:
                        print("Incorrect.")
                        print(f"A sample solution: {exercise['sample_solution']}")
                
        daily_score = (correct / num_questions) * 100
        overall_score = self._calculate_overall_score(practice_type, daily_score)
        
        self._save_score(practice_type, daily_score, overall_score)
        
        # Save history to file
        try:
            with open('practice_history.json', 'r') as f:
                existing_history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_history = []
        existing_history.extend(history)
        with open('practice_history.json', 'w') as f:
            json.dump(existing_history, f, indent=2)

        print(f"\nDaily Score: {daily_score}%")
        print(f"Overall Score: {overall_score}%")

    def _calculate_overall_score(self, practice_type, daily_score):
        """Calculates the overall score for the practice type.

        Args:
            practice_type (str): The practice type.
            daily_score (float): The current session's score.

        Returns:
            float: The averaged overall score.
        """
        if not self.scores:
            return daily_score
            
        # Extract previous overall scores for this type
        type_scores = [float(line.split(', Overall Score: ')[1].rstrip('%\n'))
                      for line in self.scores 
                      if f"Type: {practice_type}" in line]
                      
        return round((sum(type_scores) + daily_score) / (len(type_scores) + 1), 2)

if __name__ == "__main__":
    practice = CodePractice()
    practice.practice_session() 