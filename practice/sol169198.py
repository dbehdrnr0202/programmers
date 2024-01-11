'''
당구대의 가로 길이 m, 
세로 길이 n과 
머쓱이가 쳐야 하는 공이 놓인 위치 좌표를 나타내는 두 정수 startX, startY, 
그리고 매 회마다 목표로 해야하는 공들의 위치 좌표를 나타내는 정수 쌍들이 들어있는 2차원 정수배열 balls
'''
def ccw(p1,p2,p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1]))

def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        ballX, ballY = ball
        dist = 10000000000
        # 상
        if not (ballX==startX and ballY>startY):
            dist = min(dist, (ballX-startX)**2+(2*n-ballY-startY)**2)
        # 하
        if not (ballX==startX and ballY<startY):
            dist = min(dist, (ballX-startX)**2+(-ballY-startY)**2)
        # 좌
        if not (ballX<startX and ballY==startY):
            dist = min(dist, (-ballX-startX)**2+(ballY-startY)**2)
        # 우
        if not (ballX>startX and ballY==startY):
            dist = min(dist, (2*m-ballX-startX)**2+(ballY-startY)**2)
        
        '''
        targets = [
            (ballX, 2*n-ballY), # 상
            (ballX, -ballY),    # 하
            (2*m-ballX, ballY), # 우
            (-ballX, ballY)]    # 좌
        corners = [(0, n), (0, 0), (m, 0), (m, n)]
        for corner in corners:
            if ccw(corner, ball, (startX, startY))==0:
                temp_dist = (2*m-targetX-startX)**2+(2*n-targetY-startY)**2
                dist = min(temp_dist, dist)
        '''
        answer.append(dist)
    return answer