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
import os

DATA_FILE = "./data/randfile.txt"
LEN = 200

def make_matrix():
    MX10 = []
    
    # with open('{}{}'.format(os.getcwd(),DATA_FILE), "r") as f:
    with open(DATA_FILE, 'r') as f:
        invalid = 0
        for num, line in enumerate(f):
            # print '{}-{}'.format(num, len(line))
            MX = [[0.0 for x in range(LEN)] for y in range(LEN)]
            value_pos, start_pos, mark_pos, value, col, row = 0, 0, 0, 0.0, 0, 0
            for s in line:
                if row > 0 or col > 0:
                    start_pos = mark_pos + 1

                if ',' == s: # 200
                    try:
                        value = float(line[start_pos:value_pos+mark_pos])
                    except:
                        invalid += 1
                    MX[row][col] = value
                    col += 1; mark_pos += value_pos; value_pos = 0                      
                elif ';' == s: # 200
                    try:
                        value = float(line[start_pos:value_pos+mark_pos])
                    except:
                        invalid += 1
                    MX[row][col] = value                  
                    row += 1; col = 0; mark_pos += value_pos; value_pos = 0
                elif '|' == s: # 10
                    try:
                        value = float(line[start_pos:value_pos+mark_pos])
                    except:
                        invalid += 1
                    MX[row][col] = value
                    mark_pos += value_pos; value_pos = 0
                    MX10.append(MX)
                    # print '{} end of line..................\n'.format(num), value
                    break;
     
                value_pos += 1

    # print "sum of invalid is: ", invalid
    return MX10

def get_eachvalue(mxs, r, c):
    entry, sm = [], 0.0
    
    for e in mxs:
        sm += e[r][c]
        entry.append(e[r][c])

    entry.sort()
    m = (max(entry) + min(entry)) / 2
    gaps = []
    for value in entry[1:8]: # except max and min value from entry
        gaps.append(abs(m - value))

    middle = min(gaps)
    index = gaps.index(middle)
    
    return (sm / len(mxs)), entry[index+1] # average, middle
    
def get_result(mxs):
    AVG = [[float(0) for x in range(LEN)] for y in range(LEN)]
    MID = [[float(0) for x in range(LEN)] for y in range(LEN)]

    for r in range(len(AVG)):
        for c in range(len(AVG[r])):
            AVG[r][c], MID[r][c] = get_eachvalue(mxs, r, c)
            
    print "Average values of the Matrix are: ", AVG[199]
    print "Middle values of the Matrix are: ", MID[198]
                
if __name__ == '__main__':
    mxs = make_matrix()
    get_result(mxs)

    
    
        


