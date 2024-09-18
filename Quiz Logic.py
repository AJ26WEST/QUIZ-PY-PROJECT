def take_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        answer = input("Your answer: ").strip().upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
    return score
