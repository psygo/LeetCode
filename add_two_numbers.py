# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1, l2):
    mainL = l1 if len(l1) > len(l2) else l2
    otherL = l2 if len(l1) > len(l2) else l1

    currentMain = mainL
    currentOther = otherL
    carry = 0
    result = []
    while True:
        currentMainValue = currentMain.val
        currentOtherValue = currentOther.val if currentOther else 0

        sum = currentMainValue + currentOtherValue + carry
        carry = 0 if sum < 10 else 1
        result.append(sum - 10)

        currentMain = currentMain.next
        currentOther = currentOther.next

        if not currentMain:
            break

    return result


print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
