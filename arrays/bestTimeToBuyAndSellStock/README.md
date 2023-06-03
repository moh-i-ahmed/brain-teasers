# Best Time to Buy and Sell Stock

Leetcode link [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).

**Description:** You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### [Basic Solution](/arrays/bestTimeToBuyAndSellStock/solution.py): Continuously find the lowest price

[Leetcode submission](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/962998392/)

**Explanation:** Iterate through the list, finding the lowest price and comparing it to the current price. The largest difference gives us the maximum profit.

Time Complexity: **Θ(n)**
Space Complexity: **Θ(1)**

```python
    """
    :type prices: List[int]
    :rtype: int
    """
    maxProfit = 0

    # base case
    if(len(prices) == 0) : return maxProfit

    lowestPrice = float('inf')

    for price in prices :
        # find lowest price
        if(price < lowestPrice) : lowestPrice = price

        # find max profit
        if(price - lowestPrice > maxProfit) : maxProfit = price - lowestPrice

    return maxProfit
```
