---
layout : default
title  : '2013-2014 Class Test'
---
#MAT013 Class Test

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

    Write a macro that will create a separate pdf file of a scatter plot for
    every data set in the compressed directory
    [scatterdata.zip]({{site.baseurl}}/Data/scatterdata.zip).  All files in the
    directory contain two columns of numerical data.  Use the name of each file
    as the name of the pdf file.

    [25]

3. Using R:

    Obtain the profits (income \\(-\\) costs) of each company that is present in
    **both** data sets [incomes.csv]({{site.baseurl}}/Data/incomes.csv) and
    [costs.csv]({{site.baseurl}}/Data/costs.csv).

    Draw a histogram of these profits and also obtain a linear relationship between income and profits.

    [25]

4. Using either SAS or R:

    1. Write code that will obtain \\(k\\) random points \\((x,y)\\) where \\(x,y\\) are uniformly sampled between 0 and 1. [15]
    2. Identify how many of these points satisfy \\(x^2+y^2\leq 1\\) (this number will be referred to as \\(N=N(k)\\)). [15]
    3. Plot \\(\frac{4N(k)}{k}\\) for \\(1\leq k\leq 5000\\) and comment on the result. [10]
