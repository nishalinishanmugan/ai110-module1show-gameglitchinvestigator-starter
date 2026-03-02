import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

def hot_cold_label(guess: int, secret: int) -> str:
    diff = abs(guess - secret)
    if diff == 0:
        return "🎯 Perfect!"
    if diff <= 3:
        return "🔥 Hot"
    if diff <= 10:
        return "🌤️ Warm"
    return "❄️ Cold"

def closeness_emoji(diff: int) -> str:
    if diff == 0:
        return "🎯"
    if diff <= 3:
        return "🔥"
    if diff <= 10:
        return "🌤️"
    return "❄️"

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

#FIXME: The game doesn't reset when changing difficulty. I added a check to reset the game when the difficulty changes.
if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

if "secret" not in st.session_state or st.session_state.difficulty != difficulty:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.difficulty = difficulty

#FIXME:The attempts number was weird and one off. 
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.sidebar.subheader("Guess History")

valid_guesses = [h for h in st.session_state.history if h.get("valid")]

if not valid_guesses:
    st.sidebar.caption("No guesses yet.")
else:
    # Show most recent first 
    for i, h in enumerate(reversed(valid_guesses), start=1):
        g = h["guess"]
        diff = abs(g - st.session_state.secret)
        icon = closeness_emoji(diff)

        # Guess if off by
        st.sidebar.write(f"{icon} Guess {g} (off by {diff})")

st.subheader("Make a guess")

##FIXME: The range isn't always 1 to 100. Change it to low to high. 
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

#FIXME: Switching Difficulty doesn't reset the game. Add a new game button to reset the game when changing difficulty.
raw_guess = st.text_input(
    "Enter your guess:",
    key="guess_input"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

#FIXME: Change the range from low to high instead of hardcoding it to 1 to 100
# I also added a playing status check to prevent playing after winning or losing until a new game is started.
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ##FIXME: Take out the increment of attempts from the top and put it here so that it only increments when a guess is submitted. 
    ## st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append({"raw": raw_guess, "valid": False})
        st.error(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append({"raw": raw_guess, "guess": guess_int, "valid": True})

        secret = st.session_state.secret
        outcome, message = check_guess(guess_int, secret)

        temp = hot_cold_label(guess_int, secret)

        if show_hint:
            if outcome == "Too High":
                st.error(f"{message}  {temp}")
            elif outcome == "Too Low":
                st.info(f"{message}  {temp}")
            else:
                st.success(f"{message}  {temp}")

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
