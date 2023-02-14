def is_permutation_of_palindrome(phrase: str) -> bool:
    """Returns True if phrase is a permutation of a palindrome."""
    phrase = phrase.replace(" ", "")
    char_counts = {}

    for char in phrase:
        if not char.isalpha():
            continue

        char = char.lower()
        char_counts[char] = 1 if char not in char_counts else char_counts[char] + 1

    odd_count = 0
    for char, count in char_counts.items():
        if count % 2 == 1:
            odd_count += 1

            if odd_count > 1:
                return False

    return True
