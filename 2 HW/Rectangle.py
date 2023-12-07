import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectanglePatch

class Rectangle(Figure):
    def __init__(self, points):
        super().__init__(points)
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()
        
    def calculatePerimeter(self):
        return 2 * (abs(self.points[0] - self.points[2]) + abs(self.points[1] - self.points[3]))

    def calculateSquare(self):
        return abs(self.points[0] - self.points[2]) * abs(self.points[1] - self.points[3])
    
    def __str__(self):
        return f"['rectangle', {self.square}, {self.perimeter}, [{self.points[:2]}, {self.points[2:]}]]"

    @classmethod
    def constructFromSeries(cls, series: pd.Series):
        return cls(list(tuple(map(float, series[0].split(';')[1].split(':'))))+list(tuple(map(float, series[0].split(';')[2].split(':')))))

    def graphFigure(self):
        fig, ax = plt.subplots()
        rectangle = RectanglePatch((self.points[0], self.points[1]), abs(self.points[0] - self.points[2]), abs(self.points[1] - self.points[3]), fill=False)
        ax.add_artist(rectangle)
        ax.set_aspect('equal')
        plt.xlim(min(self.points) - 1, max(self.points) + 1)
        plt.ylim(min(self.points) - 1, max(self.points) + 1)
        plt.show()

