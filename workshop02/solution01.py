
def length_of_longest_substring(string):
    left = 0
    max_length = 0
    dict_item_index = {}

    for right in range(len(string)):
        dict_item = string[right]
        if dict_item in dict_item_index and dict_item_index[dict_item] >= left:
            left = dict_item_index[dict_item] + 1

        dict_item_index[dict_item] = right
        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length


def test_algorithm():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("au") == 2
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring("aab") == 2
    assert length_of_longest_substring("abba") == 2
    assert length_of_longest_substring("abcdefg") == 7

    print("Все тесты пройдены")


if __name__ == "__main__":
    test_algorithm()
