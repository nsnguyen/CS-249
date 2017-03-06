#CS-249 HW 3

# Implement a program that solves a general case of CAM.
#
# 1. Implement a function named convertToMatrix that takes in a array of edges and converts
# it into a CAM adjacency matrix. Each edge will be represented as a 3-item list. ie: [0,1,'X']
# will represent an edge from 0 to 1 with a value of X. ['B','C',2] will represent
# an edge from 'B' to 'C' with a value of 2. You may assume the graph represented in
# an undirected graph and each node is unique in the graph. The output of your program
# must be 2D array or list in your language. In addition, the function must also print the
# code equivalence of the adjacency matrix in string format.



# 2. Implement a function called generateCAM that takes in two CAM adjacency matrix
# representation you wrote in C1 that creates a new matrix using CAM to handle join case
# 1 (Both A and B have at least two edge entries in the last row) and join case 2 (A has at
# least two edge entries in last row but B has only one).
# The output of your program must be 2D array or list in your language. If the join case
# is not 1 or 2, output a blank 2D array or list.
# The function must also print a string of the join case it matched. If the graph matches
# join case 1, print "Case 1". If the graph matches join case 2, print "Case 2". If the graph
# matches join case 3a, print "Case 3a". If the graph matches join case 3b, print "Case
# 3b". Note you do not have to implement the actual functionality of case 3 join.


import csv
import inspect, os
import itertools


class Edge:
    def __init__(self):
        self.Node1 = "1"
        self.Node2 = "2"
        self.Edge = "X"



