public class BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int[] cost = new int[prices.length];
        int ans = 0;
        for(int i = 0; i< prices.length; i++){
            if(i <= 1){
                cost[i] = prices[0];
                if(i == 1)
                    ans = Math.max(ans, prices[1]-prices[0]);
                continue;
            }
            int sell = prices[i];
            int cost1 = prices[i-1];
            int cost2 = cost[i-1];
            if(sell - cost1 >= sell-cost2){
                cost[i]= prices[i-1];
                ans = Math.max(ans, sell-cost1);
            }else{
                cost[i] = cost[i-1];
                ans = Math.max(ans, sell-cost2);
            }
        }
        return ans;
    }
}
