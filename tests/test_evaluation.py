import pytest
from code_practice import CodePractice

@pytest.fixture
def practice():
    return CodePractice()

def test_evaluate_correct_answer(practice):
    exercise = {
        'test_cases': [
            {'input': {'num_list': [1,2,3]}, 'expected_output': [2]}
        ]
    }
    user_answer = '[x for x in num_list if x % 2 == 0]'
    assert practice._evaluate_answer(user_answer, exercise) is True

def test_evaluate_incorrect_answer(practice):
    exercise = {
        'test_cases': [
            {'input': {'num_list': [1,2,3]}, 'expected_output': [2]}
        ]
    }
    user_answer = '[x for x in num_list]'  # Wrong: no filter
    assert practice._evaluate_answer(user_answer, exercise) is False 