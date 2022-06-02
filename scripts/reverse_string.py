def reverse_string(word: str) -> str:
    reversed_string = ""
    index = len(word) - 1
    while index >= 0:
        reversed_string += (word[index])
        index -= 1
    return reversed_string
