import sys
import heapq
from operator import itemgetter

from LevenshteinDistance.Trie import Trie
from LevenshteinDistance.LevDistance import TrieLevDistance

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
    word_list_index = {}
    for i,e in enumerate(word_list):
        word_list_index[e] = i
    #print(word_list_index)

    for x in word_list:
        closest_strings = trie_lev_distance.search(x, max_cost)
        closest_strings.sort(key=itemgetter(1))
        closest_strings = [s[0] for s in closest_strings]
        diff_index_x = [(c,abs(word_list_index[x] - word_list_index[c])) for c in closest_strings]
        diff_index_x.sort(key=itemgetter(1))
        diff_index_x = [s[0] for s in diff_index_x]
        print("The closest {} items for {} is {}".format(N,x,','.join(diff_index_x[1:N+1])))



if __name__ == "__main__":
    # takes 2 parametets
    # 1 -> path to input file
    # 2 -> N
    #TODO: check the number of arguments later
    #main(sys.argv[1:])
    word_list = ['1','2','3','4','5','6']
    #word_list = ['a1', 'a2', 'b', 'b2', '1', '2', '3', '4']
    #word_list = ['cat','dog','god','cats','cactus']
    main(word_list,3)
