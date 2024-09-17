def solution(n, build_frames):
    answer = []
    
    def check(answer):
        for (x, y, structure) in answer:
            # 기둥
            if structure==0:
                if y==0 or ([x-1,y,1] in answer) or ([x, y, 1] in answer) or ([x, y-1, 0] in answer):
                    continue
                return False
            # 보
            elif structure==1:
                if ([x, y-1, 0] in answer) or ([x+1,y-1, 0] in answer) or ([x-1, y, 1] in answer) and ([x+1,y,1] in answer):
                    continue
                return False
        return True
        
    for (x, y, structure, build_operation) in build_frames:
        # construct
        if build_operation:
            answer.append([x, y, structure])
            if check(answer)==False:
                answer.remove([x, y, structure])
        # destruct
        else:
            answer.remove([x, y, structure])
            if check(answer)==False:
                answer.append([x, y, structure])        
    return sorted(answer)

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])==[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]])
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])==[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]])