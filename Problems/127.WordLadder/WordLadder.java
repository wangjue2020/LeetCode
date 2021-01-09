import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class WordLadder {
    @Test
    public void test(){
        //["hot","dot","dog","lot","log","cog"]
        List<String> wordList = new ArrayList<>();
//        ["most","mist","miss","lost","fist","fish"]
        wordList.add("hot");
        wordList.add("dot");
        wordList.add("dog");
        wordList.add("lot");
        wordList.add("log");
        wordList.add("cog");
        System.out.println(ladderLength(1, "hit", "cog", wordList));

    }
    public int ladderLength(int count, String beginWord, String endWord, List<String> wordList) {

        System.out.println("count: "+count+"; beginW: " + beginWord + "; endWord: " + endWord + ";   wordList: " + wordList);
        if(wordList.contains(beginWord))
            wordList.remove(beginWord);

        if(beginWord.equals(endWord)) {
            System.out.println("return: "+1);
//            System.out.println("==============end==============");
            return 1;
        }
        if(!wordList.contains(endWord) || wordList.size() == 0) {

            System.out.println("return: "+0);
//            System.out.println("==============end==============");
            return 0;
        }

        int ans = 1;
        int temp = Integer.MAX_VALUE;
        for( String s: wordList){
            int diff = computeDifference(beginWord, s);
            if(diff == 1){
                List<String> newWL = new ArrayList<>(wordList);
                newWL.remove(s);
                int result = ladderLength(count+1, s, endWord, newWL);
                System.out.println(temp+":"+result);
                if(result != 0){
                    if(temp == Integer.MAX_VALUE || temp == 0){
                        temp = result;
                    }else {
                        temp = Math.min(temp, result);
                    }
                }
                System.out.println("compared: "+temp);
            }
        }
        if(temp == Integer.MAX_VALUE || temp == 0 ) {

            System.out.println("return: "+0);
//            System.out.println("==============end==============");
            return 0;
        }

        System.out.println("return: "+(ans+temp));
//        System.out.println("==============end==============");
        return ans+temp;
    }
    public int computeDifference(String w1, String w2){
        int ans = 0;

        for(int i = 0; i< w1.length(); i++){
            if(w1.charAt(i) != w2.charAt(i)){
                ans++;
                if(ans >1){
                    return ans;
                }
            }
        }
        return ans;
    }
}
