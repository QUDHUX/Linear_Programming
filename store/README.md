# PROBLEM:

A store wants to liquidate 200 shirts and 100 pairs of pants from last season. They have decided to put together two offers offers, A and B. Offer A is a package of one shirt and a couple of pants which will sell for 30. Offer B is a package of three shirts and a pair of pants which will sell for 50. The store does not want to sell less than 20 packages of offer A and less than 10 packages of offer B. How many boxes do they have to deal with to maximize the money generated from the promotion?

# MODEL

1.  Objective function
    max_z = 30A + 50B

2.  Constraints
    A + 3B <= 200
    A + B <= 100
    A >= 20
    B >= 10

3.  Non-negativity rule
    A,B >= 0

# OPTIMAL SOLUTION

30(50) + 50(50) = 4000

# DECISON

The store should sell 50 packages of each offer.
