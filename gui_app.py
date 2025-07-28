import tkinter as tk
from tkinter import messagebox
from logic_game import EchoLogicGame

game = EchoLogicGame()

# Setup the main window
root = tk.Tk()
root.title("EchoLogic: The Mind Builder")

# Question label
question_label = tk.Label(root, text="", font=("Arial", 20), wraplength=500, justify="center")
question_label.pack(pady=20)

# Buttons for options
option_buttons = []

def load_next_puzzle():
    puzzle = game.get_puzzle()
    question_label.config(text=puzzle["question"])

    def create_option_command(index):
        def handle():
            is_correct, feedback = game.check_answer(puzzle, index)
            messagebox.showinfo("Result", feedback)
            level_msg = game.update_level()
            if level_msg:
                messagebox.showinfo("Level Update", level_msg)
            load_next_puzzle()
        return handle

    for widget in option_buttons:
        widget.destroy()
    option_buttons.clear()

    for idx, option in enumerate(puzzle["options"]):
        btn = tk.Button(root, text=option, font=("Arial", 18), width=10, command=create_option_command(idx))
        btn.pack(pady=5)
        option_buttons.append(btn)

def main():
    global root, question_label
    root = tk.Tk()
    root.title("EchoLogic: The Mind Builder")
    question_label = tk.Label(root, text="", font=("Ariel", 20), wraplength=500)
    question_label.pack(pady=20)
# Start the game
    load_next_puzzle()

    root.mainloop()
    
if __name__ == "__main__":
    main()