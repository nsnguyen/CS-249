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
            cam2_matrix = cam2
            cam1_matrix = cam1
        else:
            cam1_matrix = cam2
            cam2_matrix = cam1

        case_used = "No case was used. Return Empty Array."

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
            # If both sub matrix are the same
            temp_code_cam1 = ''
            temp_code_cam2 = ''
            for x in range(0,core_size_length-1):
                for y in range(0,core_size_length-1):
                    if y <= x:
                        temp_code_cam1 += str(cam1_matrix[x][y])
                        temp_code_cam2 += str(cam2_matrix[x][y])

            if temp_code_cam1 == temp_code_cam2:
                case = 1  # set as case 1
            else:
                # return empty array if sub matrix is not the same.
                result = []
                result_combined_CAM.append(result)

        # If A has at least two edge entries in last row but B only has one
        elif (cam1_last_row_edge_count >= 2 or cam2_last_row_edge_count >= 2) and (cam2_last_row_edge_count == 1 or cam1_last_row_edge_count == 1):
            # If both sub matrix are the same
            temp_code_cam1 = ''
            temp_code_cam2 = ''
            for x in range(0,core_size_length-1):
                for y in range(0,core_size_length-1):
                    if y <= x:
                        temp_code_cam1 += str(cam1_matrix[x][y])
                        temp_code_cam2 += str(cam2_matrix[x][y])

            if temp_code_cam1 == temp_code_cam2:
                case = 2  # set as case 2
            else:
                # return empty array if sub matrix is not the same.
                result = []
                result_combined_CAM.append(result)

            # If both A and B have one edge entry in the last row
        elif cam1_last_row_edge_count == 1 and cam2_last_row_edge_count == 1:
            case = 3
            # If both sub matrix are the same and core is the same
            if cam1_matrix[:core_size_length - 1] == cam2_matrix[:core_size_length - 1]:
                # If last node for both matrix are the same
                if str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) == str(
                        cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                    case_used = 'Case 3a: '
                elif str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) != str(
                        cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                    case_used = 'Case 3b: '
            elif len(cam1_matrix) != len(cam2_matrix):
                case_used = 'Case 3a and Case 3b: '
            else:
                # return empty array if sub matrix is not the same
                result = []
                result_combined_CAM.append(result)


        if case == 1:
            case_used = 'Case 1:'

            temp_row = []
            # add last row to result.
            # if same size, same node.    (Checked)
            if len(cam1_matrix) == len(cam2_matrix) and str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) == str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):

                # add submatrix to result.
                for row in cam1_matrix[:core_size_length - 1]:
                    result_combined_CAM.append(row)


                for x in range(0, len(cam1_matrix)):
                    if str(cam1_matrix[len(cam1_matrix) - 1][x]) != "0":
                        temp_row.append(cam1_matrix[len(cam1_matrix) - 1][x])
                    elif str(cam1_matrix[len(cam1_matrix) - 1][x]) == "0":
                        temp_row.append(cam2_matrix[len(cam2_matrix) -1][x])
                result_combined_CAM.append(temp_row)

            #if same size, different node. Therefore append new row in matrix with new node
            elif len(cam1_matrix) == len(cam2_matrix) and str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) != str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                #create vertices
                vertex = []
                temp_dict_cam1 = {}
                temp_dict_cam2 = {}
                for x in range(0,len(cam1_matrix)):
                    vertex.append(cam1_matrix[x][x])
                    temp_dict_cam1[cam1_matrix[x][x]] = cam1_matrix[x]
                for y in range(0,len(cam2_matrix)):
                    temp_dict_cam2[cam2_matrix[y][y]]  = cam2_matrix[y]

                    if cam2_matrix[y][y] not in vertex:
                        vertex.append(cam2_matrix[y][y])

                #generate matrix
                matrix = [[0 for i in range(len(cam2_matrix)+1)] for i in range(len(cam2_matrix)+1)]

                #setting nodes diagonally
                x = 0
                for vertex in vertex:
                    matrix[x][x] = vertex
                    x += 1

                for x in range(0,len(matrix)):
                    for y in range(0,len(matrix)):
                        if x == y:
                            break
                        if str(matrix[x][x]) in temp_dict_cam1:
                            if str(temp_dict_cam1.get(matrix[x][x])[y]) != "0":
                                matrix[x][y] = temp_dict_cam1.get(matrix[x][x])[y]
                            else:
                                if str(temp_dict_cam1.get(matrix[x][x])[y]) not in temp_dict_cam2:
                                    continue
                                matrix[x][y] = temp_dict_cam2.get(matrix[x][x])[y]
                        elif str(matrix[x][x]) in temp_dict_cam2:
                            if temp_dict_cam2.get(matrix[x][x])[y] == matrix[x][x]:
                                break
                            matrix[x][y] = temp_dict_cam2.get(matrix[x][x])[y]

                #add matrix to result_combined_CAM
                for row in matrix:
                    result_combined_CAM.append(row)


            # two matrix are not the same size but both last row still have at least 2 edges
            else:
                # add matrix 1 to temp dict so it can be used in iteration below...
                temp_dict_cam1 = {}
                temp_dict_cam2 = {}
                for x in range(0,core_size_length):
                    temp_dict_cam1[cam1_matrix[x][x]] = cam1_matrix[x]
                for x in range(0, core_size_length):
                    temp_row = []
                    count = 0
                    for y in cam2_matrix[x]:
                        if cam2_matrix[x][x] in temp_dict_cam1:
                            if count < x:
                                count += 1
                                if str(y) == "0":
                                    #print(y)
                                    #print(temp_dict_cam1.get(cam2_matrix[x][x])[y])
                                    temp_row.append(temp_dict_cam1.get(cam2_matrix[x][x])[y])
                                else:
                                    temp_row.append(y)
                            else:
                                temp_row.append(y)
                    result_combined_CAM.append(temp_row)

                #add unexisted node back in
                for x in range(core_size_length,len(cam2_matrix)):
                    temp_dict_cam2[cam2_matrix[x][x]] = cam2_matrix[x]

                for item in sorted(temp_dict_cam2):
                    result_combined_CAM.append(temp_dict_cam2[item])


        elif case == 2:
            case_used = 'Case 2:'

            temp_row = []
            # add last row to result.
            # if same size, same node.    (Checked)
            if len(cam1_matrix) == len(cam2_matrix) and str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) == str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):

                # add submatrix to result.
                for row in cam1_matrix[:core_size_length - 1]:
                    result_combined_CAM.append(row)

                for x in range(0, len(cam1_matrix)):
                    if str(cam1_matrix[len(cam1_matrix) - 1][x]) != "0":
                        temp_row.append(cam1_matrix[len(cam1_matrix) - 1][x])
                    elif str(cam1_matrix[len(cam1_matrix) - 1][x]) == "0":
                        temp_row.append(cam2_matrix[len(cam2_matrix) - 1][x])
                result_combined_CAM.append(temp_row)

            # if same size, different node. Therefore append new row in matrix with new node
            elif len(cam1_matrix) == len(cam2_matrix) and str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) != str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                # create vertices
                vertex = []
                temp_dict_cam1 = {}
                temp_dict_cam2 = {}
                for x in range(0, len(cam1_matrix)):
                    vertex.append(cam1_matrix[x][x])
                    temp_dict_cam1[cam1_matrix[x][x]] = cam1_matrix[x]
                for y in range(0, len(cam2_matrix)):
                    temp_dict_cam2[cam2_matrix[y][y]] = cam2_matrix[y]

                    if cam2_matrix[y][y] not in vertex:
                        vertex.append(cam2_matrix[y][y])

                # generate matrix
                matrix = [[0 for i in range(len(cam2_matrix) + 1)] for i in range(len(cam2_matrix) + 1)]

                # setting nodes diagonally
                x = 0
                for vertex in vertex:
                    matrix[x][x] = vertex
                    x += 1

                for x in range(0, len(matrix)):
                    for y in range(0, len(matrix)):
                        if x == y:
                            break
                        if str(matrix[x][x]) in temp_dict_cam1:
                            if str(temp_dict_cam1.get(matrix[x][x])[y]) != "0":
                                matrix[x][y] = temp_dict_cam1.get(matrix[x][x])[y]
                            else:
                                if str(temp_dict_cam1.get(matrix[x][x])[y]) not in temp_dict_cam2:
                                    continue
                                matrix[x][y] = temp_dict_cam2.get(matrix[x][x])[y]
                        elif str(matrix[x][x]) in temp_dict_cam2:
                            if temp_dict_cam2.get(matrix[x][x])[y] == matrix[x][x]:
                                break
                            matrix[x][y] = temp_dict_cam2.get(matrix[x][x])[y]

                # add matrix to result_combined_CAM
                for row in matrix:
                    result_combined_CAM.append(row)


            # two matrix are not the same size but both last row still have at least 2 edges
            else:
                # add matrix 1 to temp dict so it can be used in iteration below...
                temp_dict_cam1 = {}
                temp_dict_cam2 = {}
                for x in range(0, core_size_length):
                    temp_dict_cam1[cam1_matrix[x][x]] = cam1_matrix[x]
                for x in range(0, core_size_length):
                    temp_row = []
                    count = 0
                    for y in cam2_matrix[x]:
                        if cam2_matrix[x][x] in temp_dict_cam1:
                            if count < x:
                                count += 1
                                if str(y) == "0":
                                    # print(y)
                                    # print(temp_dict_cam1.get(cam2_matrix[x][x])[y])
                                    temp_row.append(temp_dict_cam1.get(cam2_matrix[x][x])[y])
                                else:
                                    temp_row.append(y)
                            else:
                                temp_row.append(y)
                    result_combined_CAM.append(temp_row)

                # add unexisted node back in
                for x in range(core_size_length, len(cam2_matrix)):
                    temp_dict_cam2[cam2_matrix[x][x]] = cam2_matrix[x]

                for item in sorted(temp_dict_cam2):
                    result_combined_CAM.append(temp_dict_cam2[item])


        elif case == 3:
            # if last node is the same node, we can safely assume that the matrix should have the same size because we can only have unique nodes in a graph
            if str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) == str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):

                case_used = 'Case 3a:'
            else:
                case_used = 'Case 3b:'


        # getting awesome Code
        if case == 3:
            CamCode = "not required to implement functionality so no CAM code will be provided."
        else:
            CamCode = ''
            for x in range(0, len(result_combined_CAM)):
                for y in range(0,len(result_combined_CAM)):
                    if y <= x:
                        CamCode += str(result_combined_CAM[x][y])

        return case_used, result_combined_CAM, CamCode







