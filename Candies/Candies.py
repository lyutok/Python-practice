"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

ratings = [1,3,2,2,1]
# Each child must have at least one candy.
candy = [1] * len(ratings)
print(candy)

for i in range(1, len(ratings)):
    if ratings[i] > ratings[i - 1]:
        candy[i] = candy[i - 1] + 1

print(candy)

for i in range(len(ratings) - 2, -1, -1):
    if ratings[i] > ratings[i + 1]:
        candy[i] = max(candy[i], candy[i + 1] + 1)

print(candy)
# Calculate the total number of candies needed
total_candies = sum(candy)
print(total_candies)  


