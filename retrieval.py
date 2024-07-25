import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import openai
from agentPlan import PromptGPT


class MemoryObject(object):

    def __init__(self, description, importance):
        self.description = description
        self.creationTime = time.time()
        self.lastAccessTime = self.creationTime
        self.importance = importance

    def updateAccessTime(self, time):
        self.lastAccessTime = time 




def calculateRecencyScore(lastAccessTime, decayFactor):
    currentTime=time.time()
    hoursSinceLastAccess=(currentTime - lastAccessTime) / 3600
    recencyScore=np.exp(- decayFactor * hoursSinceLastAccess)
    return recencyScore

def getGPTEmbedding(client, text, model="text-embedding-ada-002"):
    return client.embeddings.create(input=[text], model=model).data[0].embedding

class CalculateRelevanceScore(object):

    def __init__(self, getEmbedding):
        self.getEmbedding=getEmbedding

    def __call__(self, text, query):
        textEmbedding = self.getEmbedding(text)
        queryEmbedding = self.getEmbedding(query)
        similarity = cosine_similarity([textEmbedding], [queryEmbedding])
        return similarity[0][0]   



class RetrieveMemories(object):

    def __init__(self, calculateFinalScore):
        self.calculateFinalScore=calculateFinalScore

    def __call__(self, memoryStream, query, top_n):
        scoredMemories = [(index, self.calculateFinalScore(memory, query)) for index, memory in enumerate(memoryStream)]
        scoredMemories.sort(key=lambda x: x[1], reverse=True)
        topMemories = [memoryStream[index] for index, score in scoredMemories[:int(top_n)]]
        accessTime=time.time()
        for memory in topMemories:
            memory.updateAccessTime(accessTime)
        return topMemories


def memoriesToString(memories):
    return "\n".join([memory.description for memory in memories])




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



    query="What type of person does Isabella seem to be?"
    x = retrieveMemories(memoryStream, query, top_n)
    y=[memory1.description for memory1 in x]
    print(y)

    

    






