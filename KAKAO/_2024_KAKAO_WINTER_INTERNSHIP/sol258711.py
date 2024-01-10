def solution(edges):
    answer = [0, 0, 0, 0]
    edge_out_list = [[] for _ in range(1000001)]
    edge_in_list = [[] for _ in range(1000001)]
    max_vertex_index = 0
    for edge in edges:
        start_vertex, end_vertex = edge
        edge_out_list[start_vertex].append(end_vertex)
        edge_in_list[end_vertex].append(start_vertex)
        max_vertex_index = max(max_vertex_index, max(start_vertex, end_vertex))
    added_vertex = 0
    for vertex in range(max_vertex_index+1):
        if vertex==0:
            continue
        if len(edge_in_list[vertex])==0 and len(edge_out_list[vertex])>=2:
            answer[0]=added_vertex = vertex
            total_graph=len(edge_out_list[vertex])
            break
    for out_going_vertex in edge_out_list[added_vertex]:
        edge_in_list[out_going_vertex].remove(added_vertex)
    for vertex in range(max_vertex_index+1):
        #if vertex==edge_out_list[added_vertex]:
        #    continue
        if vertex==0 or vertex==added_vertex:
            continue
        if len(edge_out_list[vertex])==0:
            answer[2]+=1
        elif len(edge_out_list[vertex])==2 and len(edge_in_list[vertex])==2:
            answer[3]+=1
    answer[1] = total_graph-(answer[2]+answer[3])
    return answer