import openai
import re

class PromptGPT(object):

    def __init__(self, client, model):
        self.client=client
        self.model=model

    def __call__(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        return answer

class Plan(object):

    def __init__(self, location, startingTime, duration):
        self.location=location
        self.startingTime=startingTime
        self.duration=duration

class GenerateDayPlan(object):

    def __init__(self, promptModel):
        self.promptModel=promptModel

    def __call__(self, name, traits, summaryRecentExperience, summaryPreviousDay, todayDate):
        prompt=f'Name: {name}\nInnate traits: {traits}\n{summaryRecentExperience}\n{summaryPreviousDay}\nToday is {todayDate}. Here is the plan today in broad strokes: '
        dayPlan=self.promptModel(prompt)
        return dayPlan


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

if __name__=="__main__":
    main()
