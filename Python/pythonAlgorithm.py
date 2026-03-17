import random
import time
from collections import deque


class SeqList:
    def __init__(self, size=100):
        self.MAXSIZE = size
        self.length = 0
        self.data = [None for x in range(0, self.MAXSIZE)]

    def _resize(self):
        oldMaxsize = self.MAXSIZE
        self.MAXSIZE = oldMaxsize * 2
        newData = [None for i in range(self.MAXSIZE)]
        for i in range(self.length):
            newData[i] = self.data[i]
        self.data = newData
        print(f"SeqList has resized: {oldMaxsize}->{self.MAXSIZE}")

    def isFull(self):
        if self.length >= self.MAXSIZE:
            return True
        return False

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def append(self, value):
        if self.isFull():
            self._resize()
        self.data[self.length] = value
        self.length += 1

    def find(self, value):
        if self.isEmpty():
            return False
        for i in range(self.length):
            if self.data[i] == value:
                return True
        return False

    def getByIndex(self, index):
        if not isinstance(index, int):
            raise TypeError
        if self.isEmpty():
            return None
        return self.data[index]

    def insert(self, index, value):
        if self.isFull():
            self._resize()
        if not isinstance(index, int):
            raise TypeError
        if index > self.length or index < 0:
            raise AttributeError("Trying to insert into a not-exist place")
        for iCurrentIndex in range(self.length, index, -1):
            self.data[iCurrentIndex] = self.data[iCurrentIndex - 1]
        self.data[index] = value
        self.length += 1
        return True

    def display(self):
        if self.isEmpty():
            print("SeqList is empty")
            return True
        print(*(self.data[: self.length]), sep=" ", end="\n", flush=True)
        return True

    def destroyList0(self):
        self.__init__()


class LinkListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = LinkListNode(None)

    def isEmpty(self):
        if self.head.next is None:
            return True
        return False

    def pushBack(self, data):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = LinkListNode(data)

    def getElem(self, index):
        if self.isEmpty():
            raise MemoryError("Linklist is empty")
        p = self.head.next
        nCnt = 0
        while p is not None:
            if nCnt == index:
                return p.data
            nCnt += 1
            p = p.next
        raise IndexError("No such index(index too big)")

    def insert(self, index, data):
        if self.isEmpty():
            self.pushBack(data)
        else:
            p = self.head.next
            pre = self.head
            nCnt = 0
            while p.next is not None:
                if nCnt == index:
                    break
                nCnt += 1
                pre = pre.next
                p = p.next
            if p.next is None and nCnt != index:
                raise IndexError("Out of range")
            newNode = LinkListNode(data)
            newNode.next = p
            pre.next = newNode

    def delete(self, index):
        p = self.head.next
        pre = self.head
        nCnt = 0
        while p is not None:
            if nCnt == index:
                pre.next = p.next
                pdata = p.data
                del p
                return pdata
            nCnt += 1
            pre = pre.next
            p = p.next
        raise IndexError("There is no such index")

    def remove(self, data):
        p = self.head.next
        pre = self.head
        while p is not None:
            if p.data == data:
                pre.next = p.next
                del p
                return True
            pre = pre.next
            p = p.next
        raise ValueError("There is no such data")

    def _getMid(self, node):
        if node is None:
            return None
        pSlow = node
        pFast = node
        while pFast.next is not None and pFast.next.next is not None:
            pSlow = pSlow.next
            pFast = pFast.next.next
        return pSlow

    def _mergeSortRecursiveA(self, head):
        if head is None or head.next is None:
            return head
        mid = self._getMid(head)
        leftHalf = head
        rightHalf = mid.next
        mid.next = None
        left = self._mergeSortRecursiveA(leftHalf)
        right = self._mergeSortRecursiveA(rightHalf)
        return MergeLinkListA(left, right)

    def _mergeSortRecursiveD(self, head):
        if head is None or head.next is None:
            return head
        mid = self._getMid(head)
        leftHalf = head
        rightHalf = mid.next
        mid.next = None
        left = self._mergeSortRecursiveD(leftHalf)
        right = self._mergeSortRecursiveD(rightHalf)
        return MergeLinkListD(left, right)

    def getLength(self):
        nCnt = 0
        p = self.head.next
        while p:
            p = p.next
            nCnt += 1
        return nCnt

    def display(self):
        print("head", end="")
        p = self.head.next
        nCnt = 0
        while p is not None:
            nCnt += 1
            print(f" -> {p.data}", end="")
            if nCnt % 4 == 0:
                print("\n     ", end="")
            p = p.next
        print(" -> None")

    def mergeSortA(self):
        if self.head.next is not None:
            self.head.next = self._mergeSortRecursiveA(self.head.next)

    def mergeSortD(self):
        if self.head.next is not None:
            self.head.next = self._mergeSortRecursiveD(self.head.next)


def MergeLinkListN(la, lb):
    if la.head.next is None:
        return lb
    if lb.head.next is None:
        return la
    pa = la.head.next
    pb = lb.head.next
    lm = LinkList()
    while pa is not None and pb is not None:
        if pa.data > pb.data:
            lm.pushBack(pb.data)
            pb = pb.next
        else:
            lm.pushBack(pa.data)
            pa = pa.next
    while pa is not None:
        lm.pushBack(pa.data)
        pa = pa.next
    while pb is not None:
        lm.pushBack(pb.data)
        pb = pb.next
    return lm


def MergeLinkListA(la, lb):
    dummy = LinkListNode(0)
    p = dummy
    while la is not None and lb is not None:
        if la.data < lb.data:
            p.next = la
            la = la.next
        else:
            p.next = lb
            lb = lb.next
        p = p.next
    if la is not None:
        p.next = la
    if lb is not None:
        p.next = lb
    return dummy.next


