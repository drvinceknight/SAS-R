---
layout : default
title  : '2013-2014 Individual Coursework'
---

# MAT013 Coursework

*Deadline: 2013-05-09 at 0900*

## Instructions

The outputs of this coursework will be:

- A written report describing your code (SAS and R) to be handed in to Joanna Emery.
- An appendix containing a commented version of your code (SAS and R) to be handed in to Joanna Emery.
- A file containing the required SAS code. Name this file SAS-lastname-STUDENTNUMBER (eg. Knight-123456) and email it to Joanna Emery with MAT013 as the subject. Note that all operations needed to complete the coursework should be included in the SAS code.
- A file containing the required R code. Name this file R-lastname-STUDENTNUMBER (eg. Knight-123456) and email it to Joanna Emery with MAT013 as the subject. Note that all operations needed to complete the coursework should be included in the R code.

## Coursework

1. Using both SAS and R (in other words attempt this question using SAS and then using R):

    Write code (in SAS: a macro, in R: a function) that will reproduce a mathematical procedure covered in MAT001 or MAT002. Clearly document this procedure in your report.

    [20]

2. Using SAS:

    For the data set [names.csv](./Data/names.csv):

    - Identify the number of names;
    - Obtain the mean name length;
    - Plot a histogram of the name length;
    - Obtain the number of unique name lengths.

    [25]

3. Using R:

    The data set [survey.csv](./Data/survey.csv) contains responses to a questionnaire given to students regarding their attitude towards assessment.

    The questions/statements are given below:

    - How many hours a week do you spend self studying?
    - How would you describe your academic performance? (1. Very weak, 2. Weak, 3. Average, 3. Strong, 5. Very Strong)
    - What percent of compulsory homework do you complete?
    - What percent of non-compulsory homework do you complete?
    - Completing homework led to an improvement of your final mark? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - Completing homework helps you understand material? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if it is marked?  (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if it counts towards your final mark?  (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if you are aware of the amount of time it will take?  (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if you are given a timetabled slot in which to do it? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if it is in the form of multiple choice?  (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if you are going to receive feedback? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if it is linked to employability skills?  (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do homework if it is made up of past exam questions?  (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You find non marked homework is helpful? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do non compulsory homework if it is peer assessed? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do non marked homework if it was short? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do non marked homework if it improved your performance? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do non marked homework if it is to be done before the class on the relevant subject? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You are more likely to do non marked homework if it is to be completed online? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You mainly care about the mark you receive for your homework? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)
    - You feel that the feedback you receive is adequate? (1. Strongly disagree, 2. Disagree, 3. Neutral, 4. Agree, 5. Strongly agree)

    Analyse the questionnaire.

    [25]

4. Using SAS or R:

    Consider the data sets contained in [lego.zip](./Data/lego.zip) give details as to the number of individual Lego blocks (a toy) sold by 30 different shops over a 3000 day period.

    1. Give summary statistics for the entire system (i.e. you will need to combine the data sets) and plot the distribution of Lego blocks sold by each shop.
    [5]
    2. Output an appropriate chart summarising data for the total number of blocks sold.
    [5]
    3. It is decided that the shops must stop selling the blocks individually and sell combinations of blocks that give one of three products:

    - A car (3 blue blocks, 5 red blocks, 1 yellow block)
    - A plane (4 blue blocks, 1 red block, 2 yellow blocks)
    - A house (10 blue blocks, 0 red blocks, 12 yellow blocks)

    Using the information in [expected_sales_price.csv](./Data/expected_sales_price.csv), and assuming that the same number of blocks would be sold (as given by the ``1.csv''-``30.csv'' datasets) produce a final data set that contains the following variables:

    - Shop
    - Number of cars that would have optimally been sold.
    - Number of planes that would have optimally been sold.
    - Number of houses that would have optimally been sold.
    - Expected sales revenue.

    Show the expected sales revenue in a suitable graphical format.

    [20]
