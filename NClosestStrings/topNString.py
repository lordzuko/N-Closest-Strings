import sys
from operator import itemgetter

from LevenshteinDistance.Trie import Trie
from LevenshteinDistance.LevDistance import TrieLevDistance

def find_proximity(word1, word2):
    """
    Function to choose which word is closer if edit distance is equal
    :param word1:
    :param word2:
    :return:
    """

def main(word_list, N):
    """

    :param path:
    :param N:
    :return:
    """
    trie = Trie()
    trie_lev_distance = TrieLevDistance(trie)
    for word in word_list:
        trie.insert(word)

    max_cost = 4
    for x in word_list:
        closest_strings = trie_lev_distance.search(x, max_cost)
        closest_strings.sort(key=itemgetter(1))
        closest_strings = [s[0] for s in closest_strings]

        print("The closest {} items for {} is {}".format(N,x,','.join(sorted(closest_strings[1:N+1]))))


if __name__ == "__main__":
    # takes 2 parametets
    # 1 -> path to input file
    # 2 -> N
    #TODO: check the number of arguments later
    #main(sys.argv[1:])
    #word_list = ['1','2','3','4','5','6']
    word_list = ['cat','dog','god','cats','cactus']
    main(word_list,3)
