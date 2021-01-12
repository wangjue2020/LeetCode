import java.util.ArrayDeque;
import java.util.Queue;

public class MyStack {
    Queue<Integer> stack;
    Queue<Integer> backup;
    int top;
    /** Initialize your data structure here. */
    public MyStack() {
        stack = new ArrayDeque<>();
        backup = new ArrayDeque<>();

    }

    /** Push element x onto stack. */
    public void push(int x) {
        stack.add(x);
        top = x;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        // System.out.println(stack);
        while(stack.size()>1){
            backup.add(stack.remove());
        }
        int ans = stack.remove();
        // System.out.println(backup);
        if(!backup.isEmpty()){
            while (backup.size()>1){
                push(backup.remove());
            }
            push(backup.remove());
            // System.out.println(backup);
        }

        // System.out.println(stack);
        return ans;
    }

    /** Get the top element. */
    public int top() {
        return top;
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return stack.isEmpty();
    }
}