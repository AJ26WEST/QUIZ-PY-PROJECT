def main():
    print("Welcome to the Quiz App!")
    total_questions = len(questions)
    score = take_quiz(questions)
    print(f"Your score: {score}/{total_questions}")
    give_feedback(score, total_questions)

    if input("Do you want to take the quiz again? (yes/no): ").strip().lower() == "yes":
        main()

if __name__ == "__main__":
    main()
