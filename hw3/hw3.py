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
        unique_nodes = vertices.__len__()
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
        left_cam = cam1
        right_cam = cam2
        left_cam_count = left_cam.__len__()
        right_cam_count = right_cam.__len__()
        result_join_matrix = []
        case = 0 # initialize case 0 at beginning




        print(left_cam.__len__())

        print(cam1[3] == cam2[3])

        return result_join_matrix





if __name__ == "__main__":
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename)) + '/'
    graph1 = [
            ['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['C', 'D', 'X'], ['D', 'A', 'X']
              ]

    graph2 = [
            ['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3] ,['C','D','X'] , ['D','B','X']
              ]

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

    result_matrix3 = cam.generateCAM(result_matrix1, result_matrix2)

    # for x in result_matrix3:
    #     print(x)




