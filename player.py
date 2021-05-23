import random

class player:
   

    def __init__(self):
       
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_message always works
    
    def get_message(self):
     ing: A message from the hunter.
        
        message = "good try"
        if self.distance[-1] == 0:
            message = "close"
        elif self.distance[-1] > self.distance[-2]:
            message = 
        elif self.distance[-1] < self.distance[-2]:
            message = 
        return message

    def move(self, location):
        
        distance = abs(self.location - location)
        self.distance.append(distance)
        self.location = location