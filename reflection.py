#from typing import Any
from agentPlan import PromptGPT
import openai


def parse(response):
    return response.strip().split('\n') 



class AskQuestions(object):

    def __init__(self, promptModel, numberOfQuestions, parse):
        self.promptModel = promptModel
        self.numberOfQuestions = numberOfQuestions
        self.parse = parse

    def __call__(self, recentMemory): # more specific questions, now too generic, not grounded to unique experience
        questionsPrompt = recentMemory + f"\n\nGiven only the information above, what are {self.numberOfQuestions} most salient high level questions we can answer about the subjects in the statements? Please only give the questions."
        questionsResponse = self.promptModel(questionsPrompt)
        questions = self.parse(questionsResponse)
        return questions


# class Reflect(object):

#     def __init__(self, promptModel, numberOfQuestions, reflectOneQuestion, parse):
#         self.promptModel = promptModel
#         self.numberOfQuestions = numberOfQuestions
#         self.reflectOneQuestion = reflectOneQuestion
#         self.parse = parse

#     def __call__(self, recentMemory):
#         questionsPrompt = recentMemory + f"\n\nGiven only the information above, what are {self.numberOfQuestions} most salient high level questions we can answer about the subjects in the statements? Please only give the questions."
#         questionsResponse = self.promptModel(questionsPrompt)
#         questions = self.parse(questionsResponse)
#         print(questions)
#         reflections = [self.reflectOneQuestion(questions) for question in questions]
#         return questions, reflections


class ReflectOneQuestion(object):

    def __init__(self, promptModel, retrieveModel, numberOfReflects, parse):
        self.promptModel = promptModel
        self.retrieveModel = retrieveModel
        self.numberOfReflects = numberOfReflects
        self.parse=parse

    def __call__(self, question):
        relevantMemories = self.retrieveModel(question)
        reflectPrompt = relevantMemories + f"\n\nWhat {self.numberOfReflects} high-level insights can you infer from the above statements? (example format: insight (because of 1, 5, 3))"
        reflectResponse = self.promptModel(reflectPrompt)
        parsedReflections = self.parse(reflectResponse)
        return parsedReflections


def main():
    api_key = ""
    client = openai.OpenAI(api_key=api_key)
    model = 'gpt-3.5-turbo'

    promptingDictionary = {'gpt-3.5-turbo': PromptGPT}
    promptModel = promptingDictionary[model](client, model)

    exampleRetrieveResult=("Statements about Klaus Mueller\n"
                "1. Klaus Mueller is writing a research paper\n"
                "2. Klaus Mueller enjoys reading a book on gentrification\n"
                "3. Klaus Mueller is conversing with Ayesha Khan about exercising\n")

    retrieveModel = lambda question: exampleRetrieveResult

    numberOfQuestions = 3
    numberOfReflects = 5

    reflectOneQuestion=ReflectOneQuestion(promptModel, retrieveModel, numberOfReflects, parse)

    #reflect = Reflect(promptModel, numberOfQuestions, reflectOneQuestion, parse)

    recentMemory = ("Klaus Mueller is reading a book on gentrification"
                    "Klaus Mueller is conversing with a librarian about his research project"
                    "desk at the library is currently unoccupied")

    askQuestions=AskQuestions(promptModel, numberOfQuestions, parse)
    questions=askQuestions(recentMemory)
    print(questions)

    giveReflection = [reflectOneQuestion(question) for question in questions]
    print(giveReflection)

if __name__ == "__main__":
    main()
