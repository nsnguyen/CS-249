Name: Nguyen Nguyen
ID: 004870721

Problem C:
Goal:
    The goal of this design two functions based on FFSM algorithm. The first function, convertToMatrix(),
    will take in an array of 3-item arrays (node1, node2, edge) and convert it to a CAM matrix.
    The second function, generateCAM(), takes in two matrices created from the first function,
    and determine which case it can be joined (case1, case2, case3).

Assumption:
    All nodes are unique, meaning the CAM matrix cannot have the same node with the same label twice.
    Another assumption is that the sorted() function in Python is sorted lexicographically.
    If the join case does not match, it will return an empty array. If the join case 1, and join case 2 are matched,
    then the function will return a joined matrix, a CAM code, and the case which is used.

    Case 1 is used when both matrix have same number of edges (does not need to have same number of nodes),
    last row of each matrix must have at least 2 edges,
    the MP submatrix (core) for both matrix are the same, and the last node are the same.
    Because this assignment is given that the node is unique,
    we can safely assume both matrix must have the same size in order to join with Case 1.

    Case 2 is used when the last row of one of the matrix has only one edge and the other has at least 2 edges.
    Case 2 does not need to have both same matrix size,
    and the last node can be different. It will generate a new row with the new node.

    Case 3 is used when both matrix has only one edge for the last row.
    If both matrix has the same size, and the last nodes are the same then this will be case 3a.
    If the last nodes are not the same, then we can safely assume that both matrix are not from the original graph.
    In this assignment, we cannot have the same nodes twice in the graph thus it's difficult to have execute case 3a and case 3b.



How to Run:
    This programming assignment is written in Python 3.6 using core libraries only. IDE used is PyCharm,
    To run this script, please make sure that you are in the folder where this script is located in terminal.

    Execute 'python HW_3C.py' and it will display a test scenario.
    In order to input other test codes, open the python script in textPad or an IDE.
    Go to the bottom where "__main__": is. Note that this is where the python will begin reading the code, similar how main function works in C++
    Replace graph1 and graph2 variables with array of 3-item arrays. Save the file and execute the script again in terminal, or run it in an IDE.


    CAM 1:
['A', 0, 0, 0, 0]
['1', 'B', 0, 0, 0]
['3', '2', 'C', 0, 0]
[0, 'X', 'X', 'D', 0]
[0, 'X', 'Y', 0, 'E']
CAM Code: A1B32C0XXD0XY0E
CAM 2:
['A', 0, 0, 0, 0]
['1', 'B', 0, 0, 0]
['3', '2', 'C', 0, 0]
[0, 'X', 'X', 'D', 0]
['Y', 'X', 0, 0, 'E']
The resulting code for