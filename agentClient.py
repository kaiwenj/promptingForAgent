
from reflection import parse, AskQuestions, ReflectOneQuestion
from retrieval import MemoryObject, calculateRecencyScore, getGPTEmbedding, CalculateRelevanceScore, RetrieveMemories, memoriesToString
from summary import ProbeMemories, ProbeMemory
from agentPlan import GenerateDayPlan, DividePlanInNMins, breakPlanString
from reactChangePlan import React, Replan

import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import openai
from agentPromptLLM import PromptGPT


def main():

    keys_file = open("keys.txt") # api-key file
    lines = keys_file.readlines()
    api_key = lines[0].rstrip()

    client = openai.OpenAI(api_key=api_key)
    model = 'gpt-3.5-turbo'

    promptingDictionary = {'gpt-3.5-turbo': PromptGPT}
    promptModel = promptingDictionary[model](client, model)

    memoryDecayFactor=0.995
    calculateMemoryRecencyScore=lambda memory: calculateRecencyScore(memory.lastAccessTime, memoryDecayFactor)

    calculateMemoryImportanceScore=lambda memory: memory.importance

    getEmbedding=lambda text: getGPTEmbedding(client, text, model="text-embedding-ada-002")
    calculateMemoryRelevanceScore=lambda memory, query: CalculateRelevanceScore(getEmbedding)(memory.description, query)
    
    recencyWeight=1
    importanceWeight=1
    relevanceWeight=1

    calculateFinalScore=lambda memory, query: recencyWeight * calculateMemoryRecencyScore(memory) + importanceWeight * calculateMemoryImportanceScore(memory) + relevanceWeight * calculateMemoryRelevanceScore(memory, query)

    retrieveMemories=RetrieveMemories(calculateFinalScore)

    memoryStream=[]
    memoryStream.append(MemoryObject("2023-02-13 20:00:00, Isabella Rodriguez attended a local art exhibit.", 6))
    memoryStream.append(MemoryObject("2023-02-13 20:30:00, Isabella Rodriguez met a renowned artist at the exhibit.", 8))
    memoryStream.append(MemoryObject("2023-02-13 21:00:00, Isabella Rodriguez had a deep conversation about modern art with the artist.", 9))
    memoryStream.append(MemoryObject("2023-02-14 09:00:00, Isabella Rodriguez went for a morning jog in the park.", 5))
    memoryStream.append(MemoryObject("2023-02-14 10:00:00, Isabella Rodriguez had a business meeting with potential investors.", 10))
    memoryStream.append(MemoryObject("2023-02-14 12:30:00, Isabella Rodriguez visited a friend in the hospital.", 7))
    memoryStream.append(MemoryObject("2023-02-14 14:00:00, Isabella Rodriguez attended a workshop on effective communication.", 8))
    memoryStream.append(MemoryObject("2023-02-14 15:30:00, Isabella Rodriguez volunteered at an animal shelter.", 9))
    memoryStream.append(MemoryObject("2023-02-14 17:00:00, Isabella Rodriguez prepared a presentation for an upcoming conference.", 8))
    memoryStream.append(MemoryObject("2023-02-14 19:00:00, Isabella Rodriguez cooked a special dinner for her family.", 6))
    memoryStream.append(MemoryObject("2023-02-14 20:00:00, Isabella Rodriguez played board games with her family.", 5))
    memoryStream.append(MemoryObject("2023-02-14 21:00:00, Isabella Rodriguez had a video call with an old friend.", 7))
    memoryStream.append(MemoryObject("2023-02-14 22:00:00, Isabella Rodriguez wrote in her journal about the day's events.", 8))
    memoryStream.append(MemoryObject("2023-02-15 08:00:00, Isabella Rodriguez attended a yoga class.", 6))
    memoryStream.append(MemoryObject("2023-02-15 10:00:00, Isabella Rodriguez worked on a freelance project.", 9))
    memoryStream.append(MemoryObject("2023-02-15 12:00:00, Isabella Rodriguez had lunch with a colleague to discuss collaboration.", 8))
    memoryStream.append(MemoryObject("2023-02-15 14:00:00, Isabella Rodriguez participated in a webinar on sustainable living.", 7))
    memoryStream.append(MemoryObject("2023-02-15 16:00:00, Isabella Rodriguez did grocery shopping.", 5))
    memoryStream.append(MemoryObject("2023-02-15 18:00:00, Isabella Rodriguez attended a community town hall meeting.", 8))
    memoryStream.append(MemoryObject("2023-02-15 20:00:00, Isabella Rodriguez watched a documentary on climate change.", 7))
    memoryStream.append(MemoryObject("2023-02-15 22:00:00, Isabella Rodriguez read a book on personal finance.", 8))

    top_n=4

    # query="What type of person does Isabella seem to be?"
    # topMemories = retrieveMemories(memoryStream, query, top_n)
    retrieveModel=lambda query: memoriesToString(retrieveMemories(memoryStream, query, top_n))
    retrievalModel=lambda memoryStream, query: memoriesToString(retrieveMemories(memoryStream, query, top_n))

    numberOfQuestions = 3
    numberOfReflects = 5
    reflectOneQuestion=ReflectOneQuestion(promptModel, retrieveModel, numberOfReflects, parse)
    
    askQuestions=AskQuestions(promptModel, numberOfQuestions, parse)
    questions=askQuestions(memoriesToString(memoryStream))
    print("============== Questions from memory ===================")
    print(questions)

    giveReflection = [reflectOneQuestion(question) for question in questions]
    print("============== Reflections =================")
    print(giveReflection)

    probeMemories=ProbeMemories(promptModel, retrievalModel)
    questionCharacteristic = 'How would one describe the core characteristics of this person? Please only give adjective words.\n'

    probeMemory=ProbeMemory(promptModel)

    print("======== Characteristic ===============")

    answerCharacteristic = probeMemories(memoryStream, questionCharacteristic)
    print(answerCharacteristic)

    todayDate="Saturday February 16"

    questionSummaryRecentExperience='How does this person feel about their recent progress in life given the following statements?\n'
    answerSummaryRecentExperience = probeMemories(memoryStream, questionSummaryRecentExperience) # change to nouns
    print(answerSummaryRecentExperience)

    questionSummaryPreviousDay=f'Today is {todayDate}. Can you summarize what this person did yesterday given the following statements?\n'
    answerSummaryPreviousDay = probeMemory(memoriesToString(memoryStream), questionSummaryPreviousDay)
    print(answerSummaryPreviousDay)

    summaryRecentExperience = "Eddy Lin is a student at Oak Hill College studying music theory and composition. He loves to explore different musical styles and is always looking for ways to expand his knowledge. Eddy Lin is working on a composition project for his college class. He is taking classes to learn more about music theory. Eddy Lin is excited about the new composition he is working on but he wants to dedicate more hours in the day to work on it in the coming days"
    summaryPreviousDay = "On Tuesday February 12, Eddy 1) woke up and completed the morning routine at 7:00 am, 2) went to Oak Hill College to take classes starting 10:00 am, 3) had lunch at 11:00 am, 4) worked on his new music composition from 1:00 pm to 5:00 pm, 5) got ready to sleep around 10 pm."
    name='Isabella Rodriguez'

    generateDayPlan=GenerateDayPlan(promptModel)
    dayPlan=generateDayPlan(name, answerCharacteristic, answerSummaryRecentExperience, answerSummaryPreviousDay, todayDate)
    print(dayPlan)

    plans=breakPlanString(dayPlan)

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

    dateTime = "Saturday February 16, 2:56 pm"
    status = "Isabella is relaxing in the botanical garden"
    observation = "Isabella saw a beautiful orchid."
    context = answerSummaryRecentExperience

    react=React(promptModel)
    reaction = react(name, dateTime, status, observation, context)
    print('Reaction:', reaction)

    replan=Replan(promptModel)
    changedPlan = replan(name, dateTime, dayPlan, observation, context, reaction)
    print("updatedPlan: ", changedPlan)

if __name__=="__main__":
    main()


# create agent (background story)
# observation -> agent -> actions
# different pieces reacting to observation
# create and update memories

# dialogue -> joint action




