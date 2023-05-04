class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] answer = new int[2];
        answer[0] = leftBinarySearch(nums, target);
        answer[1] = rightBinarySearch(nums, target);
        return(answer);
    }

    public int leftBinarySearch(int[] nums, int target){
        int left = 0;
        int right = nums.length - 1;
        int answerLeft = -1;

        while(left<=right){
            int pivot = (left+right) / 2;
            if (nums[pivot] >= target){
                right = pivot - 1;
            }else{
                left = pivot + 1;
            }
            if (nums[pivot] == target){
                answerLeft = pivot;
            }
        }
        return answerLeft;
        
    }

    public int rightBinarySearch(int[] nums, int target){
        int left = 0;
        int right = nums.length - 1;
        int answerRight = -1;

        while(left<=right){
            int pivot = (left+right) / 2;
            if (nums[pivot] <= target){
                left = pivot + 1;
            }else{
                right = pivot - 1;
            }
            if (nums[pivot] == target){
                answerRight = pivot;
            }
        }
        return answerRight;
    }
}