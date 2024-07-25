
import openai
from agentPlan import PromptGPT, GenerateDayPlan

class React(object):

    def __init__(self, promptModel):
        self.promptModel=promptModel

    def __call__(self, name, dateTime, status, observation, context):
        prompt=f"It is {dateTime}.\n{name}'s status: {status}\nObservation: {observation}\nSummary of relevant context from {name}'s memory: {context}.\nShould {name} react to the observation, and if so, what should be an appropriate reaction? Please use only one sentence."
        reaction = self.promptModel(prompt)
        return reaction


class Replan(object):

    def __init__(self, promptModel):
        self.promptModel=promptModel

    def __call__(self, name, dateTime, plans, observation, context, reaction):
        prompt=f"It is {dateTime}.\n{name}'s plan for the day is: {plans}\nObservation: {observation}\nSummary of relevant context from {name}'s memory: {context}.\n{name}'s reaction to the observation: {reaction}.\nShould {name} replan to the observation, and if so, please help plan in the format of start time: plan."
        replan = self.promptModel(prompt)
        return replan


def main():

    keys_file = open("keys.txt") # api-key file
    lines = keys_file.readlines()
    api_key = lines[0].rstrip()

    client = openai.OpenAI(api_key=api_key)
    model = 'gpt-3.5-turbo'

    promptingDictionary={'gpt-3.5-turbo': PromptGPT}
    promptModel=promptingDictionary[model](client, model)

    generateDayPlan=GenerateDayPlan(promptModel)

    name = "Eddy Lin"
    traits = "friendly, outgoing, hospitable"
    summaryRecentExperience = "Eddy Lin is a student at Oak Hill College studying music theory and composition. He loves to explore different musical styles and is always looking for ways to expand his knowledge. Eddy Lin is working on a composition project for his college class. He is taking classes to learn more about music theory. Eddy Lin is excited about the new composition he is working on but he wants to dedicate more hours in the day to work on it in the coming days"
    summaryPreviousDay = "On Tuesday February 12, Eddy 1) woke up and completed the morning routine at 7:00 am, 2) went to Oak Hill College to take classes starting 10:00 am, 3) had lunch at 11:00 am, 4) worked on his new music composition from 1:00 pm to 5:00 pm, 5) got ready to sleep around 10 pm."
    todayDate="Wednesday February 13"

    dayPlan=generateDayPlan(name, traits, summaryRecentExperience, summaryPreviousDay, todayDate)
    print(dayPlan)

    dateTime = "Wednesday February 13, 4:56 pm"
    status = "John is back home early from work"
    observation = "John saw Eddy taking a short walk around his workplace."
    context = "Eddy Lin is John Lin's son. Eddy Lin has been working on a music composition for his class. Eddy Lin likes to walk around the garden when he is thinking about or listening to music."

    react=React(promptModel)
    reaction = react("John Lin", dateTime, status, observation, context)
    print('Reaction:', reaction)

    statusEddy = "Eddy is working on his music composition."
    observationEddy = reaction
    observationEddy2 = "John Lin asks Eddy to help with cooking dinner"
    observationEddy3 = "John Lin told Eddy that her music teacher wants to discuss the composition at 7:00 pm"
    reactionEddy = react("Eddy Lin", dateTime, statusEddy, observationEddy3, context)
    print('Eddy Reaction:', reactionEddy)

    replan=Replan(promptModel)
    changedPlan = replan("Eddy Lin", dateTime, dayPlan, observationEddy3, context, reactionEddy)

    print("updatedPlan: ", changedPlan)

if __name__=="__main__":
    main()