
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
                if str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) == str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                    case_used = 'Case 3a:'
                elif str(cam1_matrix[len(cam1_matrix) - 1][len(cam1_matrix) - 1]) != str(cam2_matrix[len(cam2_matrix) - 1][len(cam2_matrix) - 1]):
                    case_used = 'Cannot join because it is not from the same Graph. '
            elif len(cam1_matrix) != len(cam2_matrix):
                case_used = 'Case 3b: '
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
                case_used = "Cannot be joined because last nodes cannot be different or else it is not originating from the same graph."
                temp_row = []
                result_combined_CAM.append(temp_row)
            else:
                case_used = "Cannot be joined because both matrix does not have the same number of edges."
                temp_row = []
                result_combined_CAM.append(temp_row)


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


            # two matrix are not the same size
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

        # getting CAM Code
        CamCode = ''
        if case == 3:
            CamCode = "not required to implement functionality so no CAM code will be provided."
        elif len(result_combined_CAM) > 1:
            for x in range(0, len(result_combined_CAM)):
                for y in range(0,len(result_combined_CAM)):
                    if y <= x:
                        CamCode += str(result_combined_CAM[x][y])

        else:
            CamCode = 'No Matrix Joined.'

        return case_used, result_combined_CAM, CamCode




if __name__ == "__main__":
    cam = CAM()

    graph3 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'E', 'X'], ['E', 'C', 'Y']]
    graph4 = [['B', 'C', 2], ['A', 'B', 1], ['A', 'C', 3], ['D', 'B', 'X'], ['D', 'C', 'X'], ['B', 'E', 'X'], ['E', 'A', 'Y']]

    result_matrix1, result_code1 = cam.convertToMatrix(graph3)
    print("CAM 1:")
    for x in result_matrix1:
        print(x)
    print('CAM Code: ' + result_code1)
    result_matrix2, result_code2 = cam.convertToMatrix(graph4)
    print("CAM 2:")
    for x in result_matrix2:
        print(x)
    print('The resulting code for the 2d matrix: ' + result_code2)
    case, result, code = cam.generateCAM(result_matrix1, result_matrix2)
    print(case)
    for x in result:
        print(x)
    print('CAM Code: ' + code)
    print('\n\n')
