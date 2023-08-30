import nltk
import heapq
from nltk.corpus import words
nltk.download("words") #this should be run once but whatever
class TrieNode:
    def __init__(self):
        self.children = {} #children of a certain node(letter) is a dictionary of letters which when traversing creates a word at the end
        is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode() # create a new letter if the letter does not exist and giving it a child
            node = node.children[c] #traverse into the next child letter
        node.is_word = True
    
    def search(self, word):
        node = self.root 
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def suggest_corrections(self, word, max_suggestions=5):
        suggestions = []
        self._dfs_corrections(self.root, word, "", suggestions, max_suggestions)
        return suggestions

    def _dfs_corrections(self, node, current_word, current_path, suggestions, max_suggestions):
        if node.is_word and current_path != current_word:
            similarity = self._calculate_similarity(current_word, current_path)
            heapq.heappush(suggestions, (similarity, current_path))

            if len(suggestions) > max_suggestions:
                heapq.heappop(suggestions)

        for char, child_node in node.children.items():
            self._dfs_corrections(child_node, current_word, current_path + char, suggestions, max_suggestions)

    def _calculate_similarity(word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        for i in range(m + 1):
            dp[i][0] = i
    
        for j in range(n + 1):
            dp[0][j] = j
    
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if word1[i - 1] == word2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + cost
                )
    
        return dp[m][n]

english_words = words.words()
dictionary = Trie()
for word in english_words:
    dictionary.insert(word)
    
