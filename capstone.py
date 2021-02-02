Scores = [0,0,0,0,0,0,0,0,0,0]
Questions = ["What is the process of reducing complexity to enable the creation of an efficient set of rules that can be programmed?",
            "Which subroutine doesn't return a value",
            "What is something that stays the same while a program is running",
            "What is something that changes while a program is running?",
            "What is the process of  breaking down everything into the steps needed to become a computer program?",
            "What is the term used to describe loops or repetition in a program?",
            "Which subroutine returns a value?",
            "Which data type has a true or false value",
            "What is a diagrammatic representation of a algorithm?",
            "Which program development cycle is linear, where each stage is fully completed before the next begins?"]
Answers = ["abstraction", "procedure", "constant", "variable", "decomposition", "iteration", "function", "boolean", "flowchart", "waterfall"]
def AnswerQuestion(QuestionNumber):
    print(f"{QuestionNumber + 1}: {Questions[QuestionNumber]}", )
    Answer = input("Answer:")
    return Answer
def MarkQuestion(Answer, QuestionNumber):
    correctanswer = Answers[QuestionNumber]
    Answer = Answer.lower()
    if Answer == correctanswer:
        print(f"You got question {QuestionNumber + 1} correct!")
        Scores[QuestionNumber] = 1
    else:
        print(f"You got question {QuestionNumber + 1} wrong, as your answer was '{Answer}', while the correct answer was '{correctanswer}'")
def SaveHighScore(Scores):
    Score = sum(Scores)
    x = 0
    with open("highscores.txt","r") as whole_file:
        for line in whole_file:
            if Score > int(line):
                x = 1
                Score = str(Score)
                print(f"You have a new high score of {Score}. Your previous high score was {int(line)}")
    if x == 1:
        with open("highscores.txt", "w") as new_file:
                new_file.write(Score)
for n in range(0, 10):
    answer = AnswerQuestion(n)
    MarkQuestion(answer, n)
SaveHighScore(Scores)
