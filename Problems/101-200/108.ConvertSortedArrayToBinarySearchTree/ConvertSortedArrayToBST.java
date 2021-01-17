public class ConvertSortedArrayToBST {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST(nums, 0, nums.length-1);

    }
    public TreeNode sortedArrayToBST(int[] nums, int s, int e){
        int size = e - s+1;
        int mid = (s+e) /2 ;
        if(size == 1 )
            return new TreeNode(nums[s]);
        if(size == 0){
            return null;
        }
        TreeNode node = new TreeNode(nums[mid]);
        node.left = sortedArrayToBST(nums, s , mid-1);
        node.right = sortedArrayToBST(nums, mid+1, e);
        return node;
    }
}
