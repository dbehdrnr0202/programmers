def solution(edges):
    answer = []
    edge_out_list = [[] for _ in range(1000001)]
    edge_in_list = [[] for _ in range(1000001)]
    max_vertex_index = 0
    for edge in edges:
        start_vertex, end_vertex = edge
        edge_out_list[start_vertex].append(end_vertex)
        edge_in_list[end_vertex].append(start_vertex)
        max_vertex_index = max(max_vertex_index, max(start_vertex, end_vertex))
    candidate_vertex = []
    for vertex in range(max_vertex_index+1):
        if vertex==0:
            continue
        if len(edge_in_list[vertex])==0 and len(edge_out_list[vertex])>=2:
            candidate_vertex.append((vertex, len(edge_out_list[vertex])))
    return answer