import pulp 

A = pulp.LpVariable('A', lowBound=0)
B = pulp.LpVariable('B', lowBound=0)

min_z = pulp.LpProblem("Minimize_Z", pulp.LpMinimize)
min_z += 30*A + 40*B 

min_z += 20*A + 30*B >= 3000
min_z += 40*A + 30*B >= 4000

min_z.solve()

print(A.varValue)
print(B.varValue)
print(pulp.value(min_z.objective))



