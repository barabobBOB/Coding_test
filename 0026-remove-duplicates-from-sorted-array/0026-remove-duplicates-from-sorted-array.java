class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[left]) {
                continue;
            } else {
                left++;
                int temp = nums[left];
                nums[left] = nums[i];
                nums[i] = temp;
            }
        }
        return left + 1;
    }
}
