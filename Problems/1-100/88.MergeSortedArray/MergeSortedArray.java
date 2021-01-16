public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int ind = nums1.length-1;
        int i = m-1;
        int j = n-1;
        while (i >=0 || j >=0){
            if(i>=0 && j>=0)
                nums1[ind--] = nums1[i]>= nums2[j]? nums1[i--]: nums2[j--];
            else if(i >=0)
                nums1[ind--] = nums1[i--];
            else
                nums1[ind--]=nums2[j--];
        }
    }
    @Deprecated
    public void merge1(int[] nums1, int m, int[] nums2, int n) {
        if(n==0)
            return;
        int i = 0;
        int j = 0;
        int ind = 0;
        int ind_1 = 0;
        int[] temp = new int[Math.max(m,n)];
        while(i < nums1.length){
            if(ind_1== ind){
                if(i < m){
                    if(nums1[i] <= nums2[j]){
                        i++;
                    }else{
                        temp[ind++] = nums1[i];
                        nums1[i] = nums2[j];
                        i++;
                        j++;
                    }
                }else{
                    nums1[i++] = nums2[j++];
                }
            }else{
                if(i < m){
                    if( j < n){
                        if ( temp[ind_1] <= nums2[j]){
                            temp[ind++] = nums1[i];
                            nums1[i++] = temp[ind_1];
                            ind_1++;
                        }else{
                            temp[ind++] = nums1[i];
                            nums1[i++] = nums2[j];
                            j++;
                        }
                    }else{
                        if(nums1[i] <= temp[ind_1]){
                            i++;
                        }else{
                            temp[ind++] = nums1[i];
                            nums1[i++] = temp[ind_1++];
                        }
                    }
                }else{
                    if(j < n){
                        if(temp[ind_1]<=nums2[j]){
                            nums1[i++] = temp[ind_1++];
                        }else{
                            nums1[i++] = nums2[j++];
                        }
                    }else{
                        nums1[i++] = temp[ind_1++];
                    }
                }
            }

        }
    }

    /**
     * 上一个版本修改缩写得到的
     * @param nums1
     * @param m
     * @param nums2
     * @param n
     */
    @Deprecated
    public void merge2(int[] nums1, int m, int[] nums2, int n) {
        if(n==0)
            return;
        int i = 0;
        int j = 0;
        int ind = 0;
        int ind_1 = 0;
        int[] temp = new int[Math.max(m,n)];
        while(i < nums1.length){
            if(ind_1== ind){
                if(i < m){
                    if(nums1[i] <= nums2[j]){
                        i++;
                    }else{
                        temp[ind++] = nums1[i];
                        nums1[i++] = nums2[j++];
                    }
                }else{
                    nums1[i++] = nums2[j++];
                }
            }else{
                if(i < m){
                    if( j < n){
                        temp[ind++] = nums1[i];
                        nums1[i++] = temp[ind_1] <= nums2[j] ? temp[ind_1++] :nums2[j++];
                    }else{
                        if(nums1[i] <= temp[ind_1]){
                            i++;
                        }else{
                            temp[ind++] = nums1[i];
                            nums1[i++] = temp[ind_1++];
                        }
                    }
                }else{
                    nums1[i++]= (j<n && temp[ind_1]>nums2[j] )? nums2[j++]:temp[ind_1++];
                }
            }

        }
    }
}
