# emplementing all the functions
def create_set():
    my_set = {1,2,3,4,5}
    print(my_set)

def add_element():
    my_set = {2,4,6,8,10}
    my_set.add((11,13))
    print(my_set)

def remove_element():
    my_set ={1,2,3,4,5}
    my_set.remove(4)
    print(my_set)

def clear_set():
    my_set={1,3,5,7,9}
    my_set.clear()
    print(my_set)

def set_union():
    set1 = {1,2,3,4}    
    set2 = {5,6,7,8}
    my_set = set1.union(set2)
    print(my_set)

def set_intersection():
    set1 = {1,2,3,4,5}
    set2 = {4,5,6,7,8}
    my_set = set1.intersection(set2)
    print(my_set)

def set_differecne():
    set1 = {2,4,6,8}
    set2 ={1,2,3,4}
    my_set = set1.difference(set2)
    print(my_set)

def subset():
    set1 = {1,2,3,4,5}
    set2 = {1,2,3}
    my_set = set2.issubset(set1)
    print(my_set)

def superset():
    set1 = {1,2,3,4,5}
    set2 = {2,3,4}
    my_set = set1.issuperset(set2)
    print(my_set)


# code runner
if __name__ == '__main__':
    create_set()
    add_element()
    remove_element()
    clear_set()
    set_union()
    set_intersection()
    set_differecne()
    subset()
    superset()
