import pandas as pd
import numpy as np

board = np.zeros((10,10))
print(board)

class Ship:

    def __init__(self,length,rotation):
        self.length = length
        self.rotation = rotation
    
    def __str__(self) -> str:
        return f"I am ship. I have {self.length} blocks and I am placed {self.rotation}."
    
    

class Board:

    def __init__(self, size, difficulty):
        self.size = size
        self.difficulty = difficulty


    def __str__(self) -> str:
        return "Board info"
    


class Page:

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "Just a page sketch"
    

class MainPage(Page):

    def __init__(self):
        super().__init__()
        
