def get_range_for_difficulty(difficulty: str):
    #"""Return (low, high) inclusive range for a given difficulty."""
    """
    Determine the inclusive numeric range for a given difficulty level.

    Args:
        difficulty (str): The selected difficulty level.
            Expected values: "Easy", "Normal", or "Hard".

    Returns:
        tuple[int, int]: A tuple representing the inclusive (low, high)
            bounds for the secret number.

    Behavior:
        - "Easy"   -> (1, 20)
        - "Normal" -> (1, 100)
        - "Hard"   -> (1, 200)
        - Any unexpected value defaults to (1, 100)

    Notes:
        The Hard range is intentionally larger than Normal to increase
        difficulty by expanding the possible secret number space.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    #FIXME: The hard difficulty is actually easier than normal because the range is smaller.
    #Changed to 200 to make it harder.
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Convert raw user input into an integer guess.

    Args:
        raw (str | None): The raw text entered by the user.

    Returns:
        tuple[bool, int | None, str | None]:
            - ok (bool): True if parsing succeeded, False otherwise.
            - guess_int (int | None): Parsed integer value if successful.
            - error_message (str | None): Error message if parsing failed.

    Behavior:
        - Empty or None input returns a user-friendly error.
        - Decimal strings (e.g., "12.7") are converted using int(float(raw)).
        - Invalid numeric formats return an error message.
        - Leading/trailing whitespace is handled automatically by int().

    This function does not enforce difficulty bounds; that logic is handled
    elsewhere in the application.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare a player's guess to the secret number.

    Args:
        guess (int): The player's numeric guess.
        secret (int): The secret number to compare against.

    Returns:
        tuple[str, str]:
            - outcome (str): One of "Win", "Too High", or "Too Low".
            - message (str): User-facing feedback message.

    Behavior:
        - If guess equals secret -> returns ("Win", success message).
        - If guess > secret -> returns ("Too High", guidance to go lower).
        - If guess < secret -> returns ("Too Low", guidance to go higher).

    Error Handling:
        A fallback string comparison is included to guard against
        accidental type mismatches. However, in normal operation,
        both guess and secret should be integers.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    #FIXME: The logic for Too High and Too Low is reversed. If the guess is greater than the secret, it should be "Too Low" and vice versa.
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go LOWER!"
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    #"""Update score based on outcome and attempt number."""
    """
    Update the player's score based on the game outcome.

    Args:
        current_score (int): The player's score before this guess.
        outcome (str): The result from check_guess().
            Expected values: "Win", "Too High", "Too Low".
        attempt_number (int): The current attempt count (1-based).

    Returns:
        int: The updated score.

    Scoring Rules:
        - Winning awards points based on speed:
              100 - (10 * attempt_number)
          A minimum of 10 points is guaranteed for a win.
        - Any non-winning guess subtracts 5 points.

    Notes:
        This scoring system rewards faster wins while applying
        a consistent penalty for incorrect guesses.
    """
    #FIXME: The scoring system is a bit weird. Winning on the first attempt gives 90 points, but winning on the second attempt gives 80 points, and so on. I changed it to give more points for earlier wins and a minimum of 10 points for winning.
    if outcome == "Win":
        base_points = 100
        deduction_per_attempt = 10
        points = base_points - (deduction_per_attempt * attempt_number)
        return current_score + max(points, 10)

   #If the outcome is not a win.
    return current_score - 5

    #if outcome == "Too High":
    #    if attempt_number % 2 == 0:
    #        return current_score + 5
    #    return current_score - 5

    #if outcome == "Too Low":
    #    return current_score - 5

    #return current_score
