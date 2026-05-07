class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.end_of_word = True

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.end_of_word

    def starts_with(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return []

            current = current.children[char]

        suggestions = []

        self._dfs(current, prefix, suggestions)

        return suggestions

    def _dfs(self, node, path, suggestions):
        if node.end_of_word:
            suggestions.append(path)

        for char, next_node in node.children.items():
            self._dfs(next_node, path + char, suggestions)




for word in words:
    trie.insert(word)

print(trie.search("apple"))
print(trie.search("apps"))

print(trie.starts_with("app"))
