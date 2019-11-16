

# various codes to try and work out my thought processes behind creating distributions and running analyses
# methods used from Think Stats code book to try and replicate plots with my Salary data set and/or
# use additional variables from Baseball Reference for explanation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
import seaborn as sns
import math

import scipy as sp
from matplotlib.ticker import FuncFormatter

salaries = pd.read_csv('Salaries(2).csv')

def PercentileRank(scores, your_score):
count = 0
for score in scores:
if score <= your_score:
count += 1


plt.hist((salaries_2015['salary']/1e6), bins=6, color='g', edgecolor='blue', linewidth=1.7, align='mid');
plt.xlabel('Salary (millions of $)'), plt.ylabel('Count')
plt.title('MLB 2015 Salaries', size = 16);



#hypothesis testing

class HypothesisTest(object):

    def __init__(self, data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)

    def PValue(self, iters=1000):
        self.test_stats = [self.TestStatistic(self.RunModel())
                           for _ in range(iters)]

        count = sum(1 for x in self.test_stats if x >= self.actual)
        return count / iters

    def TestStatistic(self, data):
        raise UnimplementedMethodException()

    def MakeModel(self):
        pass

    def RunModel(self):
        raise UnimplementedMethodException()

    df = analytic.Salaries()
    diffs = df.war.diff()
    cdf = salary.Cdf(war, label='WIns Above Replacement')

    salary.Cdf(cdf)
    salary.Config(xlabel='WAR contribution', ylabel='CDF (dollars)')

    import # possible api here??#  as smf

    formula = 'salary ~ WAR'
    model = smf.ols(formula, data=live)
    results = model.fit()
    results.summary()