class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 测试用例里不带头结点
def middleNode(head: ListNode):
    fast_p = low_p = head
    count = 0
    while fast_p.next is not None:
        fast_p = fast_p.next
        count += 1
        if count % 2 == 0:
            low_p = low_p.next
    if count%2 == 1:
        low_p = low_p.next
    return low_p.val


def createList(nums: [int]) -> ListNode:
    head = ListNode(nums[0])
    p = head
    for i in range(1, len(nums), 1):
        new_Node = ListNode(nums[i])
        p.next = new_Node
        p = new_Node
    return head


if __name__ == "__main__":
    with open('data.txt') as data:
        nums = data.read().split('\n')
    for i in range(len(nums)):
        data = [int(number) for number in nums[i].split(',')]
        head = createList(data)
        print(middleNode(head))
