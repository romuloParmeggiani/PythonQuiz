#
# --- Quiz classes section ---
#

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correctCount = 0
        self.totalPoints = 0

    def printHeader(self):
        print("\n************************************")
        print(f"Quiz name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Questions: {len(self.questions)}")
        print(f"Total points: {self.totalPoints}")
        print("************************************\n")

    def printResults(self):
        print("\n***************************")
        print("***************************\n")

    def takeQuiz(self):
# Initializes the quiz, cleaning all previous scores, answers, etc.
        self.score = 0
        self.correctCount = 0
        for q in self.questions:
            q.isCorrect = False

        self.printHeader()

# Iterates through all questions of selected quiz.
        for q in self.questions:
            q.ask()
            if (q.isCorrect):
                self.correctCount += 1
                self.score += q.points
        return(self.score, self.correctCount, self.totalPoints)

#
# --- Question classes section ---
#

# A function to check if provided response input is valid.
def isValidResponse(Question, response):
    if len(response) == 0:
        print("Response cannot be empty, please try again")
        return False
    elif isinstance(Question, QuestionTrueOrFalse):
        response = response.capitalize()
        if response[0] != "T" and response[0] != "F":
            print(f"Invalid input: {response}, please try again")
            return False
    return True

# A simple check validation if provided response is correct.
# It mark it as True or False afterwards on given question.
def isCorrectResponse(Question, response):
    if response.capitalize() == Question.correctAnswer:
        return True
    else: return False

# The base class for the Questions model.
# It will have the attributes that all extending variations inherit.
# These being: Points, CorrectAnswer, Text.
# And finally if it has been responded correctly or not.
class Question:
    def __init__(self):
        self.points = 0
        self.correctAnswer = ""
        self.text = ""
        self.isCorrect = False

# True or False variation of the base Question class.
class QuestionTrueOrFalse(Question):
    def __init__(self):
        super().__init__()
    
    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("Selection: ")
            if (isValidResponse(self, response) != True):
                continue
            self.isCorrect = isCorrectResponse(self, response)
            break


# Multiple Choice variation of the base Question class.
class QuestionMultiChoice(Question):
    def __init__(self):
        super().__init__()
        self.answers = []
    
    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response = input("Selection: ")
            if (isValidResponse(self, response) != True):
                continue
            self.isCorrect = isCorrectResponse(self, response)
            break

# The base Answers class to be used in conjuction of Multiple Choice.
class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

if __name__ == "__main__":
    qz = Quiz()
    qz.name = "Sample Quiz"
    qz.description = "This is a sample quiz!"

    q1 = QuestionTrueOrFalse()
    q1.text = "\nBroccoli is good for you"
    q1.points = 5
    q1.correctAnswer = "T"
    qz.questions.append(q1)

    q2 = QuestionMultiChoice()
    q2.text = "\nWhat is the sum of 2+2?"
    q2.points = 10
    q2.correctAnswer = "B"
    ans = Answer()
    ans.name = "A"
    ans.text = "3"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "B"
    ans.text = "4"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "C"
    ans.text = "5"
    q2.answers.append(ans)
    qz.questions.append(q2)

    qz.totalPoints = q1.points + q2.points
    result = qz.takeQuiz()
    print(f"\nResults:")
    print(result)