def give_feedback(score, total):
    percentage = (score / total) * 100
    if percentage == 100:
        print("Perfect score! You're a genius!")
    elif percentage >= 75:
        print("Great job! You did well.")
    elif percentage >= 50:
        print("Not bad, but you can improve.")
    else:
        print("Keep trying! Practice makes perfect.")
