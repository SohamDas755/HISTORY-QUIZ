# 📚 History Quiz Program

A simple, command-line multiple-choice quiz written in Python to test knowledge of major 20th-century historical conflicts.

## ✨ Features

* **Topic Selection:** Users can choose between **World War I** and **World War II** quizzes.
* **Multiple-Choice:** Each quiz features 5 questions with 3 options.
* **Scoring:** Tracks correct answers and provides a final score out of 5.
* **Immediate Feedback:** Indicates whether the user's answer was correct or wrong after each question.

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3** installed on your system to run this program.

### Installation and Execution

1.  **Clone the Repository (If on GitHub):**
    ```bash
    git clone [Your Repository URL]
    cd history-quiz-program
    ```
    *(If not on GitHub, simply save the code as `history_quiz.py`.)*

2.  **Run the Quiz:**
    Open your terminal or command prompt in the directory where the file is saved and execute:
    ```bash
    python history_quiz.py
    ```

3.  **Start Quizzing:**
    Follow the prompts to select your topic and enter your answers (e.g., `a`, `b`, or `c`).

---

## 💻 Program Structure

The quiz is currently structured using `if/elif` statements in a single script:

1.  **Topic Selection:** The program first asks the user to choose a topic (`a`, `b`, `c`, or `d`).
2.  **Quiz Execution:** Based on the choice:
    * If 'a' (World War I), it runs the WW1 quiz logic.
    * If 'b' (World War II), it runs the WW2 quiz logic.
    * If 'c' or 'd', it prints a "COMING SOON" message.
3.  **Scoring:** A `score` variable is incremented for every correct answer.
4.  **Result:** The final score is printed to the console.

### World War I Sample Question Logic

```python
# Example of the logic used for World War I questions:
print("1. WHAT IS THE NAME OF THE DISASTROUS CAMPAIGN...")
ans = input("YOUR ANSWER (a/b/c): ")
if ans == "b":
    print("CORRECT")
    score = score + 1
💡 Future Enhancements
The following features are planned for future updates:

Quiz Expansion: Add full quizzes for Indo-Pakistan Wars (c) and Cold War (d).

Data Structure: Refactor the questions and answers into a more maintainable structure (e.g., a list of dictionaries) to make adding new quizzes easier.

Input Robustness: Implement better error handling for invalid input (e.g., non-letter characters or letters not in the options).

Case Insensitivity: Allow users to input answers in uppercase or lowercase.

🤝 Contributing
Contributions are welcome! If you have suggestions for new questions, better code structure, or bug fixes, please open an issue or submit a pull request.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License
Distributed under the MIT License. See LICENSE.md for more information.
else:
    print("WRONG")
