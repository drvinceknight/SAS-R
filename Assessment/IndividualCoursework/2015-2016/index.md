---
layout : page
title  : '2015-2016 Individual Coursework'
---

# MAT013 Coursework

*Deadline: TBD*

## Instructions

The outputs of this coursework will be:

- A written report describing your code (SAS and R) to be handed in to Joanna Emery.
- An appendix containing a commented version of your code (SAS and R) to be handed in to Joanna Emery.
- A file containing the required SAS code. Name this file SAS-lastname-STUDENTNUMBER (eg. SAS-Knight-123456) and email it to Joanna Emery with MAT013 as the subject. Note that all operations needed to complete the coursework should be included in the SAS code.
- A file containing the required R code. Name this file R-lastname-STUDENTNUMBER (eg. R-Knight-123456) and email it to Joanna Emery with MAT013 as the subject. Note that all operations needed to complete the coursework should be included in the R code.

## Coursework

1. Using both SAS and R (in other words attempt this question using SAS and then using R):

    Write code (in SAS: a macro, in R: a function) that will reproduce a mathematical procedure covered in MAT001 or MAT002. Clearly document this procedure in your report.

    [20]

2. Consider the data set [two_thirds.csv](Data/two_thirds.csv) which contains
   two columns of numerical data. These represent 1st and 2nd guesses for the
   game: "Two Thirds of the Average".

   The rules of which are explained here:
   [vknight.org/two_thirds_of_the_average_game/two_thirds_of_average_game_fill_in_sheet.pdf](http://vknight.org/two_thirds_of_the_average_game/two_thirds_of_average_game_fill_in_sheet.pdf)

   Using SAS:

   1. Draw two histograms: one for each set of guesses.
   2. Identify the winning guess for each set of guesses.

   Attempt to do this in a generic way (so that your code would work for a
   different data set).

    [25]

3. Consider the data set [jokes.csv](Data/jokes.csv) which contains jokes that
   have been ranked for the [Edinburgh Fringe
   Festival](http://www.bbc.co.uk/news/uk-scotland-edinburgh-east-fife-34039927)
   for the years 2009-2015.

   Using R:

    1. Identify the effect of joke length on the performance of a joke.
    2. Identify if authors who have repeated entries seem to do better than
       authors who do not.

    (Note that this question is not asking for sophisticated sentiment analysis.)

    [25]

4. Using SAS or R:

    1. Write code that generates a random 'stochastic matrix' \\(P\\): a square matrix of size (\\(N\\)) with the following properties:

       $$\sum_{j=1}^{N}P_{ij}=1 \text{ for all }1\leq i\leq N$$

       and:

       $$P_{ij}\geq 0\text{ for all }1\leq i,j \leq N$$

       [15]

    2. Using the above, simulate a Stochastic process in which state \\(i\\) 'moves' to state \\(j\\) with probability given by \\(P_{ij}\\). Expected outputs include: the probability of being in each state.

       [15]

    3. Write a data set with 1000 different matrices \\(P\\) and the corresponding probability distribution.

       [10]
