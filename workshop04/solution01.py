def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def test_longest_increasing_subsequence():
    print("\nТЕСТИРОВАНИЕ..\n")

    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    result1 = longest_increasing_subsequence(nums1)
    expected1 = 4
    assert result1 == expected1, f"Ошибка: ожидалось {expected1}, получено {result1}"

    nums2 = [0, 1, 0, 3, 2, 3]
    result2 = longest_increasing_subsequence(nums2)
    expected2 = 4
    assert result2 == expected2, f"Ошибка: ожидалось {expected2}, получено {result2}"

    nums3 = [7, 7, 7, 7, 7, 7, 7]
    result3 = longest_increasing_subsequence(nums3)
    expected3 = 1
    assert result3 == expected3, f"Ошибка: ожидалось {expected3}, получено {result3}"

    nums4 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    result4 = longest_increasing_subsequence(nums4)
    expected4 = 6
    assert result4 == expected4, f"Ошибка: ожидалось {expected4}, получено {result4}"

    nums5 = [2, 2, 2, 2]
    result5 = longest_increasing_subsequence(nums5)
    expected5 = 1
    assert result5 == expected5, f"Ошибка: ожидалось {expected5}, получено {result5}"

    nums6 = [1]
    result6 = longest_increasing_subsequence(nums6)
    expected6 = 1
    assert result6 == expected6, f"Ошибка: ожидалось {expected6}, получено {result6}"

    nums7 = []
    result7 = longest_increasing_subsequence(nums7)
    expected7 = 0
    assert result7 == expected7, f"Ошибка: ожидалось {expected7}, получено {result7}"

    nums8 = [4, 10, 4, 3, 8, 9]
    result8 = longest_increasing_subsequence(nums8)
    expected8 = 3
    assert result8 == expected8, f"Ошибка: ожидалось {expected8}, получено {result8}"

    nums9 = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    result9 = longest_increasing_subsequence(nums9)
    expected9 = 6
    assert result9 == expected9, f"Ошибка: ожидалось {expected9}, получено {result9}"

    nums10 = [-2, -1, 0, 1, 2]
    result10 = longest_increasing_subsequence(nums10)
    expected10 = 5
    assert result10 == expected10, f"Ошибка: ожидалось {expected10}, получено {result10}"

    print("\nВСЕ ТЕСТЫ ПРОЙДЕНЫ!\n")


if __name__ == "__main__":
    test_longest_increasing_subsequence()
