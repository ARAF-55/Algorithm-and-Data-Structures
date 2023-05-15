class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node is None:
                node = TrieNode()
                currentNode.children.update({i: node})
            currentNode = node
        currentNode.endOfString = True

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node is None:
                return "The string ain't present in the trie"
            else:
                currentNode = node
        if currentNode.endOfString:
            return "The string is present in the trie"
        else:
            return "The string ain't present in the trie"


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    if currentNode is None:
        return False
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endOfString:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
newTrie.insertString("jabalala")
deleteString(newTrie.root, 'Appl', 0)
print(newTrie.searchString("jabalala"))
print(newTrie.searchString("Appl"))

