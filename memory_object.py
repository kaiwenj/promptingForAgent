import time

class Memory:
    def __init__(self, content, type):
        if type not in ['plan', 'observation', 'reflection']:
            raise ValueError("Type must be 'plan', 'observation', or 'reflection'")
        
        self.description = content
        self.type = type
        self.creationTime = time.time()
        self.accessedTime = self.creationTime
    
    def getDescription(self):
        self.updateAccessedTime()
        return self.description
    
    def getType(self):
        self.updateAccessedTime()
        return self.type
        
    def updateAccessedTime(self):
        self.accessedTime = time.time()

    def getCreationTime(self):
        self.updateAccessedTime()
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.creationTime))
    
    def getAccessedTime(self):
        self.updateAccessedTime()
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.creationTime))

# Example usage
memory = Memory("Meeting with John about project", "plan")
print(memory.getDescription())  # Should print the description
print(memory.getType())  # Should print the type
print(memory.getCreationTime())  # Should print the creation time
print(memory.getAccessedTime())  # Should print the last accessed time
