Python History Quiz CLI 📜

A text-based interactive quiz game built with Python. This program tests your knowledge on major historical events including World War I, World War II, and the Cold War using a randomized question engine.

🚀 Features

Multiple Topics: Choose between World War I, World War II, and the Cold War.

Randomized Questions: Each topic has a pool of 10 questions, but the game randomly selects 5 unique questions per session. No two games are exactly the same!

Simple Logic: Built using easy-to-understand if/elif statements and loops.

Score Tracking: Calculates and displays your final score out of 5 at the end of the round.

Input Validation: Checks user answers against a pre-defined key.

🛠️ How It Works

The code uses the Python random library to ensure variety in gameplay without complex databases.

Topic Selection: The user selects a topic (e.g., WW1, WW2).

Random Sampling: The script uses random.sample([1...10], 5) to generate a list of 5 unique numbers from 1 to 10.

Question Retrieval: The code iterates through these 5 numbers. It uses a structure of if/elif statements to identify which question ID corresponds to which text question.

Scoring: If the user inputs the correct option (a, b, or c), the score variable increments by 1.

📋 Topics Included

World War 1: Covers trenches, treaties, and assassinations.

World War 2: Covers D-Day, the Pacific theater, and key leaders.

Cold War: Covers the Space Race, Cuban Missile Crisis, and the Berlin Wall.

Indo-Pakistan Wars: (Feature currently in development/Coming Soon).

💻 Requirements

Python 3.x

▶️ How to Run

Clone this repository or download the .py file.

Open your terminal or command prompt.

Navigate to the folder containing the file.

Run the following command:

python history_quiz.py


📝 Code Example

The core logic for picking questions looks like this:

# Selects 5 unique numbers from a pool of 10
questions = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)

for q in questions:
    if q == 1:
        # Print Question 1 logic...
    elif q == 2:
        # Print Question 2 logic...


🤝 Contributing

Feel free to fork this repository and add new topics or expand the question pool!
