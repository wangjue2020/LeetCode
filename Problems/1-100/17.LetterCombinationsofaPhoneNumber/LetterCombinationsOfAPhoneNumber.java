import java.util.ArrayList;
import java.util.List;

public class LetterCombinationsOfAPhoneNumber {
    public List<String> letterCombinations(String digits) {
        if(digits.length()==0)
            return new ArrayList<String>();
        String[] map = new String[]{
                "",
                "abc",
                "def",
                "ghi",
                "jkl",
                "mno",
                "pqrs",
                "tuv",
                "wxyz"
        };
        List<String> ans = new ArrayList<>();
        ans.add("");
        for(int i = 0; i< digits.length() ;i++){
            String cur = map[digits.charAt(i) -'0' -1];
            int size = ans.size();
            for(int j = 0; j< size; j++){
                String tmp = ans.remove(0);
                for(int k =0; k<cur.length(); k++){
                    ans.add(tmp+cur.substring(k,k+1));
                }
            }
        }
        return ans;

    }
}
