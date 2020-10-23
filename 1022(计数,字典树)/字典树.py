class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self,word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word



if __name__ == '__main__':
    trie = Trie()
    trie.insert("someone")
    trie.insert("someday")
    trie.insert("goodnight")
    print(trie.root.data)
