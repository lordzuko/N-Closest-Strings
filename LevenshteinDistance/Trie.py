class TrieNode:
    """
        General Node of Trie
    """
    def __init__(self):
        """
            :param word: word which this node makes
            :param children: next alphabets following this node
        """
        self.word = None
        self.children = dict()

class Trie:

    def __init__(self):
        """
            :param root : start of Trie Tree
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert word in the trie.
        :param word: String
        :return: None
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.word = word

    def search(self, word):
        """

        :param word: word to be searched in trie
        :return: boolean
        """
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False

        # when search completes and word is present in Trie
        if cur.word is None:
            return False
        return True

    def startsWith(self, prefix):
        """

        :param prefix: prefix to be searched in trie
        :return: boolean
        """
        cur = self.root
        for w in prefix:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False

        return True


if __name__ == "__main__":
    word_list = ["","i","am","himanshu","i","love","coding"]
    trie = Trie()
    for word in word_list:
        #build Trie
        trie.insert(word)

    # Test search and startsWith methods
    print(trie.search("am") == True)
    print(trie.search("love") == True)
    print(trie.startsWith("hima") == True)
    print(trie.search("") == True)

