---
layout : default
title  : '2015-2016 Class Test'
---
#MAT013 Class Test

## Instructions:

- *This is an open book test. You are encouraged to use the internet, your notes etc..., however no communication with any other student is allowed.*
- *The output of this class test will be: a file containing the SAS program with any comments included and a file containing the R code with any comments included.*

Once you have finished the test:

1. Call the file for the SAS code: `SAS-lastname-STUDENTNUMBER` (eg. SAS-Knight-123456) and call the file for the R code: `R-lastname-STUDENTNUMBER` (eg. R-Knight-123456).
2. Email both files Lauren Trundle with 'MAT013 - lastname-STUDENTNUMBER' as the subject. **ALL EMAILS MUST BE SENT BEFORE LEAVING THE COMPUTER LAB**.

## Class test:

1. Using both SAS and R (in other words attempt this question using SAS and then using R):

    Create a data set with two variables: "Week" and "Ranking". For every week of the MAT013 course (1-5 including this class test) give a ranking of your enjoyment of each week of the course (1 being the best). Write some code (in both SAS and R) to sort this data set in descending order of the enjoyment ranking.

    [10]

2. Using SAS:

    The following directory:
    [numbers.zip]({{site.baseurl}}/Assessment/ClassTest/2015-2016/data/numbers.zip)
    contains 20 files containing columnes of numbers.

        N_1.csv
        N_2.csv
        N_3.csv
        .
        N_20.csv

    Write code that creates 2 new data sets:

        even.csv
        odd.csv

    which writes all even numbers in `even.csv` and odd numbers in `odd.csv`.

    [25]

3. Using R:

    Consider the following 'random walk': a coordinate makes uniformly random
    steps 'left' (-1) or 'right' (+1).

    For example the following:

        (1, 1, 1, -1, 1, -1)

    describes a random walk of 6 steps that took a total of 4 steps right and 2
    steps left, resulting in a final position of 2.

    Write code that displays a histogram of the final position of 1000 random
    walks of 10 steps.

    [25]

4. Using either SAS or R, solve the following problem:

    The data set contains data of the form...

    This denotes a tournament of the iterated prisoners dilemma (the details are
    not relevant).

    1. How many players are in the data set?
    2. How many matches are in the data set?
    3. What is the mean score for each player?
    4. Obtain a distribution/histogram of scores for each player?
    5. Based on the median score, who is the winner of the tournament?

    [40]
