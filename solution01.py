class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    ptrA = headA
    ptrB = headB

    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA

    return ptrA


def test_get_intersection_node():
    # просто пересекающиеся списки
    node1 = ListNode(4)
    node2 = ListNode(1)
    node3 = ListNode(8)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = ListNode(5)
    node7 = ListNode(6)
    node8 = ListNode(1)

    node6.next = node7
    node7.next = node8
    node8.next = node3

    res = get_intersection_node(node1, node6)
    assert res == node3
    assert res.val == 8

    # пересекающиеся списки (пересечение в начале)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = node1

    res = get_intersection_node(node1, node6)
    assert res == node1
    assert res.val == 1

    # пересекающиеся списки (пересечение в конце)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node5

    res = get_intersection_node(node1, node6)
    assert res == node5
    assert res.val == 5

    # пересекающиеся списки (разная длина до пересечения)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9

    node10 = ListNode(10)
    node11 = ListNode(11)
    node12 = ListNode(12)

    node10.next = node11
    node11.next = node12
    node12.next = node5

    res = get_intersection_node(node1, node10)
    assert res == node5
    assert res.val == 5

    # непересекающиеся списки
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node10 = ListNode(10)
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10

    res = get_intersection_node(node1, node6)
    assert res is None

    # один список пустой
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    res = get_intersection_node(node1, None)
    assert res is None

    print("Все тесты пройдены")


test_get_intersection_node()
