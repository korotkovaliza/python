import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as QuadrilateralPatch

class Quadrilateral(Figure):
    def __init__(self, points):
        super().__init__(points)
        
    def calculatePerimeter(self):
        perimeter = 0
        for i in range(4):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % 4]
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return perimeter

    def calculateSquare(self):
        square = 0
        for i in range(4):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % 4]
            square += (x1 * y2 - x2 * y1) / 2
        return abs(square)
    
    def __str__(self):
        vertices = [self.points[i] for i in range(0, 4)]
        return f"['quadrilateral', {self.square}, {self.perimeter}, {vertices}]"

    @classmethod
    def constructFromSeries(cls, series: pd.Series):
        return cls([[float(value) for value in series[1].split(':')]] + [[float(value) for value in series[2].split(':')]]+[[float(value) for value in series[3].split(':')]] + [[float(value) for value in series[4].split(':')]])

    def graphFigure(self):
        fig, ax = plt.subplots() 
        quadrilateral = QuadrilateralPatch(self.points, fill=False)
        ax.add_artist(quadrilateral)
        ax.set_aspect('equal')

        x_values = [point[0] for point in self.points] 
        y_values = [point[1] for point in self.points]  

        plt.xlim(min(x_values) - 1, max(x_values) + 1)
        plt.ylim(min(y_values) - 1, max(y_values) + 1)
        plt.show()

