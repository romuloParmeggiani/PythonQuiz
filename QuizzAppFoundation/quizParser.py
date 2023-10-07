import xml.sax
from quiz import *
from enum import Enum, unique


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5

# Loads a particular quiz .xml file, parses it, and returns
# a fully-built Quiz object that can then be presented to the user.
class QuizParser(xml.sax.ContentHandler):

    def __init__(self):
        self.newQuiz = Quiz()
        self._parseState = QuizParserState.IDLE
        self._currentQuestion = None
        self._currentAnswer = None

    def parseQuiz(self, quizPath):
        # load the file contents
        quizText = ""
        with open(quizPath, "r") as quizFile:
            if quizFile.mode == "r":
                quizText = quizFile.read()

        xml.sax.parseString(quizText, self)

        # return the finished quiz
        return self.newQuiz

    def startElement(self, tagname, attrs):
        if tagname == "QuizML":
            self._parseState = QuizParserState.PARSE_QUIZ
            self.newQuiz.name = attrs["name"]
        #TODO: process the rest of the tags
        elif tagname == "Description":
            self._parseState = QuizParserState.PARSE_DESCRIPTION
        elif tagname == "Question":
            self._parseState = QuizParserState.PARSE_QUESTION
            if attrs["type"] == "multiChoice":
                self._currentQuestion = QuestionMultiChoice()
            elif attrs["type"] == "trueOrFalse":
                self._currentQuestion = QuestionTrueOrFalse()
            self._currentQuestion.points = int(attrs["points"])
            self.newQuiz.totalPoints += self._currentQuestion.points
        elif tagname == "QuestionText":
            self._parseState = QuizParserState.PARSE_QUEST_TEXT
            self._currentQuestion.correctAnswer = attrs["answer"]
        elif tagname == "Answer":
            self._currentAnswer = Answer()
            self._currentAnswer.name = attrs["name"]
            self._parseState = QuizParserState.PARSE_ANSWER
                        

    def endElement(self, tagname):
        if tagname == "QuizML":
            self._parseState = QuizParserState.IDLE
        #TODO: process the rest of the tags
        elif tagname == "Description":
            self._parseState = QuizParserState.PARSE_QUIZ
        elif tagname == "Question":
            self.newQuiz.questions.append(self._currentQuestion)
            self._parseState = QuizParserState.PARSE_QUIZ
        elif tagname == "QuestionText":
            self._parseState = QuizParserState.PARSE_QUESTION
        elif tagname == "Answer":
            self._currentQuestion.answers.append(self._currentAnswer)
            self._parseState = QuizParserState.PARSE_QUESTION

    def characters(self, chars):
        if self._parseState ==  QuizParserState.PARSE_DESCRIPTION:
            self.newQuiz.description += chars
        elif self._parseState == QuizParserState.PARSE_QUEST_TEXT:
            self._currentQuestion.text += chars
        elif self._parseState == QuizParserState.PARSE_ANSWER:
            self._currentAnswer.text += chars


if __name__ == "__main__":
    app = QuizParser()
    qz = app.parseQuiz("Quizzes/MyQuiz.xml")
    print(qz.name)
    print(qz.description)
    print(len(qz.questions))
    print(qz.totalPoints)
    for q in qz.questions:
        print(q.text)