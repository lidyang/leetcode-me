## 题目地址
https://leetcode-cn.com/problems/two-sum/

## 题目描述

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？



## 思路

设立一个表示进位的变量carried，建立一个新链表，
把输入的两个链表从头往后同时处理，每两个相加，将结果加上carried后的值作为一个新节点到新链表后面。


## 关键点解析

1. 链表这种数据结构的特点和使用

2. 用一个carried变量来实现进位的功能，每次相加之后计算carried，并用于下一位的计算

## 代码
* 语言支持：Java，Python

Java:
```java
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  if (l1 === null || l2 === null) return null

  // 使用dummyHead可以简化对链表的处理，dummyHead.next指向新链表
  let dummyHead = new ListNode(0)
  let cur1 = l1
  let cur2 = l2
  let cur = dummyHead // cur用于计算新链表
  let carry = 0 // 进位标志

  while (cur1 !== null || cur2 !== null) {
    let val1 = cur1 !== null ? cur1.val : 0
    let val2 = cur2 !== null ? cur2.val : 0
    let sum = val1 + val2 + carry
    let newNode = new ListNode(sum % 10) // sum%10取模结果范围为0~9，即为当前节点的值
    carry = sum >= 10 ? 1 : 0 // sum>=10，carry=1，表示有进位
    cur.next = newNode
    cur = cur.next

    if (cur1 !== null) {
      cur1 = cur1.next
    }

    if (cur2 !== null) {
      cur2 = cur2.next
    }
  }

  if (carry > 0) {
    // 如果最后还有进位，新加一个节点
    cur.next = new ListNode(carry)
  }

  return dummyHead.next
};
```
C++
> C++代码与上面的JavaScript代码略有不同：将carry是否为0的判断放到了while循环中
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ret = nullptr;
        ListNode* cur = nullptr;
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
            auto temp = new ListNode(carry % 10);
            carry /= 10;
            if (ret == nullptr) {
                ret = temp;
                cur = ret;
            }
            else {
                cur->next = temp;
                cur = cur->next;
            }
            l1 = l1 == nullptr ? nullptr : l1->next;
            l2 = l2 == nullptr ? nullptr : l2->next;
        }
        return ret;
    }
};
```
## 拓展

通过单链表的定义可以得知，单链表也是递归结构，因此，也可以使用递归的方式来进行reverse操作。
> 由于单链表是线性的，使用递归方式将导致栈的使用也是线性的，当链表长度达到一定程度时，递归会导致爆栈，因此，现实中并不推荐使用递归方式来操作链表。

### 描述

1. 将两个链表的第一个节点值相加，结果转为0-10之间的个位数，并设置进位信息
2. 将两个链表第一个节点以后的链表做带进位的递归相加
3. 将第一步得到的头节点的next指向第二步返回的链表

###  C++实现
```C++
// 普通递归
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addTwoNumbers(l1, l2, 0);
    }
    
private:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, int carry) {
        if (l1 == nullptr && l2 == nullptr && carry == 0) return nullptr;
        carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
        auto ret = new ListNode(carry % 10);
        ret->next = addTwoNumbers(l1 == nullptr ? l1 : l1->next,
                                 l2 == nullptr ? l2 : l2->next,
                                 carry / 10);
        return ret;
    }
};
// （类似）尾递归
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = nullptr;
        addTwoNumbers(head, nullptr, l1, l2, 0);
        return head;
    }
    
private:
    void addTwoNumbers(ListNode*& head, ListNode* cur, ListNode* l1, ListNode* l2, int carry) {
        if (l1 == nullptr && l2 == nullptr && carry == 0) return;
        carry += (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val);
        auto temp = new ListNode(carry % 10);
        if (cur == nullptr) {
            head = temp;
            cur = head;
        } else {
            cur->next = temp;
            cur = cur->next;
        }
        addTwoNumbers(head, cur, l1 == nullptr ? l1 : l1->next, l2 == nullptr ? l2 : l2->next, carry / 10);
    }
};
```
