import os

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QUESTIONS_FILE = os.path.join(BASE_DIR, "questions.txt")
SCORES_FILE = os.path.join(BASE_DIR, "scores.txt")


# Create Questions File Automatically
def create_questions_file():

    if not os.path.exists(QUESTIONS_FILE):

        sample_questions = [
            "What is Python?|programming language",
            "What does AI stand for?|artificial intelligence",
            "Which keyword is used to define a function in Python?|def",
            "What symbol is used for comments in Python?|#",
            "Which data type stores whole numbers?|int"
        ]

        with open(QUESTIONS_FILE, "w") as file:
            for question in sample_questions:
                file.write(question + "\n")


# Load Questions
def load_questions():

    questions = []

    with open(QUESTIONS_FILE, "r") as file:

        for line in file:

            parts = line.strip().split("|")

            if len(parts) == 2:
                question = parts[0]
                answer = parts[1]

                questions.append((question, answer))

    return questions


# Save Score
def save_score(name, score, total):

    with open(SCORES_FILE, "a") as file:
        file.write(f"{name} - Score: {score}/{total}\n")


# Main Quiz Function
def run_quiz():

    print("===================================")
    print("     Welcome to AI Quiz Generator")
    print("===================================")

    try:
        name = input("Enter your name: ")
    except:
        name = "Guest"

    create_questions_file()

    questions = load_questions()

    score = 0

    # Quiz Loop
    for index, (question, answer) in enumerate(questions, start=1):

        print(f"\nQuestion {index}:")
        print(question)

        try:
            user_answer = input("Your Answer: ").strip().lower()
        except:
            user_answer = ""

        if user_answer == answer.lower():
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct Answer is:", answer)

    # Final Result
    print("\n===================================")
    print("         FINAL RESULT")
    print("===================================")

    print(f"Player Name : {name}")
    print(f"Final Score : {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100

    print(f"Percentage  : {percentage:.2f}%")

    if percentage >= 80:
        print("Result      : Excellent")
    elif percentage >= 60:
        print("Result      : Good")
    elif percentage >= 40:
        print("Result      : Average")
    else:
        print("Result      : Needs Improvement")

    print("===================================")

    # Save Score
    save_score(name, score, len(questions))

    print("Score saved successfully in scores.txt")

    # Prevent Terminal Closing
    try:
        input("\nPress Enter to close the program...")
    except:
        pass


# Run Program
run_quiz()