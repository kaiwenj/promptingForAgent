
import openai
import re
#from processPlanTime import extractPlanTime


class Plan(object):

    def __init__(self, location, startingTime, duration):
        self.location=location
        self.startingTime=startingTime
        self.duration=duration


class GenerateDayPlan(object):

    def __init__(self, promptModel):
        self.promptModel=promptModel

    def __call__(self, name, traits, summaryRecentExperience, summaryPreviousDay, todayDate):
        prompt=f'Name: {name}\nInnate traits: {traits}\n{summaryRecentExperience}\n{summaryPreviousDay}\nToday is {todayDate}. Here is the plan today in broad strokes. Please only give me answer in the format of starting time: plan. '
        dayPlan=self.promptModel(prompt)
        return dayPlan


class DividePlanInNMins(object):

    def __init__(self, promptModel):
        self.promptModel=promptModel

    def __call__(self, name, memory, startTime, endTime, plan, nextPlan, nMinutes):
        prompt=f"{name} did {memory}, then plans to {plan} at {startTime} and {nextPlan} at {endTime}, can you plan for every {nMinutes} minutes in the interval? Please only give me answer in the format of start time: plan."
        detailedPlan = self.promptModel(prompt)
        return detailedPlan

def breakPlanString(plan):
    splitPlan = re.split('\n', plan)
    plans=[re.split(': ', detailedPlan) for detailedPlan in splitPlan]
    return plans



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

    plans=breakPlanString(dayPlan)

    # while len(splitPlan) == 1:
    #     promptReplan = "Can you plan again?"
    #     replan = promptModel(promptReplan)
    #     splitPlan = re.split('1\) ', replan)

    # splitPlan=splitPlan[1]

    # while True:
    #     splitPlan = re.split(f'{i}\) ', splitPlan)
    #     if len(splitPlan) == 1:
    #         break
    #     plan = splitPlan[0]
    #     planTuple = extractPlanTime(plan)
    #     while planTuple == None or planTuple[1].replace(' ','').isalpha():
    #         promptSpecifyTime = "Please add the starting time in the day for "+plan+". Please only give me answer in the format of time: plan."
    #         timeSpecifiedAnswer = promptModel(promptSpecifyTime)
    #         planTuple = (plan, timeSpecifiedAnswer)
    #     plans.append(planTuple)
    #     splitPlan=splitPlan[1]
    #     i=i+1
    
    dividePlanInNMins=DividePlanInNMins(promptModel)
    nMinutes=15
    memory='nothing'
    detailedPlans=[]
    for i in range(len(plans)-1):
        startTime=plans[i][0]
        endTime=plans[i+1][0]
        plan=plans[i][1]
        nextPlan=plans[i+1][1]
        answer=dividePlanInNMins(name, memory, startTime, endTime, plan, nextPlan, nMinutes)
        memory=plan
        detailedPlan=breakPlanString(answer)
        detailedPlans=detailedPlans+detailedPlan
    detailedPlans=detailedPlans+plans[-1]
    
    print(detailedPlans)










if __name__=="__main__":
    main()




