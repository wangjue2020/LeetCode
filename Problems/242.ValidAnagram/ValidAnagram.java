import java.util.HashMap;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if(s.length()!= t.length())
            return false;
        HashMap<Character, Integer> map = new HashMap<>();
        for ( int i =0;i < s.length(); i++){
            char c = s.charAt(i);
            int val = map.getOrDefault(c,0);
            map.put(c, ++val);
        }

        for(int i =0; i < t.length(); i++){
            char c =t.charAt(i);
            int val = map.getOrDefault(c, 0);
            if(val == 0)
                return false;
            map.put(c, --val);
        }
        return true;
    }

    public boolean isAnagram1(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] table = new int[26];
        for (int i = 0; i < s.length(); i++) {
            table[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            table[t.charAt(i) - 'a']--;
            if (table[t.charAt(i) - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}
