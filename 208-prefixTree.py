class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for letter in word:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]

        return node.isWord
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for letter in prefix:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]

        return True

obj = Trie()
obj.insert('test')
print(obj.search('test'))
print(obj.search('notest'))
print(obj.startsWith('tes'))
