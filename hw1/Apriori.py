import csv
from itertools import combinations, chain

class Candidate:
    def __init__(self):
        self.name = 0
        self.item_sets = []
        self.candidates = {}
        self.min_sup = 0
        self.support = 1
        self.k = 1


class Apriori:
    def __init__(self, filename, min_sup):
        self._filename = filename
        self._min_sup = min_sup
        self.Candidates = []
        self._frequentItemSets = {}
        self.k = 1 #this is to set k itemsetl
        self.main()

    def main(self):
        first_candidate = self.create_first_candidate(self._filename, self._min_sup)
        self.Candidates.append(first_candidate)

        self.create_k_candidate(self._filename, self._min_sup, self.Candidates, self.k)





    def create_first_candidate(self,filename, min_sup):
        freq = Candidate()
        freq.k = self.k
        freq.min_sup = min_sup
        freq.name = str(freq.k) + "-candidate" #this is to set the name so it's easy to track later.
        with open(filename, 'r') as file:
            for line in file:
                temp_line = line.strip('\n').split(',')
                for item in temp_line:
                    if item not in freq.item_sets: #check if item is in list already. Add if not.
                        if item != '': #check for empty item.
                            freq.item_sets.append(item)
                            freq.candidates[item] = freq.support
                    else:
                        freq.candidates[item] = int(freq.candidates.get(item)) + 1
        freq.item_sets, freq.candidates = self.pruning(freq.candidates, freq.item_sets, freq.min_sup)
        self.k += 1 #increment k since first candidate is already created.
        # print(freq.item_sets)
        # print(freq.candidates)
        return freq

    def pruning(self, candidates, item_sets, min_sup):
        for item in list(candidates):
            if candidates.get(item) < min_sup:
                item_sets.remove(item)
                del candidates[item]
        return item_sets, candidates

    def create_k_candidate(self, filename, min_sup, candidates, k):
        freq = Candidate()
        freq.k = self.k
        freq.min_sup = min_sup
        freq.name = str(freq.k) + "-candidate"
        freq.item_sets = combinations(candidates[k-2].item_sets, k)

        # ('a', 'c')
        # ('a', 'b')
        # ('a', 'e')
        # ('c', 'b')
        # ('c', 'e')
        # ('b', 'e')

        with open(filename,'r') as file:
            for line in file:
                temp_line = line.strip('\n').split(',')
                for comb in freq.item_sets:
                    item_name = str.join('',list(comb))
                    item_list = list(comb)
                    #print(item_list)
                    print(set(item_list).issubset(temp_line))
                    test = set(item_list).issubset(temp_line)
                    print(item_list)
                    if set(item_list).issubset(temp_line):
                        freq.candidates[item_name] = freq.support

                        #why does it stop??

                    # for item in comb:
                    #     print(comb)
                    #     if item in temp_line:
                    #         print(temp_line)
                    #         print(item + ' in')
                    #
                    #         if counter < k-1:
                    #             print('count ' + str(counter))
                    #             counter += 1
                    #         else:
                    #             counter = 0
                    #             print('add to candidates')
                    #             freq.candidates[item_name] = freq.support

                            # if counter == k-1:
                            #     print('add to candidates')
                            #     freq.candidates[item_name] = freq.support
                            # else:
                            #     print('count ' + str(counter))
                            #     counter += 1
                            #     print(counter)
        print(freq.candidates)













if __name__ == "__main__":
    filename = "test.csv"
    min_sup = 2
    apriori = Apriori(filename, min_sup)
