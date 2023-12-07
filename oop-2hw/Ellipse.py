import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse as EllipsePatch

class Ellipse(Figure):
    def __init__(self, points):
        super().__init__(points)
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()
        
    def calculatePerimeter(self):
        a = self.points[2]
        b = self.points[3]
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return math.pi * (a + b) * (1 + ((3 * h) / (10 + math.sqrt(4 - 3 * h))))
    
    def calculateSquare(self):
        return math.pi * self.points[2] * self.points[3]
    
    def __str__(self):
        return f"['ellipse', {self.square}, {self.perimeter}, [{self.points[:2]}, {self.points[2]}, {self.points[3]}]]"

    @classmethod
    def constructFromSeries(cls, series: pd.Series):
        return cls([float(value) for value in series[1].split(':')] + [float(series[2])]+ [float(series[3])])

    def graphFigure(self):
        fig, ax = plt.subplots()
        ellipse = EllipsePatch((self.points[0], self.points[1]), self.points[2], self.points[3], fill=False)
        ax.add_artist(ellipse)
        ax.set_aspect('equal')
        plt.xlim(self.points[0] - self.points[2] - 1, self.points[0] + self.points[2] + 1)
        plt.ylim(self.points[1] - self.points[3] - 1, self.points[1] + self.points[3] + 1)
        plt.show()

