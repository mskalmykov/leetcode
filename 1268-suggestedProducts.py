from typing import List

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

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        def suggestions(t: Trie, p: str) -> List[str]:
            words = []
            node = t.root

            for letter in p:
                if letter not in node.children:
                    return []
                else:
                    node = node.children[letter]

            if node.isWord:
                words.append(p)

            stack = []
            for w in node.children:
                stack.append((p + w, node.children[w]))

            while stack:
                prefix, node = stack.pop()
                if node.isWord:
                    words.append(prefix)
                for w in node.children:
                    stack.append((prefix + w, node.children[w]))

            words.sort()

            return words[:3]


        trie = Trie()
        for p in products:
            trie.insert(p)

        answer = []
        prefix = ''
        for c in searchWord:
            prefix += c
            answer.append(suggestions(trie, prefix))

        return answer

print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
print(Solution().suggestedProducts(["havana"], "havana"))