from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_negative_number():
    # If secret is 50 and guess is -10, it should be "Too Low"
    outcome, message = check_guess(-10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_large_number():
    # If secret is 50 and guess is a very large number, it should be "Too High"
    outcome, message = check_guess(1000000, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_boundary_value():
    # If secret is 50 and guess is 49, it should be "Too Low"
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
