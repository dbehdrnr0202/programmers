def solution():
    '''
    ### Pizza Boxes
    https://www.acmicpc.net/problem/14754

    문제
    There are pizza boxes all of which have the same dimensions. The boxes are stacked in piles, forming a three- dimensional grid where the heights are all different. The view from front shows the height of the tallest pile in each column, the view from the side shows the height of the tallest pile in each row.
    What is the maximum number of pizza boxes we can remove without changing the front and side views? In the following example, Figure I.2 shows the solution of Figure I.1(a) case. In Figure I.1(a) and Figure I.2, each number (height) represents the number of boxes stacked.
    Figure I.1. (a) Grid of heights and (b) the corresponding views.
    Figure I.2. Grid of heights after removing boxes.
    Your task is to compute the maximum number of pizza boxes that can be removed without changing the original front and side views.

    입력
    Your program is to read from standard input. The input contains two integers, n and m (1 ≤ n, m ≤ 1,000), the number of rows and columns in the grid, respectively. Each of the following n lines contain m integers, the number of pizza boxes (heights) in the corresponding row. All heights are between 0 and 109 inclusive and the heights are all different.

    출력
    Your program is to write to standard output. Print exactly one line for the input. The line should contain the maximum number of pizza boxes that can be removed without changing the original views.
    '''
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    max_row = [max(row) for row in grid]
    max_col = [max(grid[i][j] for i in range(n)) for j in range(m)]
    
    total_sum = sum(map(sum, grid))
    max_row_sum = sum(max_row)
    max_col_sum = sum(max_col)

    result = total_sum - max_row_sum - max_col_sum + sum(set(max_row) & set(max_col))

    print(result)

solution()