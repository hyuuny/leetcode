# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1과 list2를 비교하여, 더 작은 값이 왼쪽에 오도록 한다.
        if (not list1) or (list2 and (list1.val > list2.val)):
            list1, list2 = list2, list1 # Python 다중 할당
        
        # list1의 next를 재귀호출 하며 다음번 연결 리스트가 계속 스왑될 수 있도록 한다.
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1