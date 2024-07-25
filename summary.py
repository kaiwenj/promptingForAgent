
from agentPlan import PromptGPT
import openai

class ProbeMemories(object):

    def __init__(self, promptModel, retrievalModel):
        self.promptModel = promptModel
        self.retrievalModel = retrievalModel

    def __call__(self, memory, question):
        retrieval = self.retrievalModel(memory, question)
        prompt = (
            f'Given the following statements, {question}\n'
            f'{retrieval}'
        )
        return self.promptModel(prompt)


class ProbeMemory(object):

    def __init__(self, promptModel):
        self.promptModel = promptModel

    def __call__(self, memory, question):
        prompt = (
            f'Given the following statements, {question}\n'
            f'{memory}'
        )
        return self.promptModel(prompt)



class DescribeCoreCharacteristics(object):

    def __init__(self, promptModel):
        self.promptModel = promptModel

    def __call__(self, name, retrieval, todayDate):
        prompt = (
            f'Today is {todayDate}.\n'
            f'How would one describe {name}\'s core characteristics given the following statements?\n'
            f'{retrieval}'
        )
        return self.promptModel(prompt)


class DescribeDailyOccupation(object):

    def __init__(self, promptModel):
        self.promptModel = promptModel

    def __call__(self, name, retrieval, todayDate):
        prompt = (
            f'Today is {todayDate}.\n'
            f'What is {name}\'s current daily occupation given the following statements?\n'
            f'{retrieval}'
        )
        return self.promptModel(prompt)


class DescribeRecentProgress(object):

    def __init__(self, promptModel):
        self.promptModel = promptModel

    def __call__(self, name, retrieval, todayDate):
        prompt = (
            f'Today is {todayDate}.\n'
            f'How does {name} feel about their recent progress in life given the following statements?\n'
            f'{retrieval}'
        )
        return self.promptModel(prompt)


class GenerateSummary(object):

    def __init__(self, coreCharacteristicsModel, dailyOccupationModel, recentProgressModel):
        self.coreCharacteristicsModel = coreCharacteristicsModel
        self.dailyOccupationModel = dailyOccupationModel
        self.recentProgressModel = recentProgressModel

    def __call__(self, name, age, traits, retrieval, todayDate):
        core_characteristics = self.coreCharacteristicsModel(name, retrieval, todayDate)
        daily_occupation = self.dailyOccupationModel(name, retrieval, todayDate)
        recent_progress = self.recentProgressModel(name, retrieval, todayDate)

        summary = (
            f"Summary for {name}, {age} years old, with traits: {traits}.\n\n"
            f"Core Characteristics:\n{core_characteristics}\n\n"
            f"Current Daily Occupation:\n{daily_occupation}\n\n"
            f"Feelings about Recent Progress:\n{recent_progress}"
        )

        return summary


def main():
    keys_file = open("/Users/stephanie/Documents/Gao Lab/openai/key.txt")  # api-key file
    lines = keys_file.readlines()
    api_key = lines[0].rstrip()

    client = openai.OpenAI(api_key=api_key)
    model = 'gpt-3.5-turbo'

    promptingDictionary = {'gpt-3.5-turbo': PromptGPT}
    promptModel = promptingDictionary[model](client, model)

    coreCharacteristicsModel = DescribeCoreCharacteristics(promptModel)
    dailyOccupationModel = DescribeDailyOccupation(promptModel)
    recentProgressModel = DescribeRecentProgress(promptModel)

    generateSummary = GenerateSummary(coreCharacteristicsModel, dailyOccupationModel, recentProgressModel)

    name = "Eddy Lin"
    age = 21
    traits = "friendly, outgoing, hospitable"
    retrieval = [
        "Eddy is a student at the Oak Hill College studying music theory and composition",
        "Eddy is working on a new music composition and loves exploring different musical styles",
        "Eddy attends classes at Oak Hill College",
        "Eddy spends a significant amount of time on his music composition project",
        "Eddy is excited about his new composition but feels he needs to dedicate more hours to it",
        "Eddy is always looking for ways to expand his knowledge in music theory"
    ]
    todayDate = "Wednesday February 13"

    summary = generateSummary(name, age, traits, retrieval, todayDate)
    print(summary)


if __name__ == "__main__":
    main()
