from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def test_levelOrder():
    print("\nТЕСТИРОВАНИЕ..\n")
    root1 = None
    result1 = levelOrder(root1)
    expected1 = []
    assert result1 == expected1, f"Ошибка: ожидалось {expected1}, получено {result1}"

    root2 = TreeNode(1)
    result2 = levelOrder(root2)
    expected2 = [[1]]
    assert result2 == expected2, f"Ошибка: ожидалось {expected2}, получено {result2}"

    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    root3.right.left = TreeNode(6)
    root3.right.right = TreeNode(7)

    result3 = levelOrder(root3)
    expected3 = [[1], [2, 3], [4, 5, 6, 7]]
    assert result3 == expected3, f"Ошибка: ожидалось {expected3}, получено {result3}"

    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)

    result4 = levelOrder(root4)
    expected4 = [[1], [2], [3]]
    assert result4 == expected4, f"Ошибка: ожидалось {expected4}, получено {result4}"

    root5 = TreeNode(3)
    root5.left = TreeNode(9)
    root5.right = TreeNode(20)
    root5.right.left = TreeNode(15)
    root5.right.right = TreeNode(7)

    result5 = levelOrder(root5)
    expected5 = [[3], [9, 20], [15, 7]]
    assert result5 == expected5, f"Ошибка: ожидалось {expected5}, получено {result5}"

    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.left.left = TreeNode(3)

    result6 = levelOrder(root6)
    expected6 = [[1], [2], [3]]
    assert result6 == expected6, f"Ошибка: ожидалось {expected6}, получено {result6}"

    root7 = TreeNode(10)
    root7.left = TreeNode(5)
    root7.right = TreeNode(15)
    root7.left.left = TreeNode(3)
    root7.left.right = TreeNode(7)
    root7.right.left = TreeNode(12)
    root7.right.right = TreeNode(20)
    root7.left.left.left = TreeNode(2)
    root7.left.left.right = TreeNode(4)

    result7 = levelOrder(root7)
    expected7 = [[10], [5, 15], [3, 7, 12, 20], [2, 4]]
    assert result7 == expected7, f"Ошибка: ожидалось {expected7}, получено {result7}"

    tree_list = [3, 9, 20, None, None, 15, 7]
    root8 = build_tree(tree_list)
    result8 = levelOrder(root8)
    expected8 = [[3], [9, 20], [15, 7]]
    assert result8 == expected8, f"Ошибка: ожидалось {expected8}, получено {result8}"

    root9 = TreeNode(-1)
    root9.left = TreeNode(-2)
    root9.right = TreeNode(-3)
    root9.left.left = TreeNode(-4)
    root9.left.right = TreeNode(-5)
    root9.right.right = TreeNode(-6)

    result9 = levelOrder(root9)
    expected9 = [[-1], [-2, -3], [-4, -5, -6]]
    assert result9 == expected9, f"Ошибка: ожидалось {expected9}, получено {result9}"

    root10 = TreeNode(1)
    root10.left = TreeNode(2)
    root10.right = TreeNode(2)
    root10.left.left = TreeNode(3)
    root10.left.right = TreeNode(4)
    root10.right.left = TreeNode(4)
    root10.right.right = TreeNode(3)

    result10 = levelOrder(root10)
    expected10 = [[1], [2, 2], [3, 4, 4, 3]]
    assert result10 == expected10, f"Ошибка: ожидалось {expected10}, получено {result10}"
    print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ!\n")


if __name__ == "__main__":
    test_levelOrder()
