
import plotly.figure_factory as ff
import pandas as pd
import statistics
df = pd.read_csv('distribution.csv')
height = df["Height(Inches)"].tolist()
fig = ff.create_distplot([height], ['gra'], show_hist = False)
fig.show()
#Mean = Median = Mode
#peak value in center = Mean, symmetric around the peak value 
mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)
sd = statistics.stdev(height)
print(mean)
print(median)
print(mode)
print(sd)

sd1 = [i for i in height if i>(mean-sd) and i<(mean+sd)]
sd2 = [i for i in height if i>(mean-2*sd) and i<(mean+2*sd)]
sd3 = [i for i in height if i>(mean-3*sd) and i<(mean+3*sd)]
print(len(sd1)*100/len(height))
print(len(sd2)*100/len(height))
print(len(sd3)*100/len(height))
#68% of all data lie within one standard deviation of the mean
#95% of all the data lie within two standard deviation of the mean
#99% of all the data lie within three standard deviation of the mean