import myMath as mm
import usefulFunc as uf
import nose
import sorting as sort
import logging
 
logging.basicConfig(level=logging.INFO)

def test_power():
    assert mm.f_power(2,3) == 8

def test_sqrt():
    assert int(mm.f_sqrt(4)) == 2, 'reason why this failed'

def test_sorting():
    import random
    random_items = [random.randint(1, 100) for _ in range(100)]

    log = logging.getLogger('SORT')
    log.info('Before')
    #log.info(random_items)

    sorts = { "Bubble":sort.bubble_sort, "Insertion":sort.insertion_sort, "Built-In":sorted,
              "Merge":sort.merge_sort, "Quick":sort.quick_sort, "Heap":sort.heap_sort }
    
    for key, _ in sorts.iteritems():
        items = random_items[:]
        time = uf.time_it(sorts[key], items)
        log.info('After ' + key + ': ' + str(time))
        #log.info(items)

'''  INFO:SORT: size of 100 | 1,000 | 10,000
     Insertion: 0.878810882568 | 92.4010276794 | 9639.51587677
     Built-In:  0.025033950805 | 0.28395652771 | 3.4019947052
     Merge:     0.546216964722 | 7.10797309875 | 88.497877121
     Heap:      0.375986099243 | 5.29217720032 | 70.8267688751
     Quick:     0.375032424927 | 6.17504119873 | 188.364982605
     Bubble:    1.16610527039  | 112.60509491  | 11508.1179142
'''

if __name__ == "__main__":

    nose.runmodule()

