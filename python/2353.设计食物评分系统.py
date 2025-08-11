#
# @lc app=leetcode.cn id=2353 lang=python3
#
# [2353] 设计食物评分系统
#
from collections import defaultdict
from heapq import *
# @lc code=start
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.foods = {}
        for i, food in enumerate(foods):
            cuisine, rating = cuisines[i], ratings[i]
            
            heappush(self.cuisines[cuisine], [-rating, food])
            self.foods[food] = [cuisine, rating]

    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food][1] = newRating
        cuisine = self.foods[food][0]
        
        heappush(self.cuisines[cuisine], [-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        cuisine = self.cuisines[cuisine]
        while -cuisine[0][0] != self.foods[cuisine[0][1]][1]:
            heappop(cuisine)
        return cuisine[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# @lc code=end