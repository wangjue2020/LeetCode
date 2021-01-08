import java.util.HashSet;
import java.util.Iterator;

public class IntersectionOfTwoArrays {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> s = new HashSet<>();
        for(int e:nums1){
            s.add(e);
        }
        HashSet<Integer> ans = new HashSet<>();
        int ind = 0;
        for(int e:nums2){
            if(s.contains(e)){
                ans.add(e);
            }
        }
        int [] f = new int[ans.size()];
        Iterator<Integer> it = ans.iterator();
        while(it.hasNext()){
            f[ind++] = it.next();
        }
        return f;
    }
}