def MergeLinkListD(la, lb):
    dummy = LinkListNode(0)
    p = dummy
    while la is not None and lb is not None:
        if la.data > lb.data:
            p.next = la
            la = la.next
        else:
            p.next = lb
            lb = lb.next
        p = p.next
    if la is not None:
        p.next = la
    if lb is not None:
        p.next = lb
    return dummy.next


class TreeNode:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree:
    def __init__(self):
        self.root = TreeNode(None)
        self.maxIndex = 0

    def createBiTree(self, vals):
        if len(vals) == 0:
            return None
        if vals[0] != "#":
            node = TreeNode(vals[0])
            if self.maxIndex == 0:
                self.root = node
            self.maxIndex += 1
            vals.pop(0)
            node.lchild = self.createBiTree(vals)
            node.rchild = self.createBiTree(vals)
            return node
        else:
            vals.pop(0)
            return None

    def preOrderTraverse(self, t):
        if t:
            print(f"{t.data}", end=" ")
            self.preOrderTraverse(t.lchild)
            self.preOrderTraverse(t.rchild)

    def inOrderTraverse(self, t):
        if t:
            self.inOrderTraverse(t.lchild)
            print(f"{t.data}", end=" ")
            self.inOrderTraverse(t.rchild)

    def postOrderTraverse(self, t):
        if t:
            self.postOrderTraverse(t.lchild)
            self.postOrderTraverse(t.rchild)
            print(f"{t.data}", end=" ")

    def levelTraverse(self, t):
        if t is None:
            return
        queue = []
        queue.append(t)
        while queue:
            p = queue.pop(0)
            print(f"{p.data}", end=" ")
            if p.lchild:
                queue.append(p.lchild)
            if p.rchild:
                queue.append(p.rchild)
        print()

    def locateAndPrintPath(self, t, val):
        if t is None:
            print("Empty tree")
            return False
        queue = []
        queue.append(t)
        while queue:
            p = queue.pop(0)
            print(f"{p.data}", end=" ")
            if p.lchild:
                queue.append(p.lchild)
            if p.rchild:
                queue.append(p.rchild)
            if p.lchild is None and p.rchild is None:
                print(f"\nleaf node reached, which is {p.data}")
            if p.data == val:
                print(f"\n{p.data} found")
                return True
        return False

    def countLeafNode(self, t):
        if t is None:
            print("Empty tree")
            return 0
        if t.lchild is None and t.rchild is None:
            return 1
        return self.countLeafNode(t.lchild) + self.countLeafNode(t.rchild)

    def createBiTreeLevelOrder(self, vals):
        if len(vals) == 0 or vals[0] == "#" or vals[0] is None:
            self.root = None
            return None
        root = TreeNode(vals[0])
        self.root = root
        queue = deque([root])
        i = 1
        while queue and i < len(vals):
            cur = queue.popleft()
            if i < len(vals) and vals[i] is not None:
                if vals[i] != "#":
                    cur.lchild = TreeNode(vals[i])
                    queue.append(cur.lchild)
                i += 1
            if i < len(vals) and vals[i] is not None:
                if vals[i] != "#":
                    cur.rchild = TreeNode(vals[i])
                    queue.append(cur.rchild)
                i += 1
        return root


def executionTime(func, *args, **kwargs):
    s = time.perf_counter()
    res = func(*args, **kwargs)
    e = time.perf_counter()
    duration = (e - s) * 1000
    print(f"Execution time: {duration:.2f} ms")
    return res


def main():
    op = input("Enter s for seqlist, enter l for linklist, enter t for bitree:")
    if op.lower() == "s":
        initLength = input("Enter init data, which is the MAXSIZE of SeqList:")
        myList = SeqList(int(initLength))
        for i in range(int(initLength)):
            myList.append(i)
        myList.display()
        rawInput = input("Enter insert index and value:")
        iInsertIndex, nValue = rawInput.split()
        myList.insert(int(iInsertIndex), int(nValue))
        myList.display()
        input("Enter to end")
    elif op.lower() == "l":
        llA = LinkList()
        for i in range(100):
            llA.pushBack(random.randint(0, 1000))
        llA.mergeSortA()
        llA.display()
        llA.mergeSortD()
        llA.display()
        input("Enter to end")
    elif op.lower() == "t":
        myTree = BiTree()
        vals = []
        op = input("p for pre-order construction, l for level-order construction:")
        if op.lower() == "p":
            print(
                "Input vals for bitree in pre-order(None node must be included):",
                end="",
            )
            rawInput = input()
            rawInput = list(rawInput)
            while rawInput:
                vals.append(rawInput.pop(0))
            myTree.createBiTree(vals)
            myTree.preOrderTraverse(myTree.root)
            print()
            myTree.levelTraverse(myTree.root)
            # myTree.locateAndPrintPath(myTree.root, "E")
            executionTime(myTree.locateAndPrintPath, myTree.root, "E")
            print(f"{myTree.countLeafNode(myTree.root)}")
        elif op.lower() == "l":
            print(
                "Input vals for bitree in level-order(None node must be included):",
                end="",
            )
            rawInput = input()
            rawInput = list(rawInput)
            while rawInput:
                vals.append(rawInput.pop(0))
            myTree.createBiTreeLevelOrder(vals)
            myTree.preOrderTraverse(myTree.root)
            print()
            myTree.levelTraverse(myTree.root)
            # myTree.locateAndPrintPath(myTree.root, "E")
            executionTime(myTree.locateAndPrintPath, myTree.root, "E")
            print(f"{myTree.countLeafNode(myTree.root)}")
        input("Enter to end")
    else:
        raise SyntaxError("Not a valid op")


if __name__ == "__main__":
    main()
