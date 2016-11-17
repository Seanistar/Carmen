''' issue 1
숫자열 소팅하기 - 100만개의 숫자를 소팅하되 한 번에 10만개씩 메모리에 올릴 수 있는 경우를 가정하여 프로그래밍

a) 16 bit unsigned integer 숫자를 백만개 생성하여 hexDec.bin 파일에 저장
b) 전체 크기 십만개인 unsigned integer 배열을 이용하여 hexDec.bin의 숫자를 오름차순으로 정렬하여 hexDecSort.bin 파일에 저장
c) 다시 반복되는 숫자가 많은 크기대로 다시 정렬한다. 예를 들어 1,2,2,3,3,3,4,4,5 의 정렬된 배열을 3,3,3,2,2,4,4,1,5와 같이 정렬
이 때 파일 이름을 hexDecSizeSort.bin으로 저장
'''

import random
import pprint
#import issue_2 as i2
#from ..useful import sorting


G_2X16 = 2**16
G_2X12 = 2**12
G_2X04 = 2**4

def make_hexdec(num):
    data = []
    #f = open('hexdec.dat', 'w')
    for i in range(num):
        r = random.randint(1, G_2X16)
        #data.append(r)
        yield r
        #f.write(str(r)+' ')
    #f.close()
    #return data

def make_hexdecsort():
    pass

def make_hexdecsize():
    pass

def sort_items(data):
    tosort = []
    tosort.append(data[0])

    for i in range(1, len(data)):
        idx = compute_index(tosort, data[i])
        if idx == -1:
            tosort.append(data[i])
        else:
            tosort.insert(idx, data[i])
        
    return tosort

# if x is between t1 and t2, return will be 0
# x larger than t2, return will be 1
# x smaller than t1, return will be -1
def compute_index(data, x):
    if x < data[0]:
        return 0
    elif x > data[-1]:
        return -1

    idx = 0
    while idx < len(data):
        if x >= data[idx] and x <= data[idx+1]:
            return idx + 1
        idx += 1

    #to do is using binary sort     
    return idx
    
def sort_data(data):
    mx = [[] for i in range(100)]
    for i in range(len(data)):
        n = data[i] / (G_2X16 / 10) # number of bucket is 10 
        mx[n].append(data[i])

    sorted_mx = []
    for i in range(len(mx)):
        quick_sort(mx[i])
        sorted_mx += mx[i]
        
    #pprint.pprint(sorted_mx)
    return sorted_mx

def quick_sort(items):
    if len(items) > 1: # they are considered as already sorted.
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items
        
def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)    

def number_mapper(data):
    ''' yield (number, 1) whenever find any number '''
    for number in data:
        yield (number, 1)

def number_reducer(num, counts):
    yield (num, sum(counts))
    
def assemble_same_size(data):
    from collections import defaultdict
    collector = defaultdict(list)

    for num, count in number_mapper(data):
        collector[num].append(count)

    return [result
            for num, counts in collector.items()
            for result in number_reducer(num, counts)]
       
if __name__ == '__main__':
    #sample = [534, 893, 751, 1819, 1793, 586, 1531, 3140, 49, 2143]
    #to = [49, 534, 586, 751, 893, 1531, 1793, 1819, 2143, 3140]
    #print sort_items(sample)

    # a. generate random number and save to hexDec.bin
    data = [random.randint(1, G_2X16) for _ in range(1000)] # 1000**2
    #write_file('hexdec.bin', "%s\n" % data)

    # b. to ascending sort above created array by using 1/10 array to data and save to hexDecSort.bin
    sorted_data = sort_data(data)    
    #write_file('hexDecSort.dat', "%s\n" % sorted_data)

    # c. resort by size that count an appearance frequency and save to hexDecSizeSort.bin
    group_data = assemble_same_size(sorted_data)
    #write_file('hexDecSizeSort.dat', "%s\n" % group_data)
    print group_data[][1]

    '''
    #f = open('./data/sorted_list.dat','w')
    for i in range(len(mx)):
        #mx[i].sort()
        item = sort_items(mx[i])
        print item
        #for n in range(len(mx[i])):
            #f.write(str(mx[i][n])+' ')
    #f.close()
    '''


