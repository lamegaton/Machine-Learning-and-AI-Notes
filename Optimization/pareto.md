# Pareto optimality

https://web.stanford.edu/group/sisl/k12/optimization/MO-unit5-pdfs/5.8Pareto.pdf

this is a break down of parento

problem:
you are the owner of a small bussiness and want to advertise:
- each ad cost $2000 that yield 2 customers and 1 positive rating per month
- each appearance costs $500, generate 2 new customers and 5 positive ratings

The company wants at least 16 news customers, and 28 positive rating/month

minimize the cost

## design
**1. understand problem**

Set contrains: 16 new cus and 28 pos rating/month
front: are set of solution
file:///C:/Users/sonph/Downloads/Multi-Objective%20Optimization%20Using%20Genetic%20Algorithms.pdf

the most optimal front is call pareto front

For m objectives or 
properties, if y={y1(x), y2(x), y3(x), …, ym(x)} is the set of objectives for a material identifed by a material descriptor (feature) vector x=(x1, x2, … xn), then we are interested in fnding the x optimizing all objectives in y. In 
general, a unique solution satisfying all objectives does not exist, and we thus seek the set of optimal solutions on 
the Pareto front. Such solutions are based on the defnition of dominance such that x is said to Pareto dominate x′
if y x( ) ⩽ y x( )′ i i for all i=1, 2, …, m and yi
(x)<yi
(x′) for at least one i=1, 2, …, m, that is, x is as good as x′ in all 
objectives and is strictly better in at least one. An x not dominated by any other is called Pareto optimal and the 
set of all Pareto optimal solutions constitutes the Pareto front