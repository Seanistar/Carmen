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
    random_items = [random.randint(1, 100) for c in range(1000)]

    log = logging.getLogger('SORT')
    log.info('Before')
    #log.info(random_items)

    sorts = {"Bubble":sort.bubble_sort, "Insertion":sort.insertion_sort, "Built-In":sorted,
             "Merge":sort.merge_sort, "Quick":sort.quick_sort, "Heap":sort.heap_sort}
    
    for key, value in sorts.iteritems():
        items = random_items[:]
        time = uf.time_it(sorts[key], items)
        log.info('After ' + key + ': ' + str(time))
        #log.info(items)

if __name__ == "__main__":

    nose.runmodule()

