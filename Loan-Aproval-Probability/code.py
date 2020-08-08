# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

# probability of  fico score greater than 700

p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)


# probability of purpose == debt_consolidation
p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

# Create new dataframe for condition ['purpose']== 'debt_consolidation' 
df1 = df[df['purpose']== 'debt_consolidation']

# Calculate the P(A|B)
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)


# --------------
# probability of paid_back_loan is Yes

#probability of loan to be paid back
prob_lp=df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
print(prob_lp)

#probability of credit policy
prob_cs=df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print(prob_cs)

new_df=df[df['paid.back.loan']=='Yes']

prob_pd_cs=new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]

bayes=prob_pd_cs*prob_lp/prob_cs
print('Bayes Score is=',bayes)


# --------------
# code starts here
#bar plot for purpose
df['purpose'].value_counts().plot(kind='bar')
#plt.show()

df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar')
plt.show()
# code ends here


# --------------
# code starts here

#median for installment
inst_median=df['installment'].median()
print('inst median=',inst_median)
#mean for installment a
inst_mean=df['installment'].mean()
print('inst mean=',inst_mean)

df['installment'].hist(bins=50)
df['log.annual.inc'].hist(bins=50)
plt.show()
# code ends here


