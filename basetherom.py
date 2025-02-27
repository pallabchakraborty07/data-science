
# - 20 percent of the population has covidt. - 80 percent of the 
# population does not have covid. Now suppose that we test a
# bunch of people for covid. The possible results of these
#  tests are shown in the next set of branches: - If a person has
# covid, there is an 85% chance their test will be positive
# and a 15% chance it will be negative. - If a person does not have
# covid, there is a 98% chance their test will be negative
# and a 2% chance it will be positive.

covid_prob = 0.2
no_covid_prob = 0.8

possitive_covid_false = 0.15  #  p(-/+)
possitive_covid_true = 0.85

negative_covid_false = 0.98
negative_covid_true =0.02

# if someone gets positive what is the probablity they have covid ?

# p(covid/test+)
# ={p(test+/covid)*p(covid)}/p(test+)


# 0.186

a = 0.15
b = 0.2
c = 0.186

print(a*b/c)