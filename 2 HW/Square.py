
import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectanglePatch

class Square(Figure):
    def __init__(self, points):
        super().__init__(points)
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()
        

    def calculatePerimeter(self):
        return 4*self.points[2]


    def calculateSquare(self):
        return pow(self.points[2],2)

    
    def __str__(self):
        return f"['square', {self.square}, {self.perimeter}, [{self.points[:2]}, {self.points[2]}]]"

    @classmethod
 
    def constructFromSeries(cls,series: pd.Series):
        return cls(list(tuple(map(float, series[0].split(';')[1].split(':')))) + [float(series[0].split(';')[2])])


    def graphFigure(self):
        fig, ax = plt.subplots()
        rectangle = RectanglePatch((self.points[0], self.points[1]), self.points[2], self.points[2], fill=False)
        ax.add_artist(rectangle)
        ax.set_aspect('equal')
        plt.xlim(self.points[0] - self.points[2] - 1, self.points[0] + self.points[2] + 1)
        plt.ylim(self.points[1] - self.points[2] - 1, self.points[1] + self.points[2] + 1)
        plt.show()


