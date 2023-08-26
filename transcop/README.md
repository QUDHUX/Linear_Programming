# PROBLEM:

A transport company has two types of truck, typeA and type B. type A has a refrigerated capacity of 20m3 and a non-refrigerated capacity of 40m3. in contrast,Type B has the same overall volume with equal refrigerated and non-refrigerated stock sections.A grocer must hire trucks to transport 3000m3 of refrigerated stock and 4000m3 of non-refrigerated stock.The cost per kilometre of type A is 30 and 40 for type B. How many trucks of each type should the grocer rent to achieve the minimum total cost?

# MODEL

1.  Objective function
    min_z = 30A + 40B

2.  Constraints
    20A + 30B >= 3000
    40A + 30B >= 4000

3.  Non-negativity rule
    A,B >= 0

# OPTIMAL SOLUTION

30(50) + 40(67) = 4167

# DECISION

The grocer should rent 50 trucks of type A and 67 trucks of type B.
