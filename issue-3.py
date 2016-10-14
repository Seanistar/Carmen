# issue 3
'''
there are 10 matrixs in 200*200.
it needs to make two outpus.
one is would be a matrix that is caculated by average value.
the other would be a matrix that is caculated by middle value.

첨부파일에는 200*200 행렬 10개가 있습니다.
이를 읽어서 다음과 같은 계산을 하는 프로그램을 짜세요.
입력 받은 행렬 10개를 A, B, C, D, ..., J 라고 이름을 붙였을 때에
10개 행렬들의 평균값(X)과 중간값(Y)을 계산한 결과 행렬(200*200)을 출력해야합니다.
이 때에 X(i,j)는 A(i,j), B(i,j), C(i,j), D(i,j), ..., J(i,j) 의 평균값이고
Y(i,j)는 A(i,j), B(i,j), C(i,j), D(i,j), ..., J(i,j)의 중간값입니다.
단, 입력값에 오류가 있을 경우 적절히 보정하셔야하고 출력값은 유한한 실수여야합니다.

첨부파일은 다음과 같은 모양입니다.
행렬의 성분값은 ,로 구분되고 줄바꿈은 ;로 구분되며 서로 다른 행렬은 |로 구분됩니다.
아래 예시는 2*2 행렬 3개를 적은 것입니다.
1,2;3,4|
0,1;1,0|
5,3;3,1|
'''
import pprint

DATA_FILE = "./data/randfile.txt"
LEN = 20
MX = [[float(0) for x in range(LEN)] for y in range(LEN)]

def test():

    with open(DATA_FILE, "r") as f:
        
        for row, line in enumerate(f):
            value_pos, mark_pos, pos_pipe, col = 0, 0, 0, 0
            for s in line:
                if ',' == s:
                    if col > 0:
                        MX[row][col] = float(line[mark_pos+1:mark_pos+value_pos])
                    else:
                        MX[row][col] = float(line[mark_pos:mark_pos+value_pos])

                    #MX[row][col] = float(line[mark_pos:mark_pos+value_pos])
                    col += 1; mark_pos += value_pos; value_pos = 0

                if col == LEN:
                    break;
                
                value_pos += 1
            
    pprint.pprint(MX)           
            
def get_value(s):
    
    

    print lines
test()
        


