import random

puzzles = [
    # 🟦 Color-Pattern: Easy → Hard
    {
        "question": "What comes next? 🟥 🟦 🟥 🟦",
        "options": ["🟥", "🟩", "🟨"],
        "answer": "🟥",
        "category": "color-pattern",
        "difficulty": "easy"
    },
    {
        "question": "🟥 + 🟦 = ?",
        "options": ["🟪", "🟧", "🟨"],
        "answer": "🟪",
        "category": "color-pattern",
        "difficulty": "easy"
    },
    {
        "question": "🟦🟥🟩🟦🟥🟩... What comes next?",
        "options": ["🟦", "🟩", "🟥"],
        "answer": "🟦",
        "category": "color-pattern",
        "difficulty": "easy"
    },
    {
        "question": "🔺🟦🔺🟩🔺🟨🔺...",
        "options": ["🟦", "🟥", "🟧"],
        "answer": "🟧",
        "category": "color-pattern",
        "difficulty": "medium"
    },
    {
        "question": "🟦🟧🟩🟦🟧...?",
        "options": ["🟧", "🟦", "🟩"],
        "answer": "🟩",
        "category": "color-pattern",
        "difficulty": "medium"
    },
    {
        "question": "🔴🔴🟠🔴🔴🟠... What comes next?",
        "options": ["🟠", "🔴", "🟡"],
        "answer": "🔴",
        "category": "color-pattern",
        "difficulty": "medium"
    },
    {
        "question": "🟩🟩🟥🟩🟩🟥... What comes next?",
        "options": ["🟩", "🟥", "🟨"],
        "answer": "🟩",
        "category": "color-pattern",
        "difficulty": "hard"
    },
    {
        "question": "🟨🟨🟥🟨🟨🟥...",
        "options": ["🟨", "🟥", "🟩"],
        "answer": "🟨",
        "category": "color-pattern",
        "difficulty": "hard"
    },

    # 🔢 Sequence: Easy → Medium
    {
        "question": "2, 4, 6, 8, ...",
        "options": ["10", "12", "9"],
        "answer": "10",
        "category": "sequence",
        "difficulty": "easy"
    },
    {
        "question": "1, 2, 4, 8, ...",
        "options": ["16", "12", "10"],
        "answer": "16",
        "category": "sequence",
        "difficulty": "easy"
    },
    {
        "question": "🟥 + 🟨 = ?",
        "options": ["🟧", "🟪", "🟩"],
        "answer": "🟧",
        "category": "color-pattern",
        "difficulty": "easy"
    },
    {
        "question": "1, 3, 5, 7, ...",
        "options": ["9", "10", "11"],
        "answer": "9",
        "category": "sequence",
        "difficulty": "easy"
    },
    {
        "question": "If 1 = A, 2 = B, then 3 = ?",
        "options": ["C", "D", "E"],
        "answer": "C",
        "category": "sequence",
        "difficulty": "easy"
    },
    {
        "question": "5, 10, 20, 40, ...",
        "options": ["60", "80", "100"],
        "answer": "80",
        "category": "sequence",
        "difficulty": "medium"
    },
    {
        "question": "11, 22, 33, 44, ...",
        "options": ["55", "66", "77"],
        "answer": "55",
        "category": "sequence",
        "difficulty": "medium"
    },
    {
        "question": "3, 6, 12, 24, ...",
        "options": ["36", "48", "30"],
        "answer": "48",
        "category": "sequence",
        "difficulty": "medium"
    },
    {
        "question": "13, 26, 52, ...",
        "options": ["65", "78", "104"],
        "answer": "104",
        "category": "sequence",
        "difficulty": "hard"
    },
    {
        "question": "7, 14, 28, ...",
        "options": ["35", "56", "42"],
        "answer": "56",
        "category": "sequence",
        "difficulty": "hard"
    },

    # 📐 Spatial: Easy → Hard
    {
        "question": "Which doesn't belong? 🔺 🔵 🟨 🟥",
        "options": ["🔺", "🔵", "🟥"],
        "answer": "🔺",
        "category": "spatial",
        "difficulty": "easy"
    },
    {
        "question": "Which shape doesn’t fit? 🔺 🔻 🔸 🟣",
        "options": ["🔻", "🟣", "🔸"],
        "answer": "🟣",
        "category": "spatial",
        "difficulty": "easy"
    },
    {
        "question": "Which doesn't belong? 🟨 🟧 🟥 🦊",
        "options": ["🦊", "🟥", "🟧"],
        "answer": "🦊",
        "category": "spatial",
        "difficulty": "easy"
    },
    {
        "question": "Odd one out? 🟫 🔵 🟪 🟣",
        "options": ["🟫", "🔵", "🟪"],
        "answer": "🟫",
        "category": "spatial",
        "difficulty": "medium"
    },
    {
        "question": "Odd one out? 🟥 🔺 🔴 🟧",
        "options": ["🔺", "🟧", "🔴"],
        "answer": "🔺",
        "category": "spatial",
        "difficulty": "medium"
    },
    {
        "question": "Odd one out? ◼️ 🟧 🔵 🟥",
        "options": ["🟥", "🟧", "◼️"],
        "answer": "◼️",
        "category": "spatial",
        "difficulty": "hard"
    },
    {
        "question": "Which doesn't belong? ⬜ ⬛ 🔲 🔳",
        "options": ["⬛", "🔲", "⬜"],
        "answer": "⬜",
        "category": "spatial",
        "difficulty": "hard"
    },

    # 🧠 Reasoning: Easy → Hard
    {
        "question": "😁 + 😁 = 🤣 ...so what is 😞 + 😞 ?",
        "options": ["😭", "😡", "😴"],
        "answer": "😭",
        "category": "reasoning",
        "difficulty": "easy"
    },
    {
        "question": "🐶 is to 🐾 as 🐦 is to ?",
        "options": ["🐣", "🐥", "🪶"],
        "answer": "🪶",
        "category": "reasoning",
        "difficulty": "easy"
    },
    {
        "question": "If 🌞 = day and 🌙 = night, then 🌧️ = ?",
        "options": ["cloudy", "rain", "wet"],
        "answer": "rain",
        "category": "reasoning",
        "difficulty": "easy"
    },
    {
        "question": "🟥 + 🟦 = 🟪\nSo 🟨 + 🟥 = ?",
        "options": ["🟧", "🟩", "⬛"],
        "answer": "🟧",
        "category": "reasoning",
        "difficulty": "medium"
    },
    {
        "question": "👨‍👩‍👧 + 👶 = ?",
        "options": ["👨‍👩‍👧‍👦", "👨‍👧", "👨‍👩‍👦"],
        "answer": "👨‍👩‍👧‍👦",
        "category": "reasoning",
        "difficulty": "medium"
    },
    {
        "question": "If 🐛 becomes 🦋 and 🐣 becomes 🐓, then 🐸 becomes...?",
        "options": ["🧍", "🐊", "🪰"],
        "answer": "🧍",
        "category": "reasoning",
        "difficulty": "hard"
    },
    {
        "question": "🧊 melts into 💧, 💧 heats into 🌫️, 🌫️ condenses into...?",
        "options": ["💧", "🔥", "🧊"],
        "answer": "💧",
        "category": "reasoning",
        "difficulty": "hard"
    },
    {
        "question": "Which doesn’t belong? 🔷 🔹 🔸 🔺",
        "options": ["🔺", "🔷", "🔸"],
        "answer": "🔺",
        "category": "spatial",
        "difficulty": "hard"
    },

    # 🤯 Mind-Bender: Medium → Hard
    {
        "question": "What came first? 🐓 or 🥚?",
        "options": ["🐓", "🥚", "🤷🏾‍♂️"],
        "answer": "🤷🏾‍♂️",
        "category": "reasoning",
        "difficulty": "hard"
    }
]

