import java.util.HashSet;
import java.util.Stack;

public class ValidParenthese {
    public boolean isValid(String s) {
        if(s.length() == 1)
            return false;
        Stack<String> stack = new Stack<>();

        HashSet<String> l = new HashSet<>();
        l.add("(");
        l.add("{");
        l.add("[");
        HashSet<String> r = new HashSet<>();
        r.add(")");
        r.add("]");
        r.add("}");

        for(int i =0; i < s.length(); i++){
            String c = s.substring(i,i+1);
            if(l.contains(c)){
                stack.add(c);
            }else{
                if(stack.empty()){
                    return false;
                }
                String cc = stack.peek();
                switch(c){
                    case ")":
                        if(cc.equals("(")){
                            stack.pop();
                            break;
                        }else{

                            // System.out.println("2");
                            return false;
                        }
                    case "}":
                        if("{".equals(cc)){
                            stack.pop();
                            break;
                        }else{
                            // System.out.println("3");
                            return false;
                        }
                    case "]":
                        if("[".equals(cc)){
                            stack.pop();
                            break;
                        }else{
                            // System.out.println("4");
                            return false;
                        }
                }
            }

        }
        return stack.empty();
    }
}
