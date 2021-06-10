class _Node:
    __slots__ = '_element','_left','_right'

    def __init__(self,e,left=None,right=None):
        self._element=e
        self._left=left
        self._right=right

class binarySearchTreeIter():

    def __init__(self):
        self._root = None

    def insert(self,troot,e):
        temp = None

        while troot:
            temp = troot
            if e == troot._element:
                return
            elif e < troot._element:
                troot=troot._left
            elif e > troot._element:
                troot=troot._right

        new = _Node(e)
        if self._root:
            if e > temp._element:
                temp._right = new
            elif e < temp._element:
                 temp._left = new
        else:
            self._root = new

    def rinsert(self,troot,e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left,e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right,e)
        else:
            new = _Node(e)
            troot = new
        #print(troot,troot._left,troot._right,troot._element)
        return troot

    def searchItr(self,troot,key):
        while troot:
            if key == troot._element:
                return True
            if key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def searchRec(self,troot,key):
        if troot:
            if troot._element == key:
                return True
            if key < troot._element:
                return self.searchRec(troot._left,key)
            elif key > troot._element:
                return self.searchRec(troot._right,key)
        return False

    def delete(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right
        if not p:
            return False
        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p._left = s
            #pp = ps
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c





    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

B_itr = binarySearchTreeIter()
B_itr._root = B_itr.rinsert(B_itr._root,50)
B_itr.rinsert(B_itr._root,10)
B_itr.rinsert(B_itr._root,30)
B_itr.rinsert(B_itr._root,20)
B_itr.rinsert(B_itr._root,70)
B_itr.rinsert(B_itr._root,60)
B_itr.rinsert(B_itr._root,55)
B_itr.inorder(B_itr._root)
#print(B_itr.searchItr(B_itr._root,100))
#print(B_itr.searchRec(B_itr._root,10))
B_itr.delete(70)
print()
B_itr.inorder(B_itr._root)


