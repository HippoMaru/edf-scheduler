class Node:
    def __init__(self, task):
        self.task = task
        self.next = None
        self.prev = None


class TaskList:
    def __init__(self, *tasks):
        self.head = None
        self.tail = None
        for task in tasks:
            self.insert_task(task)

    def insert_task(self, task):
        if not self.head:
            self.head = Node(task)
            self.tail = self.head
            return
        node = Node(task)

        if task.deadline < self.head.task.deadline:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return

        prev = self.head
        cur = self.head.next
        while cur:
            if task.deadline < cur.task.deadline:
                node.next = cur
                prev.next = node
                cur.prev = node
                return
            prev = cur
            cur = cur.next

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove_task(self, task):
        print(task)
        print(self.head.task)
        if task == self.head.task:
            self.cut_head()
            return
        prev = self.head
        cur = prev.next
        while cur.task != task:
            prev = cur
            cur = prev.next
        prev.next = cur.next
        if cur.next:
            cur.next.prev = prev
        if cur == self.tail:
            self.tail = prev

    def cut_head(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def __str__(self):
        if not self.head:
            return "empty list"
        cur = self.head
        res = str(cur.task)
        while cur.next:
            cur = cur.next
            res += f' <-> {cur.task}'
        return res

    def __repr__(self):
        return self.__str__()
