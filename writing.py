import statistics
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
writing = df["writing score"].tolist()

mean=sum(writing)/len(writing)
sd=statistics.stdev(writing)
median=statistics.median(writing)
mode=statistics.mode(writing)
print("The mean is:", mean)
print("the standard deviation is:", sd)
print("The median is:", median)
print("the mode is:",mode)

first_sd_start,first_sd_end = mean-sd,mean+sd
list_of_data_within_1_sd=[result for result in writing if result>first_sd_start and result<first_sd_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_sd)*100.0/len(writing)))
second_sd_start,second_sd_end = mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end = mean-(3*sd),mean+(3*sd)

list_of_data_within_2_sd=[result for result in writing if result>second_sd_start and result<second_sd_end]
list_of_data_within_3_sd=[result for result in writing if result>third_sd_start and result<third_sd_end]

print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_sd)*100.0/len(writing)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_sd)*100.0/len(writing)))