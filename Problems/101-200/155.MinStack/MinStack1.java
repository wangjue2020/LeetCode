import java.util.Stack;

public class MinStack1 {
    Stack<Integer> stack;
    Stack<Integer> helper;
    /** initialize your data structure here. */
    public MinStack1() {
        stack = new Stack<>();
        helper = new Stack<>();
    }

    public void push(int x) {
        stack.push(x);
        if(helper.size() == 0 || x <= helper.peek())
            helper.push(x);
    }

    public void pop() {
        if(!stack.isEmpty()){
            int tmp = stack.pop();
            if(tmp == helper.peek())
                helper.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return helper.peek();
    }
}
