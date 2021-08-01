package solution;

public class RemoveDuplicatesFromSortedArrayII {

    public int removeDuplicates(int[] nums) {
        int j = -1;
        for (int i = 0; i < nums.length; i++) {
            if (j < 1 || nums[i] != nums[j - 1]) {
                nums[++j] = nums[i];
            }
        }
        return j + 1;
    }
}
