import java.util.Stack;

public class MyQueue {
    Stack<Integer> queue;
    int peek;
    Stack<Integer> backup;
    /** Initialize your data structure here. */
    public MyQueue() {
        queue = new Stack<>();
        backup = new Stack<>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        queue.push(x);
        if(queue.size() == 1){
            peek = x;
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        while(queue.size()!=0){
            backup.push(queue.pop());
        }
        int ans = backup.pop();
        if(!backup.empty()){
            peek = backup.peek();
            while(backup.size()!= 0){
                queue.push(backup.pop());
            }
        }
        return ans;
    }

    /** Get the front element. */
    public int peek() {
        return peek;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return queue.empty();
    }
}