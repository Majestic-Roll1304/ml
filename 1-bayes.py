def bayes_theorem(p_f, p_f_and_a): 
    p_a_given_f = (p_f_and_a) / p_f
    return p_a_given_f
# P(F) p_f = 0.2
# P(F^A)
p_f_and_a = 0.03
# calculate P(A|F)
p_f=float(input())
p_f_and_a=float(input())
result = bayes_theorem(p_f, p_f_and_a)
# summarize
print('P(A|F) = %.3f%%' % (result * 100))
#OUTPUT:
#P(A|F) = 15.000%
