class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[{self.val}]->{self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        return str(self.head)

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverseList(self, head:ListNode) -> ListNode:
        if not head:
            return head
        temp = head
        teil = ListNode(val=head.val)
        while temp.next:
            temp = temp.next
            teil = ListNode(val=head.val,next=teil)
        return teil

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp = ListNode()
        tail = temp
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2= list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return temp.next



if __name__ == '__main__':
    linked_list = LinkedList()
    temp = ListNode(1)
    linked_list.head = temp
    for i in range(2, 5):
        temp.next = ListNode(i)
        temp = temp.next
    print(linked_list)
    num = LinkedList.length(linked_list)
    print(num)
