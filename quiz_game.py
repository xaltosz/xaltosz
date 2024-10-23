def quiz():
    questions = {
        "What is the capital of France?": {
            "a": "Berlin",
            "b": "Madrid",
            "c": "Paris",
            "d": "Lisbon"
        },
        "What is 2 + 2?": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6"
        },
        "What is the largest planet in our solar system?": {
            "a": "Earth",
            "b": "Jupiter",
            "c": "Mars",
            "d": "Saturn"
        }
    }

    answers = {
        "What is the capital of France?": "c",
        "What is 2 + 2?": "b",
        "What is the largest planet in our solar system?": "b"
    }

    score = 0

    for question, options in questions.items():
        print(question)
        for option, answer in options.items():
            print(f"{option}: {answer}")
        user_answer = input("Your answer (a, b, c, d): ").lower()

        if user_answer == answers[question]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{answers[question]}'.\n")

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()

