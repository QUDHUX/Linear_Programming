import pulp 

A = pulp.LpVariable('A', lowBound=0)
B = pulp.LpVariable('B', lowBound=0)

max_z = pulp.LpProblem("Maximize_Z", pulp.LpMaximize)
max_z += 30*A + 50*B 

max_z += A + 3*B <= 200
max_z += A + B <= 100
max_z += A >= 20
max_z += B >= 10

max_z.solve()

print(A.varValue)
print(B.varValue)
print(pulp.value(max_z.objective))



