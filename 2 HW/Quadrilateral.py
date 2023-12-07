import pandas as pd
from Figure import Figure
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as QuadrilateralPatch

class Quadrilateral(Figure):
    def __init__(self, points):
        super().__init__(points)
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()
        
    def calculatePerimeter(self):
        perimeter = 0
        n = len(self.points) // 2
        for i in range(n):
            x1, y1 = self.points[i * 2], self.points[i * 2 + 1]
            x2, y2 = self.points[(i + 1) % n * 2], self.points[(i + 1) % n * 2 + 1]
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return perimeter

    def calculateSquare(self):
        square = 0
        n = len(self.points) // 2
        for i in range(n):
            x1, y1 = self.points[i * 2], self.points[i * 2 + 1]
            x2, y2 = self.points[(i + 1) % n * 2], self.points[(i + 1) % n * 2 + 1]
            square += (x1 * y2 - x2 * y1) / 2
        return abs(square)
    
    def __str__(self):
        vertices = [self.points[i:i+2] for i in range(0, len(self.points), 2)]
        return f"['quadrilateral', {self.square}, {self.perimeter}, {vertices}]"

    @classmethod
    def constructFromSeries(cls, series: pd.Series):
        return cls(list(tuple(map(float, series[0].split(';')[1].split(':'))))+list(tuple(map(float, series[0].split(';')[2].split(':'))))+list(tuple(map(float, series[0].split(';')[3].split(':'))))+list(tuple(map(float, series[0].split(';')[4].split(':')))))

    def graphFigure(self):
        fig, ax = plt.subplots()
        vertices = [(self.points[i], self.points[i + 1]) for i in range(0, len(self.points), 2)]
        quadrilateral = QuadrilateralPatch(vertices, fill=False)
        ax.add_artist(quadrilateral)
        ax.set_aspect('equal')
        x_values, y_values = zip(*vertices)
        plt.xlim(min(x_values) - 1, max(x_values) + 1)
        plt.ylim(min(y_values) - 1, max(y_values) + 1)
        plt.show()

