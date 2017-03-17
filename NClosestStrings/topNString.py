import sys
from operator import itemgetter

from LevenshteinDistance.Trie import Trie
from LevenshteinDistance.LevDistance import TrieLevDistance

# TODO: Try to make it lazy
def create_word_list(path):
    pass
# TODO: later 1st argument is path
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

    closest_strings = trie_lev_distance.search('4',3)
    closest_strings.sort(key=itemgetter(1,0))
    print(closest_strings[1:N+1])


if __name__ == "__main__":
    # takes 2 parametets
    # 1 -> path to input file
    # 2 -> N
    #TODO: check the number of arguments later
    #main(sys.argv[1:])
    word_list = ['1','2','3','4','5','6']
    main(word_list,3)
