import java.util.Iterator;
import java.util.Stack;

class MinStack {
    Stack<Integer> stack;
    int top;
    int min = Integer.MAX_VALUE;
    /** initialize your data structure here. */
    public MinStack() {
        stack=new Stack<>();

    }

    public void push(int x) {
        stack.push(x);
        top = x;
        min = x < min?x:min;
    }

    public void pop() {
        if(top == min)
            min = Integer.MAX_VALUE;
        stack.pop();
        Iterator<Integer> it = stack.iterator();

        while(it.hasNext()){
            top = it.next();
            min = top< min?top:min;
        }
    }

    public int top() {
        return top;
    }

    public int getMin() {
        return min;
    }
}