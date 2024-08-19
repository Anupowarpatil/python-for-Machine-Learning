# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def insertNode(self,l3,sum):
            l3=l3.next
            l3=ListNode(sum)

    def addtwoNode(self,val1,val2,carry):
        sum=val1+val2+carry
        carry=sum%10
        l3=ListNode(0)
        self.insertNode(l3,sum)
        while(l3.next!=None):
            print(l3.val)
            l3 = l3.next
        return carry,l3
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1=0
        val2=0
        carry=0
        while(l1.next!=None and l2.next!=None):
            val1=l1.val
            val2=l2.val
            self.addtwoNode(val1,val2,carry)
            l1=l1.next
            l2=l2.next
            

           
    
    
            

        
        
        
        
