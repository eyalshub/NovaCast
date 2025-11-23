import pytest
from app.core.flow.intent import classify_intent

def test_classify_intent_greeting():
    user_input = "Hello, how are you?"
    expected_intent = "greeting"
    assert classify_intent(user_input) == expected_intent

def test_classify_intent_farewell():
    user_input = "Goodbye, see you later!"
    expected_intent = "farewell"
    assert classify_intent(user_input) == expected_intent

def test_classify_intent_question():
    user_input = "What is the weather like today?"
    expected_intent = "question"
    assert classify_intent(user_input) == expected_intent

def test_classify_intent_unknown():
    user_input = "Blah blah blah"
    expected_intent = "unknown"
    assert classify_intent(user_input) == expected_intent

def test_classify_intent_empty_input():
    user_input = ""
    expected_intent = "unknown"
    assert classify_intent(user_input) == expected_intent