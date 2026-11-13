from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = []
        self.x_axis: dict = defaultdict(list)
        self.y_axis: dict = defaultdict(list)

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        self.points.append(p)
        self.x_axis[p[1]].append(p) # parallel to the x axis
        self.y_axis[p[0]].append(p) # parallel to the y axis

    def count(self, point: List[int]) -> int:
        count = 0
        for x in self.x_axis[point[1]]:
            dx = x[0] - point[0]
            if dx == 0:
                continue
            l1 = [(point[0], point[1] + dx), (point[0] + dx, point[1] + dx)]
            l2 = [(point[0], point[1] - dx), (point[0] + dx, point[1] - dx)]
            square_1 = all(p in self.y_axis[p[0]] for p in l1)
            square_2 = all(p in self.y_axis[p[0]] for p in l2)
            if square_1:
                tmp = 1
                for p in l1:
                    tmp *= self.points.count(p)
                count += tmp
            if square_2:
                tmp = 1
                for p in l2:
                    tmp *= self.points.count(p)
                count += tmp
        return count