class EchoLogicGame:

    def __init__(self):
        self.level = 1
        self.streak = 0
        self.misses = 0
        self.last_puzzle = None
        self.used_puzzles = []

    def get_difficulty(self):
        if self.level <= 1:
            return "easy"
        elif self.level == 2:
            return "medium"
        else:
            return "hard"

    def get_puzzle(self):
        difficulty = self.get_difficulty()
        candidates = [p for p in puzzles if p["difficulty"] == difficulty and p not in self.used_puzzles]

        if not candidates:
            self.used_puzzles = []
            candidates = [p for p in puzzles if p["difficulty"] == difficulty]

        puzzle = random.choice(candidates)
        self.used_puzzles.append(puzzle)
        self.last_puzzle = puzzle
        return puzzle

    def check_answer(self, puzzle, player_input):
        try:
            selected = puzzle["options"][player_input]
            if selected == puzzle["answer"]:
                self.streak += 1
                self.misses = 0
                return True, "✅ Correct!"
            else:
                self.streak = 0
                self.misses += 1
                return False, f"❌ Wrong! The correct answer was: {puzzle['answer']}"
        except:
            return False, "⚠️ Invalid input."

    def update_level(self):
        message = ""
        if self.streak >= 3:
            self.level += 1
            self.streak = 0
            message = "⬆️ Level Up!"
        elif self.misses >= 2 and self.level > 1:
            self.level -= 1
            self.misses = 0
            message = "⬇️ Level Down... Keep going!"
        return message