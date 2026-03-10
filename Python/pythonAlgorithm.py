import random


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


def main():
    op = input("Enter s for seqlist, enter l for linklist:")
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
        input("请按回车继续...")
    elif op.lower() == "l":
        llA = LinkList()
        for i in range(100):
            llA.pushBack(random.randint(0, 1000))
        llA.mergeSortA()
        llA.display()
        llA.mergeSortD()
        llA.display()
        input("请按回车继续...")
    else:
        raise SyntaxError("Not a valid op")


if __name__ == "__main__":
    main()
