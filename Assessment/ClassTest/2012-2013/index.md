---
layout : default
title  : '2012-2013 Class Test'
---
# MAT013 Class Test

## Instructions:

- *This is an open book test. You are encouraged to use the internet, your notes etc..., however no communication with any other student is allowed.*
- *The output of this class test will be: a file containing the SAS program with any comments included and a file containing the R code with any comments included.*

Once you have finished the test:

1. Call the file for the SAS code: `SAS-lastname-STUDENTNUMBER` (eg. SAS-Knight-123456) and call the file for the R code: `R-lastname-STUDENTNUMBER` (eg. R-Knight-123456).
2. Email both files to Joanna Emery (EmeryJL4@cf.ac.uk) with 'MAT013 - lastname-STUDENTNUMBER' as the subject. **ALL EMAILS MUST BE SENT BEFORE LEAVING THE COMPUTER LAB**.

## Class test:

1. Using both SAS and R (in other words attempt this question using SAS and then using R):

    Create a data set with two variables: "Week" and "Ranking". For every week of the MAT013 course (1-5 including this class test) give a ranking of your enjoyment of each week of the course (1 being the best). Write some code (in both SAS and R) to sort this data set in descending order of the enjoyment ranking.

    [10]

2. Using SAS:

    Solve the following optimisation problem:

    Maximize

    $$x+3y-z+max(x,y)+2z$$

    Subject to:

    $$x-3y\leq 20$$
    $$x-7y\geq 5$$
    $$y+z\leq 25$$
    $$y\geq 0$$
    $$z\geq \max(x,y)$$


    [25]

3. Using R:

    Create a function that will give all numbers less than \\(k\\) (an input),
    not divisible by \\(3,7\\) or \\(13\\). Furthermore let your function take as input the name of a file and write those numbers to a csv file with that name.

    Demonstrate this with \\(k=2341\\) and the file name "classtest".

    [25]

4. Using either SAS or R:

    The files [Game_1.csv](./Data/Game_1.csv), [Game_2.csv](./Data/Game_2.csv), [Game_3.csv](./Data/Game_3.csv), [Game_4.csv](./Data/Game_4.csv), [Game_5.csv](./Data/Game_5.csv), [Game_6.csv](./Data/Game_6.csv) contain data for guesses of the game "2/3rds of the average":

    > "All individuals must guess a number between 0 and 100 (inclusive). The winner of the game is the guess that is closest to two thirds of the average of all guesses."

    i. Obtain histograms showing the distribution of guesses in each individual game and over all games (i.e. produce 7 plots). [10]
    ii. Identify the winning guess in each individual game and over all games. [20]
    iii. Every game is played with a different number of players, obtain a scatter plot of the winning guesses against the number of players (include the overall). [7]
    iv. Comment on the relationship (if any) between the number of players and the winning guess. [3]
