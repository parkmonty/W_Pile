import sys
import numpy as np
from math import sqrt
import heapq

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


plant_count, connect_wire = map(int, sys.stdin.readline().split())
limit_len = float(sys.stdin.readline().strip())

location = []
for _ in range(plant_count):
    location.append(list(map(int, sys.stdin.readline().split())))

all_distance = np.full((plant_count, plant_count), 1e8)

for p1 in range(plant_count):
    for p2 in range(plant_count):
        if p1 >= p2:
            continue

        all_distance[p1][p2] = dist(location[p1][0], location[p1][1], location[p2][0], location[p2][1])

        if all_distance[p1][p2] > limit_len:
            all_distance[p1][p2] = 1e8
        else:
            all_distance[p2][p1] = all_distance[p1][p2]

for _ in range(connect_wire):
    plant1, plant2 = map(int, sys.stdin.readline().split())
    all_distance[plant1 - 1][plant2 - 1] = 0
    all_distance[plant2 - 1][plant1 - 1] = 0

distance = [1e8 for _ in range(plant_count)]
distance[0] = 0

len_loc = []
heapq.heappush(len_loc, (0, 0))

while len_loc:
    wire_len, plant = heapq.heappop(len_loc)

    if distance[plant] < wire_len:
        continue

    for num, cost in enumerate(all_distance[plant]):
        if cost == 1e8:
            continue

        new_cost = wire_len + cost
        if new_cost < distance[num]:
            distance[num] = new_cost
            heapq.heappush(len_loc, (new_cost, num))

print(int(distance[plant_count - 1] * 1000))