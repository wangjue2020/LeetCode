import java.util.HashSet;

public class HappyNumber {
    public boolean isHappy(int n) {
        if(n ==1)
            return true;
        HashSet<Integer> s = new HashSet<>();
        while(!s.contains(n)){
            s.add(n);
            String str = String.valueOf(n);
            n = 0;
            for ( int i = 0; i< str.length(); i++){
                int temp = str.charAt(i)-'0';
                n += temp*temp;
            }
            if(n==1)
                return true;
        }
        return false;
    }
}
