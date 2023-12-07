import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch

class Circle(Figure):
    def __init__(self, points):
        super().__init__(points)
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()
        
    def calculatePerimeter(self):
        return 2 * math.pi * self.points[2]

    def calculateSquare(self):
        return math.pi * math.pow(self.points[2], 2)
    
    def __str__(self):
        return f"['circle', {self.square}, {self.perimeter}, [{self.points[:2]}, {self.points[2]}]]"


    @classmethod
    def constructFromSeries(cls, series: pd.Series):
        return cls([float(value) for value in series[1].split(':')] + [float(series[2])])
  
    def graphFigure(self):
        fig, ax = plt.subplots()
        circle = CirclePatch((self.points[0], self.points[1]), self.points[2], fill=False)
        ax.add_artist(circle)
        ax.set_aspect('equal')
        plt.xlim(self.points[0] - self.points[2] - 1, self.points[0] + self.points[2] + 1)
        plt.ylim(self.points[1] - self.points[2] - 1, self.points[1] + self.points[2] + 1)
        plt.show()
