import json
import pytest

def test_exercises_have_required_fields():
    with open('code_practice_exercises.json', 'r') as f:
        data = json.load(f)
    
    for practice_type, content in data['practice_types'].items():
        for exercise in content['exercises']:
            assert exercise['prompt'] is not None, f"Prompt is null in {exercise['id']}"
            assert exercise['sample_solution'] is not None, f"Sample solution is null in {exercise['id']}"
            assert exercise['test_cases'], f"Test cases empty in {exercise['id']}"
            for tc in exercise['test_cases']:
                assert tc['expected_output'] is not None, f"Expected output null in {exercise['id']}" 