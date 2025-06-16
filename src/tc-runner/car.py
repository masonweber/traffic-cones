class Car:
    def __init__(self, position, destination):
        self.position = position #0, 90, 180, 270
        self.destination = destination #0, 90, 180, 270
    
    def __str__(self):
        return f"{self.position} -> {self.destination}"
    
    def getTurnDirection(self):
        degreeTurn = abs(self.destination - self.position)