import random
import pprint
import issue_2 as i2

G_2X16 = 2**16
G_2X12 = 2**12
G_2X04 = 2**4

def make_hexdec(num):
    data = []
    #f = open('hexdec.dat', 'w')
    for i in range(num):
        r = random.randint(0, G_2X16)
        data.append(r)
        #f.write(str(r)+' ')
    #f.close()
    return data

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
    
def make_hashtable(data):
    # Creates a list containing 2**4 lists, each of 2*12 items, all set to 0
    #w, h = 2**12, 2**4 
    #mx = [[0 for x in range(w)] for y in range(h)]
    #mx = [[0]*w for i in range(h)]
    mx = [[] for i in range(G_2X04)]
    
    for i in range(len(data)):
        #n = i2.f_log(data[i], w)
        n = data[i] / G_2X12
        mx[n].append(data[i])

    pprint.pprint(mx)
    return mx
    
if __name__ == '__main__':
    #sample = [534, 893, 751, 1819, 1793, 586, 1531, 3140, 49, 2143]
    # to = [49, 534, 586, 751, 893, 1531, 1793, 1819, 2143, 3140]
    #print sort_items(sample)
    
    data = make_hexdec(100)
    mx = make_hashtable(data)

    #f = open('./data/sorted_list.dat','w')
    for i in range(len(mx)):
        #mx[i].sort()
        item = sort_items(mx[i])
        print item
        #for n in range(len(mx[i])):
            #f.write(str(mx[i][n])+' ')
    #f.close()
    
    '''
    f = open('hexDec.bin', 'r')
    print(f.read())
    f.close()
    '''

