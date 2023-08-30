import nltk
from spellchecker import SpellChecker
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

    def suggestions(self, word, max_suggestions=5):
        spell = SpellChecker()
        corrections = spell.candidates(word)
        return corrections

english_words = words.words()
dictionary = Trie()
for word in english_words:
    dictionary.insert(word)
    
