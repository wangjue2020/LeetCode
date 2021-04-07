import java.util.ArrayList;
import java.util.List;

public class ZigZagConversion {
    public String convert(String s, int numRows) {
        if (numRows == 1){
            return s;
        }
        List<StringBuilder> l = new ArrayList<>();
        for(int i =0; i < numRows; i++){
            l.add(new StringBuilder());
        }
        // System.out.println(l.size());
        int ind = 0;
        boolean flag = true;
        for ( int i = 0; i < s.length(); i++){
            // System.out.println(i+":"+ind);
            char c = s.charAt(i);
            StringBuilder sb = l.get(ind);
            sb.append(c);
            if(ind == numRows-1 || (i!=0 && ind == 0)){
                flag = !flag;
            }
            if(flag){
                ind++;
            }else{
                ind--;
            }
        }
        String ans = "";
        for (StringBuilder string: l){
            ans+=string.toString();
        }
        return ans;
    }
}
