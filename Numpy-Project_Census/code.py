# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print("\nData: \n\n",data)
print("\nType of data: \n\n",type(data))
census=np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
race=census[:,2]
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
#race_5=census[census[:,2]]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

race_lst=[len_0,len_1,len_2,len_3,len_4]

minority_race=race_lst.index(min(race_lst))

print(minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

#avg_pay_high=np.mean(high[7])
avg_pay_high=high[:,7].mean()
#avg_pay_low=np.mean(low[7])
avg_pay_low=low[:,7].mean()
print(avg_pay_high)
print(avg_pay_low)


