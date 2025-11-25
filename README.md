# 📜 Python History Quiz CLI

Test your knowledge of the 20th Century's most defining moments in this interactive, randomized command-line quiz game!

---

## 📖 Table of Contents

- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [How It Works](#how-it-works-the-logic)
- [Topics Included](#topics-included)
- [Getting Started](#getting-started)
- [Code Structure](#code-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## 🧐 About the Project

**History Quiz CLI** is a lightweight educational tool designed for the terminal. This isn’t just another static quiz—you’ll get unique questions each time thanks to dynamic randomization.

Whether you're a history buff or a student cramming for exams, this tool helps you recall key dates, figures, and events from World War I, World War II, and the Cold War.

---

## 🚀 Key Features

- **🔀 Dynamic Randomization**  
  Every topic has a pool of 10 questions. Each session randomly selects 5 unique ones—no two rounds are the same!

- **📊 Live Score Tracking**  
  Get instant feedback for every answer ("CORRECT" or "WRONG") and see your final score at the end (e.g., `4 OUT OF 5`).

- **🛡️ Robust Input Handling**  
  Validates answers (`a`/`b`/`c`/`d`), prevents crashes, and lets you navigate with simple text input.

- **🧠 Beginner-Friendly Codebase**  
  Pure Python, using standard libraries. The logic is transparent and easy to follow.

---

## 🛠️ How It Works (The Logic)

1. **Topic Selection:**  
   Choose a historical era (e.g., World War II).

2. **Random Sampling:**  
   Generates a list of 5 unique IDs between 1-10 (e.g., `[3, 9, 1, 5, 8]`) using `random.sample`.

3. **Question Retrieval:**  
   For each selected ID, the script maps it via `if/elif` to a specific question & answer.

4. **Scoring:**  
   Your score increases with each correct answer!

---

## 📋 Topics Included

| Topic                | Description                                    | Status        |
|----------------------|------------------------------------------------|--------------|
| **World War 1**      | Trench warfare, Versailles, Assassinations     | ✅ Active    |
| **World War 2**      | D-Day, Holocaust, Pacific, Generals            | ✅ Active    |
| **Cold War**         | Space Race, Cuban Missile Crisis, Berlin Wall  | ✅ Active    |
| **Indo-Pakistan Wars** | Conflicts & treaties in South Asia           | 🚧 Coming Soon |

---

## 💻 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

```bash
git clone https://github.com/SohamDas755/HISTORY-QUIZ.git
cd HISTORY-QUIZ
python history_quiz.py
```

---

## 📝 Code Structure

Readability > Complexity. Here’s how questions are chosen and answers checked:

```python
import random

# Select 5 unique questions out of 10
questions = random.sample([1,2,3,4,5,6,7,8,9,10], 5)

for q in questions:
    if q == 1:
        print("QUESTION TEXT HERE...")
        # Check answer
    elif q == 2:
        print("NEXT QUESTION TEXT HERE...")
        # Check answer
    # ... and so on
```

---

## 🗺️ Roadmap

- [ ] **Indo-Pakistan Wars:** Complete this topic.
- [ ] **Play Again:** Restart quiz without exiting.
- [ ] **Leaderboard:** Store high scores locally.
- [ ] **Timer:** Countdown for each question.

---

## 🤝 Contributing

We 🫶 contributions!

- Fork the project
- Create your branch (`git checkout -b feature/AmazingFeature`)
- Commit changes (`git commit -m 'Add AmazingFeature'`)
- Push to branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request

---

## 📄 License

Distributed under the MIT License.  
See `LICENSE.txt` for more information.
