public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;

        System.out.println('z'-'A');
        while (l<r){
            String ls = s.substring(l,l+1);
            String rs = s.substring(r,r+1);
            if(!ls.matches("^[a-zA-Z0-9]$")){
                l++;
                continue;
            }
            if(!rs.matches("^[a-zA-Z0-9]$")){
                r--;
                continue;
            }
            if(!ls.equalsIgnoreCase(rs) )
                return false;
            else{
                l++;
                r--;
            }

        }
        return true;
    }
}
