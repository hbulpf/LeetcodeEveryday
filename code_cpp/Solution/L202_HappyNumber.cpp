/**
 * 题目：202. 快乐数
 * 编写一个算法来判断一个数 n 是不是快乐数。
 * 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
 * 如果 n 是快乐数就返回 True ；不是，则返回 False 。
 * 示例：
 * 输入：19
 * 输出：true
 * 解释：
 * 12 + 92 = 82
 * 82 + 22 = 68
 * 62 + 82 = 100
 * 12 + 02 + 02 = 1
 * 
 * 解法：
 * 结论：对于int整型中，所有数的各个位置的循环平方和存在两种情况：1.最终得到1；2.进入循环
 * 简单的证明：int类型最大值为为‭‭2 147 483 647‬‬， 所以平方和最大的数是1 999 999 999，平方和
 * 为1 + 81*9 = 724。任何数的平方和都在1到724之间，那么对于任意一个数进行725次循环，肯定存在重复平方和的情况，重复的情况有2：
 * 1. 重复的值为1，那么后续的循环平方和认为1，是快乐数
 * 2. 重复的值不为1，那么会进入循环：x,x1,x2.....,x;其中x为重复的值
 *   
 * 1. 快慢指针判断是否有循环存在，若是，且重复的值为1,则是快乐数，否则不是
 * 2. 利用set记录每次平方和，计算下一次的值是判断结果是否在set中，值为1则是快乐数；不为1但在set中则不为快乐数，
 **/ 

class Solution {
public:
    bool isHappy(int n) {
        int fast = n,slow = n;
        do{
            slow = bitSquareSum(slow);
            fast = bitSquareSum(fast);
            fast = bitSquareSum(fast);
        }while(slow != fast);
        return slow == 1;
    }

    int bitSquareSum(int n){
        int sum = 0;
        while(n > 0){
            int tmp = n % 10;
            sum += tmp * tmp;
            n /= 10;
        }
        return sum;
    }
};