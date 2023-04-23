class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def get_number_correspondence(char: str) -> str:
    T9_CHARS = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    return T9_CHARS.get(char, "")


trie = None


def get_valid_t9_words(number: str, words: list[str]) -> list[str]:
    global trie
    if trie is None:
        trie = Trie()
        for word in words:
            trie.insert(word)

    if len(number) == 0:
        return []

    if len(number) == 1:
        return [word for word in get_number_correspondence(number) if trie.search(word)]

    result = []

    def dfs(node: TrieNode, prefix: str, numbers_remaining: str):
        if node.is_word and numbers_remaining == "":
            result.append(prefix)

        if numbers_remaining == "":
            return

        for char in get_number_correspondence(numbers_remaining[0]):
            if char in node.children:
                dfs(node.children[char], prefix + char, numbers_remaining[1:])

    dfs(trie.root, "", number)

    return result
