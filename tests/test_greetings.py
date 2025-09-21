import pytest
from app.greetings import greeting

def test_greeting():
    assert greeting("Sonam") == "Good Morning Sonam"