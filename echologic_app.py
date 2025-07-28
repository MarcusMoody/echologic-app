import streamlit as st
from logic_game import EchoLogicGame  # Ensure this file is in the same directory

# Initialize session state
if "game" not in st.session_state:
    st.session_state.game = EchoLogicGame()
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "selected_index" not in st.session_state:
    st.session_state.selected_index = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "level_message" not in st.session_state:
    st.session_state.level_message = ""
if "current_puzzle" not in st.session_state:
    st.session_state.current_puzzle = st.session_state.game.get_puzzle()

# Title
st.title("🧠 EchoLogic: The Mind Builder")

# Display current level
st.markdown(f"### Current Level: {st.session_state.game.level}")

# Show puzzle
puzzle = st.session_state.current_puzzle
st.markdown(f"**Category:** `{puzzle['category'].capitalize()}` | **Difficulty:** `{puzzle['difficulty'].capitalize()}`")
st.markdown(f"#### {puzzle['question']}")

# Answer options with no default selected
st.session_state.selected_index = st.radio(
    "Choose your answer:",
    options=range(len(puzzle["options"])),
    format_func=lambda i: puzzle["options"][i],
    index=None,
    key="answer"
)

# Submit button
if st.button("Submit", disabled=st.session_state.submitted or st.session_state.selected_index is None):
    if st.session_state.selected_index is not None:
        correct, feedback = st.session_state.game.check_answer(puzzle, st.session_state.selected_index)
        st.session_state.feedback = feedback
        st.session_state.level_message = st.session_state.game.update_level()
        st.session_state.submitted = True

# Show feedback if submitted
if st.session_state.submitted:
    st.info(st.session_state.feedback)
    if st.session_state.level_message:
        st.success(st.session_state.level_message)

# Next button (appears only after submitting)
if st.session_state.submitted:
    if st.button("➡️ Next Question"):
        st.session_state.current_puzzle = st.session_state.game.get_puzzle()
        st.session_state.selected_index = None
        st.session_state.submitted = False
        st.session_state.feedback = ""
        st.session_state.level_message = ""
        st.rerun()