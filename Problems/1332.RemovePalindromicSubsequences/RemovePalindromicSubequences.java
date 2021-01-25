public class RemovePalindromicSubequences {
    public int removePalindromeSub(String s) {
        if ("".equals(s)) {
            return 0;
        }
        if (s.equals(new StringBuilder(s).reverse().toString())) {
            return 1;
        }
        return 2;
    }
}
