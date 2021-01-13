import java.util.Stack;

public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        if(tokens.length==0)
            return 0;
        Stack<String> stack = new Stack<>();
        String operators = "+-*/";
        for(String s: tokens){
            if (operators.contains(s)){
                String se = stack.pop();
                String fi = stack.pop();
                String res = compute(s, fi, se);
                stack.push(res);
            }else{
                stack.push(s);
            }
        }
        return Integer.parseInt(stack.pop());
    }
    public String compute(String operator, String f, String s){
        int first = Integer.parseInt(f);
        int second = Integer.parseInt(s);
        int ans = 0;
        switch(operator){
            case "+":
                ans = first+second;
                break;
            case "-":
                ans = first-second;
                break;
            case "*":
                ans = first*second;
                break;
            case "/":
                ans = first/second;
                break;
        }
        return ans+"";
    }
}
