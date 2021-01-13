import java.util.Stack;

public class RemoveAllAdjacentDuplicatesInString {
    public String removeDuplicates(String S) {
        Stack<String> stack = new Stack<>();
        for(int i =0; i < S.length(); i++){
            String cur = S.substring(i, i+1);
            if(stack.empty() || !cur.equals(stack.peek())){
                stack.push(cur);
            }else{
                stack.pop();
            }
        }
        String ans="";
        while(!stack.empty()){
            ans= stack.pop()+ans;
        }
        return ans;
    }
}
