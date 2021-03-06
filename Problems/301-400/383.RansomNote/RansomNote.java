public class RansomNote {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] dictionary = new int[26];
        for(int i=0; i<magazine.length(); i++){
            char c = magazine.charAt(i);
            dictionary[c-'a']++;
        }
        for(int i = 0; i< ransomNote.length(); i++){
            char c = ransomNote.charAt(i);
            if(dictionary[c-'a']==0)
                return false;
            dictionary[c-'a']--;
        }
        return true;
    }
}
