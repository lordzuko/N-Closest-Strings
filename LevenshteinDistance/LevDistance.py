import time
import sys

class TrieLevDistance:

    def __init__(self, trie):
        """
        :param trie: Prebuilt trie to easily check for the latest row
        """
        self.trie = trie

    def search(self,word, maxCost):
        """
        Return words that are less than the given
        maximum distance from the target word
        :param target:
        :param word: word to be searched
        :param maxCost:
        :param trie: Prebuilt trie of words
        :return: its helder function yields words less than maximum distance
        """
        result = []
        currentRow = range(len(word) + 1)
        for letter in self.trie.root.children:
            self.searchRecursive(self.trie.root.children[letter], letter, word, currentRow, result,
                            maxCost)

        return result

    def searchRecursive(self,node, letter, word, previousRow, result, maxCost):
        """
        Recursive helper function for search(), assumes that previous row has
        already been filled.
        :param node: current Trie Node
        :param letter: next letter to node
        :param word: word to be searched
        :param previousRow: row that this recursive function assumes has been filled
        :param maxCost: upper limit on distance b/w words to be yielded
        :return: result -> list
        """

        columns = len(word) + 1
        currentRow = [previousRow[0] + 1]

        # Build one row for the letter, with a column for each letter in the target
        # word, plus one for the empty string at column 0
        for column in range(1, columns):

            # calculate the costs for the cases
            # 1) an alphabet is added
            # 2) an alphabet is deleted
            # 3) an alphabet is replaced

            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word[column - 1] != letter:
                # if its not a match
                replaceCost = previousRow[column - 1] + 1
            else:
                # no need to replace if its a match, hence cost stays the same
                replaceCost = previousRow[column - 1]
            currentRow.append(min((insertCost, deleteCost, replaceCost)))

        # if the optimal cost in the currentRow, viz the last element in row
        # is lesser than the maximum cost and there is a word in trie
        # then it is a close string
        if currentRow[-1] <= maxCost and node.word != None:
            result.append((node.word, currentRow[-1]))

        if min(currentRow) <= maxCost:
            for letter in node.children:
                self.searchRecursive(node.children[letter], letter, word, currentRow, result,
                                maxCost)


