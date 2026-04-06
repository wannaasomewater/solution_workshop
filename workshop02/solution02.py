
def find_smallest_in_matrix(matrix, k):
    n = len(matrix)
    left = matrix[0][0]
    right = matrix[n-1][n-1]

    while left < right:
        mid = (right + left) // 2

        count = 0
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1

        if count < k:
            left = mid + 1
        else:
            right = mid

    return left


def test_find_smallest_in_matrix():
    matrix1 = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]]

    assert find_smallest_in_matrix(matrix1, 8) == 13

    matrix2 = [
        [1, 2],
        [3, 4]
    ]
    assert find_smallest_in_matrix(matrix2, 1) == 1
    assert find_smallest_in_matrix(matrix2, 2) == 2
    assert find_smallest_in_matrix(matrix2, 3) == 3
    assert find_smallest_in_matrix(matrix2, 4) == 4

    matrix3 = [
        [1, 3, 5],
        [2, 4, 6],
        [7, 8, 9]
    ]
    assert find_smallest_in_matrix(matrix3, 5) == 5

    matrix4 = [[1]]
    assert find_smallest_in_matrix(matrix4, 1) == 1

    matrix5 = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7]
    ]
    assert find_smallest_in_matrix(matrix5, 10) == 4
    print("Все тесты пройдены")


if __name__ == "__main__":
    test_find_smallest_in_matrix()
