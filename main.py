class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = "LinkedList(["
        cur = self.head
        while cur is not None:
            s += repr(cur.get_data()) + ", "
            cur = cur.get_next()
        s = s.strip(", ") + "])"
        return s

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

list = OrderedList()

fruit_text = open("fruit_file.txt", "r")
fruit_list = []
fruit_line = fruit_text.read()
fruit_split = fruit_line.split("\n")


for line in fruit_split:
    if "insert" in line:
        line_split = line.split()
        key = line_split[1]
        list.add(key)
        print(str(list))
    elif "delete" in line:
        key = line.split()[1]
        if list.search(key):
            list.remove(key)
            print(str(list))
