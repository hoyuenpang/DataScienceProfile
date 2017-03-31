# DataScienceProfile
Some of programs and data from data science online course quizzes I took. It is a good example to show what I know

----------------------------

These are Python codes to demonstrate my ability to code in Python, Pandas, and Matplotlib. The codes are from the Coursera courses quizzes I took.

To make sure the codes cannot be found by students taking Coursera courses. The program names and data file names are changed. 

I may add more Python codes since I will write more codes after application deadline. 

——————————

ttests_real_estate.py is for running a t-test on real estate price. First I create new data showing the decline or growth of housing prices between the recession start and the recession bottom. Then I run a t-test comparing the university town values to the non-university towns values, return whether the alternative hypothesis (that the two groups are the same) is true or not as well as the p-value of the confidence. It requires two data sets. HomesPrice.csv is the value of house in cities including university towns and non-university towns. towns.txt contains names of university and their city name. 
The return of this function can be viewed by

difference, p, better = ttests_real_estate()

True
0.00549642735369
university town

—————————————

Albuquerque_Weather.py

Albuquerque_Weather.py read in c90b2d1a390d0c37060efd9692871c1da343f617720b7a6143831c7f.csv which contains weather record of several weather stations in Albuquerque metro area. In this exercise, I use Pandas to find the maximum temperature and minimum temperature in Albuquerque for everyday between 2005 and 2014. I use Matplotlib to create line graph displaying record highs and lows for 2005-2014. I shade area between two lines. I overlaid a scatter plot that indicates days in 2015 that broke a record high or low for 2005-2014. The output is saved in ABQ_Weather_2005-2015.png. 

————————————————

UNM_Sports.py

UNM_Sports.py read LobosFootball.csv and LobosBasketsball.csv. These two csv files contains season win percentage from 1950 to 2016. I use a 10 year moving average to identify any major trends in the team’s win percentages. 10 year moving average is calculate using Excel. The plot is saved as UNM_Sports.png. The plot of 10 year moving average of win percentage from 1959 to 2016 shows that the UNM football and the UNM basketball have a negative correlation. The better basketball team win percentage is, the worst football team win percentage is. And vice versa. This supports my hypothesis. The UNM can only support one winning program in sports. 