class CAM:
    def convertToMatrix(self, edges):
        vertices = []
        edge_dict = dict()
        for edge in edges:
            if str(edge[0]) == str(edge[1]):
                continue  # skip iteration because node 1 and node 2 cannot be the same. Doesn't make sense.
            if str(edge[0]) not in vertices:
                vertices.append(str(edge[0]))  # add this to vertex which will be then be used in diagonal order.
            if str(edge[1]) not in vertices:
                vertices.append(str(edge[1]))  # add second node to vertex list
            obj = Edge()
            obj.Node1 = str(edge[0]).strip()
            obj.Node2 = str(edge[1]).strip()
            obj.Edge = str(edge[2]).strip()
            obj1 = Edge()  # there's gotta be a better implementation but no time to fix it...
            obj1.Node1 = str(edge[1]).strip()
            obj1.Node2 = str(edge[0]).strip()
            obj1.Edge = str(edge[2]).strip()
            edge_dict.setdefault(obj.Node1,[]).append(obj)  # add obj to dictionary so it can be found easily.
            edge_dict.setdefault(obj1.Node1,[]).append(obj1)

        # sort the unique vertices
        vertices = sorted(vertices) # python sort by lexicographic order by default. See python documentation

        # initialize 2d matrix
        unique_nodes = len(vertices)
        matrix = [[0 for i in range(unique_nodes)] for i in range(unique_nodes)]

        # setting nodes across diagonally
        x = 0
        for vertex in vertices:
            matrix[x][x] = vertex
            x += 1

        #setting edges now.
        for x in range(1,unique_nodes):
            node2 = matrix[x][x]
            for y in range(0,unique_nodes):
                node1 = matrix[y][y]
                if x == y:
                    break
                if node1 in edge_dict:
                    for item in edge_dict[node1]:
                        if node2 == item.Node2:
                            matrix[x][y] = item.Edge

        # getting awesome Code
        CamCode = ''
        for x in range(0, unique_nodes):
            for y in range(0,unique_nodes):
                if y <= x:
                    CamCode += str(matrix[x][y])
        return matrix, CamCode





    def generateCAM(self,cam1, cam2):

        if(len(cam2) > len(cam1)):  # if cam2 is bigger than swap it.. this will help with case 2
            cam2_matrix = cam1
            cam1_matrix = cam2
        else:
            cam1_matrix = cam1
            cam2_matrix = cam2

        core_size_length = min(len(cam1_matrix), len(cam2_matrix)) # this will use smaller matrix size to compare submatrix
        case = 0
        cam1_last_row_edge_count = -1  # to not count node
        cam2_last_row_edge_count = -1  # to not count node
        result_combined_CAM = []

        # Case 1: both A and B have at least two edge entries in the last row.
        # Case 2: A has at least two edge entries but B only has at least one.
        # Case 3: both A and B have one edge entry in the last row.

        for x in cam1_matrix[len(cam1_matrix) - 1]:  # loop through last row to count edges cam1
            if str(x) != "0":
                cam1_last_row_edge_count += 1
        for y in cam2_matrix[len(cam2_matrix) - 1]:  # loop through last row to count edges cam2
            if str(y) != "0":
                cam2_last_row_edge_count += 1

        # If Both A and B have at least two edge entries in last row
        if cam1_last_row_edge_count >= 2 and cam2_last_row_edge_count >= 2:

            #print(len(cam1_matrix))
            #print(len(cam2_matrix))
            # If both sub matrix are the same
            temp_code_cam1 = ''
            temp_code_cam2 = ''
            for x in range(0,core_size_length-1):
                for y in range(0,core_size_length-1):
                    if y <= x:
                        temp_code_cam1 += cam1_matrix[x][y]
                        temp_code_cam2 += cam2_matrix[x][y]

            if temp_code_cam1 == temp_code_cam2:
                case = 1  # set as case 1
            else:
                # return empty array if sub matrix is not the same.
                result = []
                result_combined_CAM.append(result)

        # If A has at least two edge entries in last row but B only has one
        elif cam1_last_row_edge_count >= 2 and cam2_last_row_edge_count == 1:
            # If both sub matrix are the same
            if cam1_matrix[:core_size_length - 1] == cam2_matrix[:core_size_length - 1]:
                case = 2  # set as case 2
            else:
                # return empty array if sub matrix is not the same.
                result = []
                result_combined_CAM.append(result)

            # If both A and B have one edge entry in the last row
        elif cam1_last_row_edge_count == 1 and cam2_last_row_edge_count == 1:
            # If both sub matrix are the same
            if cam1_matrix[:core_size_length - 1] == cam2_matrix[:core_size_length - 1]:
                case = 3
            else:
                # return empty array if sub matrix is not the same
                result = []
                result_combined_CAM.append(result)


        #print(case)

        if case == 1:
            print('Using Case 1:')

            # add submatrix to result.
            for row in cam1_matrix[:core_size_length - 1]:
                result_combined_CAM.append(row)

            temp_row = []
            # add last row to result.
            # if last node is same node so this must means that the two matrix are the same size, because the nodes are unique.
            if str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) == str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                for x in range(0, len(cam1_matrix)):
                    if str(cam1_matrix[len(cam1_matrix) - 1][x]) != "0":
                        temp_row.append(cam1_matrix[len(cam1_matrix) - 1][x])
                    elif str(cam1_matrix[len(cam1_matrix) - 1][x]) == "0":
                        temp_row.append(cam2_matrix[len(cam2_matrix) -1][x])
                result_combined_CAM.append(temp_row)
            # else if last node is not the same, this means that the two matrix are not the same size but both last row still have at least 2 edges
            else:
                temp_dict = {}
                for x in range(core_size_length - 1, len(cam1_matrix)):
                    temp_dict[str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1])] = cam1_matrix[len(cam1_matrix) - 1]

                for y in range(core_size_length - 1, len(cam2_matrix)):
                    if str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]) not in temp_dict:
                        temp_dict[str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1])] = cam2_matrix[len(cam2_matrix) - 1]





                # add all all nodes to graph...
                for item in sorted(temp_dict):
                    result_combined_CAM.append(temp_dict[item])



        elif case == 2:
            print('Using Case 2:')





        for x in result_combined_CAM:
            print(x)


            # cam1
            # ['A', 0, 0, 0]
            # ['1', 'B', 0, 0]
            # ['3', '2', 'C', 0]
            # ['X', 0, 'X', 'D']
            #
            # cam2
            # ['A', 0, 0, 0]
            # ['1', 'B', 0, 0]
            # ['3', '2', 'C', 0]
            # [0, 'X', 'X', 'D']










if __name__ == "__main__":
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename)) + '/'

    # #case 1
    # graph1 = [
    #         #['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'A', 'X']
    #          ['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['C', 'D', 'X'], ['D', 'A', 'X']
    #           ]
    #
    # graph2 = [
    #         #['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['D','B','X']
    #          ['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['C','D','X'] , ['D','B','X']
    #           ]


    # #case 1.1
    # graph1 = [
    #         #['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'A', 'X']
    #          ['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3]
    #           ]
    #
    # graph2 = [
    #         #['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['D','B','X']
    #           ['A', 'B', 1], ['A', 'C', 3] ,['C','D','X'] , ['D','B','X']
    #           ]

    cam = CAM()

    result_matrix1, result_code1 = cam.convertToMatrix(graph1)

    print("Graph1:")
    for x in result_matrix1:
        print(x)

    print('The resulting code for the 2d matrix above is: ' + result_code1)

    print('\n')

    result_matrix2, result_code2 = cam.convertToMatrix(graph2)

    print("Graph2:")
    for x in result_matrix2:
        print(x)

    print('The resulting code for the 2d matrix above is: ' + result_code2)

    print('\n')

    cam.generateCAM(result_matrix1, result_matrix2)

    # for x in result_matrix3:
    #     print(x)

