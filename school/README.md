# PROBLEM:

A school is preparing a trip for 400 students. The company who is providing the transportation has 10 buses of 50 seats and 8 buses of 40 seats, but only has 9 drivers available. The rental cost for a large bus is 800 and 600 for a small bus. Calculate how many buses of each type should be used for the trip for the least possible cost.

# MODEL

1.  Objective function
    min_z = 800L + 600S

2.  Constraints
    L + S <= 9
    50L + 40S >= 400

3.  Non-negativity rule
    L,S >= 0

# OPTIMAL SOLUTION

800(4) + 600(5) = 6200

# DECISON

The school should rent 4 large buses and 5 small ones to minimize cost
