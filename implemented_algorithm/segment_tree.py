import math
#Build, Query, Update
global tree

def init_tree(input_arr:list[int]):
    global tree
    # n = number of nodes
    # height = ceil(log2(n))
    # tree_size = 2^(h+1)-1 or 2^(h+1) or 4n
    n = len(input_arr)
    height = math.ceil(math.log2(n))
    tree_size = 2**(height+1) - 1
    # tree_size = 2**(height+1)
    # tree_size = 4*n
    tree = [0]*tree_size
    return tree

def build(node, start_index, end_index, input_arr:list[int]):
    global tree
    # leaf node: start_index==end_index
    if start_index==end_index:
        tree[node]=input_arr[start_index]
        return tree[node]
    # node has child
    mid = (start_index+end_index) //2
    left_child = build(node*2, start_index, mid, input_arr)
    right_child = build(node*2+1, mid+1, end_index, input_arr)
    # add values of child
    tree[node]=left_child+right_child
    return tree[node]

'''
- 트리를 순회합니다.
- 노드가 나타내는 범위가 지정된 범위 밖에 있다면 0을 반환합니다.
- 노드가 나타내는 범위가 지정된 범위 내에 있다면 값을 반환합니다.
- 노드가 나타내는 범위가 지정된 범위 일부만 포함한다면 왼쪽 자식과 오른쪽 자식의 합을 반환합니다.
'''
# start_index, end_index    : 노드가 나타내는 범위
# left_range, right_range   : 지정한 범위
def query(node:int, start_index:int, end_index:int, left_range, right_range):
    global tree
    if end_index<left_range or start_index>right_range:
        return 0
    if start_index>=left_range and end_index<=right_range:
        return tree[node]
    mid = (start_index+end_index)//2
    left_child = query(node*2, start_index, mid, left_range, right_range)
    right_child = query(node*2+1, mid+1, end_index, left_range, right_range)
    return left_child+right_child


def update(node:int, start_index:int, end_index:int, index:int, changed_value:int):
    global tree
    if start_index==end_index==index:
        tree[node]=changed_value
        return
    if end_index< index or start_index> index:
        return
    mid=(start_index+end_index)//2
    left_child, right_child = node*2, node*2+1
    update(left_child, start_index, mid, index, changed_value)
    update(right_child, mid+1, end_index, index, changed_value)
    tree[node] = tree[left_child]+tree[right_child]
    return

def test():
    global tree
    input_arr = [1,2,3,4,5]
    builded_tree = [0, 15, 6, 9, 3, 3, 4, 5, 1, 2]
    init_tree(input_arr)
    build(1, 0, len(input_arr)-1, input_arr)
    for index, _ in enumerate(builded_tree):
        if builded_tree[index]!=tree[index]:
            print("incorrect")
            break
    print("build corrected")
    sum_arr = query(1, 0, len(input_arr)-1, 2, 4)
    print("sum of input_arr[2:5] (from index2 to index4)", sum_arr)
    if sum_arr!=12:
        print("incorrect")
    print("query corrected")
    update(1, 0, len(input_arr)-1, 2, 5)
    updated_tree = [0, 17, 8, 9, 3, 5, 4, 5, 1, 2]
    for index, _ in enumerate(updated_tree):
        if updated_tree[index]!=tree[index]:
            print("incorrect")
            break
    print("update corrected")

test()