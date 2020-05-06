#This is like an intro to numpy
import numpy as np 

integers=np.arange(a,b)
print integers

ran_nos=np.random.randint(low=a,high=b,size=c)
print ran_nos

#To create random floating nos between 0 and 1
ran_float=np.random.random([a])

random_floats_between_2_and_3 = ran_float + 2.0
print(random_floats_between_2_and_3)


random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)