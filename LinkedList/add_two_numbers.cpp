class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int val1 = 0, val2 = 0, digit = -1, carry = 0;
        ListNode* result = new ListNode;
        ListNode* temp = result;
        
        while (l1 != nullptr || l2 != nullptr || carry == 1)
        {
            if (l1 == nullptr)
                val1 = 0;
            else
            {
                val1 = l1->val;
                l1 = l1->next;
            }
            
            if (l2 == nullptr)
                val2 = 0;
            else
            {
                val2 = l2->val;
                l2 = l2->next;
            }
            
            digit = (val1 + carry) + val2;
            carry = digit / 10;
            digit %= 10;
            result->val = digit;
            
            if (l1 == nullptr && l2 == nullptr && carry == 0)
                result->next = nullptr;
            else
            {
                result->next = new ListNode;
                result = result->next;
            }
        }
        
        result = temp;
        return result;
    }
};
