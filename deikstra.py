import heapq

def dijkstra_matrix(graph, start):
    n = len(graph)  # Количество вершин
    distances = [float('inf')] * n  # Изначально все расстояния ∞
    distances[start] = 0  # Расстояние до стартовой вершины 0

    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Если текущее расстояние больше уже найденного, пропускаем
        if current_distance > distances[current_node]:
            continue

        # Обходим всех соседей (по строке в матрице)
        for neighbor in range(n):
            weight = graph[current_node][neighbor]
            if weight > 0:  # Если есть ребро
                distance = current_distance + weight
                if distance < distances[neighbor]:  # Нашли более короткий путь
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances  # Возвращаем массив кратчайших расстояний


# Пример: граф в виде матрицы смежности
graph = [
    [0, 4, 2, 0],  # Вершина 0 → (0-1: 4, 0-2: 2)
    [4, 0, 5, 10],  # Вершина 1 → (1-0: 4, 1-2: 5, 1-3: 10)
    [2, 5, 0, 3],  # Вершина 2 → (2-0: 2, 2-1: 5, 2-3: 3)
    [0, 10, 3, 0]  # Вершина 3 → (3-1: 10, 3-2: 3)
]

start_node = 0  # Начинаем с вершины 0
shortest_paths = dijkstra_matrix(graph, start_node)
print(shortest_paths)  # Вывод кратчайших расстояний от вершины 0
