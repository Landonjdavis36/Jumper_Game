import random

class Rabbit:
    """A code template for a cute little fuzzy-tailed animal. The 
    responsibility of this class of objects is to watch the hunter and give 
    hints.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Rabbit (1-1000).
        distance (list): The distance from the hunter.
    """

    def __init__(self):
        
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_hint always works
    
    def get_hint(self):
        tring: A hint for the player.
       
        hint = 
        if self.distance[-1] == 0:
            hint = 
        elif self.distance[-1] > self.distance[-2]:
            hint = 
        elif self.distance[-1] < self.distance[-2]:
            hint =
        
    def watch(self, location):
       

        Args:
            self (player): An instance of player.
        
        distance = abs(self.location - location)
        self.distance.append(distance)