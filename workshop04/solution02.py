from collections import deque


def count_distances(mat):
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    dist = [[float('inf')] * n for _ in range(m)]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist


def test_count_distances():
    print("\nТЕСТИРОВАНИЕ..\n")

    mat1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result1 = count_distances(mat1)
    expected1 = [[0, 0, 0], [0, 1, 0],x [0, 0, 0]]
    assert result1 == expected1, f"Ошибка: ожидалось {expected1}, получено {result1}"

    mat2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result2 = count_distances(mat2)
    expected2 = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert result2 == expected2, f"Ошибка: ожидалось {expected2}, получено {result2}"

    mat3 = [[0]]
    result3 = count_distances(mat3)
    expected3 = [[0]]
    assert result3 == expected3, f"Ошибка: ожидалось {expected3}, получено {result3}"

    mat4 = [[1]]
    result4 = count_distances(mat4)
    expected4 = [[float('inf')]]
    assert result4 == expected4, f"Ошибка: ожидалось {expected4}, получено {result4}"

    mat5 = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    result5 = count_distances(mat5)
    expected5 = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
    assert result5 == expected5, f"Ошибка: ожидалось {expected5}, получено {result5}"

    mat6 = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    result6 = count_distances(mat6)
    expected6 = [[1, 0, 1], [2, 1, 2], [3, 2, 3]]
    assert result6 == expected6, f"Ошибка: ожидалось {expected6}, получено {result6}"

    mat7 = [[0, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 0]]
    result7 = count_distances(mat7)
    expected7 = [[0, 1, 0, 1], [1, 0, 1, 2], [1, 1, 2, 1], [0, 1, 1, 0]]
    assert result7 == expected7, f"Ошибка: ожидалось {expected7}, получено {result7}"

    mat8 = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1]]
    result8 = count_distances(mat8)
    expected8 = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 2],
                 [1, 2, 1, 2, 3], [0, 1, 2, 3, 4]]
    assert result8 == expected8, f"Ошибка: ожидалось {expected8}, получено {result8}"

    mat9 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
        1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    result9 = count_distances(mat9)
    expected9 = [[4, 3, 2, 3, 4], [3, 2, 1, 2, 3], [
        2, 1, 0, 1, 2], [3, 2, 1, 2, 3], [4, 3, 2, 3, 4]]
    assert result9 == expected9, f"Ошибка: ожидалось {expected9}, получено {result9}"

    mat10 = []
    result10 = count_distances(mat10)
    expected10 = []
    assert result10 == expected10, f"Ошибка: ожидалось {expected10}, получено {result10}"

    print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ!\n")


if __name__ == "__main__":
    test_count_distances()
