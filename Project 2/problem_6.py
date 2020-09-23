class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def size(self):
        return self.size


def union(llist_1, llist_2):
    # Your Solution Here

    if llist_1.head is None and llist_2.head is None:
        return LinkedList()

    hashmap = dict()
    result = LinkedList()
    curr = llist_1.head
    while curr is not None:
        hashmap[curr.value] = 0
        curr = curr.next

    curr = llist_2.head
    while curr is not None:
        hashmap[curr.value] = 0
        curr = curr.next

    for key in hashmap:
        result.append(key)
    return result


def intersection(llist_1, llist_2):
    # Your Solution Here

    if llist_1.head is None or llist_2.head is None:
        return LinkedList()

    hashmap = dict()
    result = LinkedList()
    curr = llist_1.head
    while curr is not None:
        hashmap[curr.value] = 0
        curr = curr.next

    curr = llist_2.head
    while curr is not None:
        if hashmap.get(curr.value, 1) == 0:  # to avoid duplicate value
            hashmap[curr.value] = 1
            result.append(curr.value)
        curr = curr.next
    return result


if __name__ == "__main__":
    # Test case 1
    print("Test 1")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union")
    print(union(linked_list_1, linked_list_2))  # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    print("Intersection")
    print(intersection(linked_list_1, linked_list_2)) # 6 -> 4 -> 21 ->

    # Test case 2
    print("Test 2")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("Union")
    print(union(linked_list_3, linked_list_4)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    print("Intersection")
    print(intersection(linked_list_3, linked_list_4)) # nothing

    # Test case 3
    print("Test 3")
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print("Union")
    print(union(linked_list_5, linked_list_6))  # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 ->
    print("Intersection")
    print(intersection(linked_list_5, linked_list_6))  # nothing

    # Test case 4
    print("Test 4")
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [3, 2, 4, 35, None, None, 65, 6, 4, 3, 23]
    element_2 = [3, None, None, None]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    print("Union")
    print(union(linked_list_7, linked_list_8))  # 3 -> 2 -> 4 -> 35 -> None -> 65 -> 6 -> 23 ->
    print("Intersection")
    print(intersection(linked_list_7, linked_list_8))  # 3 -> None ->