import random
from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    # EDITED: check_guess returns a tuple (outcome, message), not just a string
    # assert result == "Win"
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    # EDITED: check_guess returns a tuple (outcome, message), not just a string
    # assert result == "Too High"
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    # EDITED: check_guess returns a tuple (outcome, message), not just a string
    # assert result == "Too Low"
    assert result[0] == "Too Low"

def test_new_game_secret_within_range():
    # Simulates what happens when New Game is clicked:
    # get the difficulty range, then generate a secret within it
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        new_secret = random.randint(low, high)
        assert low <= new_secret <= high
