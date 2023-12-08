import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectanglePatch

class Rectangle(Figure):
    def __init__(self, points):
        super().__init__(points)
        
    def calculatePerimeter(self):
        return 2 * (abs(self.points[0][0] - self.points[1][0]) + abs(self.points[0][1] - self.points[1][1]))

    def calculateSquare(self):
        return abs(self.points[0][0] - self.points[1][0]) * abs(self.points[0][1] - self.points[1][1])
    
    def __str__(self):
        return f"['rectangle', {self.square}, {self.perimeter}, [{self.points[:2]}, {self.points[2:]}]]"

    @classmethod
    def constructFromSeries(cls, series: pd.Series):
        return cls([[float(value) for value in series[1].split(':')]] +[[float(value) for value in series[2].split(':')]])

    def graphFigure(self):
        fig, ax = plt.subplots()
        rectangle = RectanglePatch((self.points[0][0], self.points[0][1]), abs(self.points[0][0] - self.points[1][0]), abs(self.points[0][1] - self.points[1][1]), fill=False)
        ax.add_artist(rectangle)
        ax.set_aspect('equal')
        
        x_values = [point[0] for point in self.points] 
        y_values = [point[1] for point in self.points]  

        plt.xlim(min(x_values) - 1, max(x_values) + 1)
        plt.ylim(min(y_values) - 1, max(y_values) + 1)
        plt.show()
