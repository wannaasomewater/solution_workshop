import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]


def test_findKthLargest():
    print("\nТЕСТИРОВАНИЕ..\n")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    assert findKthLargest(nums1, k1) == 5

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    assert findKthLargest(nums2, k2) == 4

    nums3 = [1]
    k3 = 1
    assert findKthLargest(nums3, k3) == 1

    nums4 = [5, 4, 3, 2, 1]
    k4 = 1
    assert findKthLargest(nums4, k4) == 5

    nums5 = [5, 4, 3, 2, 1]
    k5 = 5
    assert findKthLargest(nums5, k5) == 1

    nums6 = [-1, -2, -3, -4, -5]
    k6 = 2
    assert findKthLargest(nums6, k6) == -2

    nums7 = [2, 2, 2, 2, 2]
    k7 = 3
    assert findKthLargest(nums7, k7) == 2

    nums8 = [1, 2]
    k8 = 1
    assert findKthLargest(nums8, k8) == 2

    nums9 = [1, 2]
    k9 = 2
    assert findKthLargest(nums9, k9) == 1

    nums10 = [1234565, 500000, 999999, 1, 0, -1000000]
    k10 = 3
    assert findKthLargest(nums10, k10) == 500000

    print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ!\n")


if __name__ == "__main__":
    test_findKthLargest()
