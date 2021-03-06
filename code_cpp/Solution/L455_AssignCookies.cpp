/**
 * 题目：分发饼干
 * 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
 * 注意：
 * 你可以假设胃口值为正。
 * 一个小朋友最多只能拥有一块饼干。
 * 
 * 示例 1:
 * 输入: [1,2,3], [1,1]
 * 输出: 1
 * 解释: 
 * 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
 * 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
 * 所以你应该输出1。
 * 
 * 题解：
 * 1. 将饼干数组合胃口值数组从小到大排好序
 * 2. 用尽量小的饼干去匹配每个人的胃口值，
 *      若匹配成功，选择用下一个小的饼干去匹配下一个小胃口值的人
 *      若匹配失败，选择下一个小的饼干去匹配当前这个人
 *      循环进行，直到饼干都用完
 * 
 * */

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        std::sort(g.begin(),g.end());
        std::sort(s.begin(),s.end());

        int j = 0;
        int res = 0;
        for(int i=0;i<s.size();i++)
        {
            if(j<g.size() && s[i]>=g[j])
            {
                res++;
                j++;
            }
        }
        return res;
    }
};