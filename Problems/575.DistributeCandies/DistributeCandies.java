import java.util.HashSet;

public class DistributeCandies {
    /**
     * Method 2
     * @param candyType
     * @return
     */
    public int distributeCandies1(int[] candyType) {
        HashSet<Integer> hs = new HashSet<>();
        for(int i : candyType){
            hs.add(i);
        }
        return hs.size()>=candyType.length/2? candyType.length/2 : hs.size();
    }

    /**
     * Method 1
     * @param candyType
     * @return
     */
    public int distributeCandies(int[] candyType) {
        HashSet<Integer> hs = new HashSet<>();
        int boy = 0;
        int girl = 0;
        for(int i : candyType){
            if((hs.contains(i) && boy <candyType.length/2) || (girl>= candyType.length/2)){
                boy++;
            }else{
                hs.add(i);
                girl++;
            }
        }
        System.out.println(girl+":"+boy);
        return hs.size();
    }
}
