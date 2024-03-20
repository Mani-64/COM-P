# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenHeadA,lenHeadB  = 0,0
        currentNode = headA
        while currentNode: 
            lenHeadA, currentNode = lenHeadA + 1 , currentNode.next
        
        currentNode = headB
        while currentNode: 
            lenHeadB,currentNode = lenHeadB+1 , currentNode.next
        
        bigNode = headA if lenHeadA > lenHeadB else headB
        smallNode = headA if lenHeadA <= lenHeadB else headB

        for _ in range(abs(lenHeadA - lenHeadB)): 
            bigNode = bigNode.next

        while bigNode and smallNode:
            if bigNode == smallNode: return bigNode
            bigNode,smallNode = bigNode.next, smallNode.next
    
        return None