if __name__ == "__main__":
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename)) + '/'

    cam = CAM()

    # # # #case 1 - Checked - 2 matrix different size, different last node
    # graph1 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'A', 'X']]
    # graph2 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'E', 'X'], ['E', 'A', 'Y']]
    #
    # result_matrix1, result_code1 = cam.convertToMatrix(graph1)
    # print("CAM 1:")
    # for x in result_matrix1:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code1)
    # result_matrix2, result_code2 = cam.convertToMatrix(graph2)
    # print("CAM 2:")
    # for x in result_matrix2:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code2)
    # case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    # print(case)
    # for x in result:
    #     print(x)
    # print('The resulting CAM Code for the two joined matrix: ' + code)
    # print('\n\n')
    #
    # # # #case 1.1 - Checked - 2 matrix same size, same last node
    # graph3 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'E', 'X'], ['E', 'C', 'Y']]
    # graph4 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'E', 'X'], ['E', 'A', 'Y']]
    #
    # result_matrix1, result_code1 = cam.convertToMatrix(graph1)
    # print("CAM 1:")
    # for x in result_matrix1:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code1)
    # result_matrix2, result_code2 = cam.convertToMatrix(graph2)
    # print("CAM 2:")
    # for x in result_matrix2:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code2)
    # case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    # print(case)
    # for x in result:
    #     print(x)
    # print('The resulting CAM Code for the two joined matrix: ' + code)
    # print('\n\n')
    #
    # ##case 1.2 - Checked - 2 matrix same size, different last node - add new node
    # graph5 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'F', 'X'], ['F', 'C', 'Y']]
    # graph6 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'E', 'X'], ['E', 'A', 'Y']]
    #
    # result_matrix1, result_code1 = cam.convertToMatrix(graph1)
    # print("CAM 1:")
    # for x in result_matrix1:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code1)
    # result_matrix2, result_code2 = cam.convertToMatrix(graph2)
    # print("CAM 2:")
    # for x in result_matrix2:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code2)
    # case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    # print(case)
    # for x in result:
    #     print(x)
    # print('The resulting CAM Code for the two joined matrix: ' + code)
    # print('\n\n')
    #
    # # #case 2 - Checked - 2 matrix  same size , same last node
    # graph7 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D','A','X']]
    # graph8 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['C','D','X'] , ['D','B','X']]
    #
    # result_matrix1, result_code1 = cam.convertToMatrix(graph1)
    # print("CAM 1:")
    # for x in result_matrix1:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code1)
    # result_matrix2, result_code2 = cam.convertToMatrix(graph2)
    # print("CAM 2:")
    # for x in result_matrix2:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code2)
    # case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    # print(case)
    # for x in result:
    #     print(x)
    # print('The resulting CAM Code for the two joined matrix: ' + code)
    # print('\n\n')
    #
    # # #case 2.1 - Checked - 2 matrix different size, different last node
    # graph9 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D','A','X']]
    # graph10 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['C','D','X'] , ['D','B','X'], ['E', 'A', 'Y'], ['E', 'B', 'Y']]
    #
    # result_matrix1, result_code1 = cam.convertToMatrix(graph1)
    # print("CAM 1:")
    # for x in result_matrix1:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code1)
    # result_matrix2, result_code2 = cam.convertToMatrix(graph2)
    # print("CAM 2:")
    # for x in result_matrix2:
    #     print(x)
    # print('The resulting code for the 2d matrix: ' + result_code2)
    # case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    # print(case)
    # for x in result:
    #     print(x)
    # print('The resulting CAM Code for the two joined matrix: ' + code)
    # print('\n\n')

    ##case 3 - Checked
    graph11 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D','A','X']]
    graph12 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['C','D','X']]

    result_matrix1, result_code1 = cam.convertToMatrix(graph11)
    print("CAM 1:")
    for x in result_matrix1:
        print(x)
    print('The resulting code for the 2d matrix: ' + result_code1)
    result_matrix2, result_code2 = cam.convertToMatrix(graph12)
    print("CAM 2:")
    for x in result_matrix2:
        print(x)
    print('The resulting code for the 2d matrix: ' + result_code2)
    case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    print(case)
    for x in result:
        print(x)
    print('The resulting CAM Code for the two joined matrix: ' + code)
    print('\n\n')


    # cam = CAM()

    # result_matrix1, result_code1 = cam.convertToMatrix(graph1)
    #
    # print("CAM 1:\n")
    # for x in result_matrix1:
    #     print(x)
    #
    # print('The resulting code for the 2d matrix: ' + result_code1)
    #
    # print('\n')
    #
    # result_matrix2, result_code2 = cam.convertToMatrix(graph2)
    #
    # print("CAM 2:\n")
    # for x in result_matrix2:
    #     print(x)
    #
    # print('The resulting code for the 2d matrix: ' + result_code2)
    #
    # print('\n')
    #
    # case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    #
    # print(case + '\n')
    # for x in result:
    #     print(x)
    # print ('\n')
    # print ('The resulting CAM Code for the two joined matrix: ' + code)

