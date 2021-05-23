from game.console import Console
from game.player import Hunter
from game.jumper import Rabbit

class Director:
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.player = player()
        self.keep_playing = True
        self.jumper = jumper()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        message = self.hunter.get_message()
        self.console.write(message)
        location = self.console.read_number("Enter a location [1-1000]: ")
        self.player.move(location)
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
        self.jumper.watch(self.player.location)
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        hint = self.rabbit.get_hint()
        self.console.write(hint)
        self.keep_playing = (self.rabbit.distance[-1] != 0)