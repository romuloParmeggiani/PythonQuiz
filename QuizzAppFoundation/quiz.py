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

def isCorrectResponse(Question, response):
    if response.capitalize() == Question.correctAnswer:
        return True
    else: return False

class Question:
    def __init__(self):
        self.points = 0
        self.correctAnswer = ""
        self.text = ""
        self.isCorrect = False

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

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

if __name__ == "__main__":
    q1 = QuestionTrueOrFalse()
    q1.text = "Broccoli is good for you"
    q1.points = 5
    q1.correctAnswer = "T"
    q1.ask()
    q2 = QuestionMultiChoice()
    q2.text = "What is 2+2?"
    q2.points = 10
    q2.correctAnswer = "B"
    ans = Answer()
    ans.name = "A"
    ans.text = "3"
    q2. answers.append(ans)
    ans = Answer()
    ans.name = "B"
    ans.text = "4"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "C"
    ans.text = "5"
    q2.answers.append(ans) 
    q2.ask()
    print(q1.isCorrect)
    print (q2.isCorrect)