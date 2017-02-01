import csv
import inspect, os
from itertools import combinations

class Candidate:
    def __init__(self):
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
        self.k = 1
        self.main()

    def main(self):
        _candidate, self.k = self.create_first_candidate(self._filename, self._min_sup, self.k)
        self.Candidates.append(_candidate)
        while(True):
            _candidate, self.k = self.create_k_candidate(self._filename, self._min_sup, self.Candidates, self.k)
            if len(_candidate.item_sets) == 0 or len(_candidate.candidates) == 0:
                break
            self.Candidates.append(_candidate)
        self.print_outputs(self.Candidates)

    def print_outputs(self,list_of_candidates):
        for candidate in list_of_candidates:
            for item in candidate.candidates:
                print(item, ':', candidate.candidates[item])


    def create_first_candidate(self,filename, min_sup, k):
        freq = Candidate()
        freq.k = k
        freq.min_sup = min_sup
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
        freq.k += 1 #increment k since first candidate is already created.
        return freq, freq.k

    def pruning(self, candidates, item_sets, min_sup):
        for item in list(candidates):
            if candidates.get(item) < min_sup:
                if len(item) > 1:
                    temp_item = list(item)
                else:
                    temp_item = item
                item_sets.remove(temp_item)
                del candidates[item]
        return item_sets, candidates

    def create_k_candidate(self, filename, min_sup, candidateObjects, k):
        freq = Candidate()
        freq.k = k
        freq.min_sup = min_sup

        #combinations
        combs = combinations(candidateObjects[0].item_sets, freq.k)

        #convert combinations to list
        for comb in combs:
            freq.item_sets.append(list(comb))
        lines = []
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.strip('\n').split(','))

        for comb in freq.item_sets:
            item_name = str.join('',list(comb))
            for line in lines:
                if set(comb).issubset(line):
                    if item_name not in freq.candidates:
                        freq.candidates[item_name] = freq.support
                    else:
                        freq.candidates[item_name] = int(freq.candidates.get(item_name)) + 1
        freq.item_sets, freq.candidates = self.pruning(freq.candidates, freq.item_sets, freq.min_sup)
        freq.k += 1
        return freq, freq.k


if __name__ == "__main__":
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename)) + '/'
    csv_file_name = "run_file.csv"
    #filename = input("Enter the file name with extension. For example, test.csv or test.txt\n")
    print("Make sure that your input file is name run_file.csv and is in the same folder as Apriori.py script.")
    min_sup = input("Enter the minimum support.\n")
    print("Outputs:")
    try:
        min_sup = int(min_sup)
        apriori = Apriori(path + csv_file_name, min_sup)
    except FileNotFoundError:
        print("filename error.")
    except ValueError:
        print("min_sup is not numeric.")
    input("Press Enter Key to Continue")
