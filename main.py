from mtree_ import MTree


def d_int(x,y):
    return abs(x-y)

def main():
    tree = MTree(d_int, max_node_size=4)
    tree = MTree(d_int, max_node_size=4)   # create an empty M-tree
    tree.add(1)           # add object 1 to the tree
    tree.add_all([5, 9])  # add objects 5 and 9
    print(list(tree.search(10)))       # search the object closest to 10. Will return 9
    print(list(tree.search(9,2)))   # search the two objects closest to 9.
    #draw()
    #tree.printTree()
main()
