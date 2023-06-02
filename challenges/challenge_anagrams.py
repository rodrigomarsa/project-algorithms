def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def is_anagram(first_string, second_string):
    first_string_ordened = quicksort(first_string.lower())
    second_string_ordened = quicksort(second_string.lower())
    f = "".join(first_string_ordened)
    s = "".join(second_string_ordened)
    if len(first_string) == 0 or len(second_string) == 0:
        return f, s, False
    elif first_string_ordened == second_string_ordened:
        return f, s, True
    else:
        return f, s, False


print(is_anagram("pedra", "perdaaa"))
