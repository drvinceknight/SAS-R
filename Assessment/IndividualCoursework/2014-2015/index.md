---
layout : page
title  : '2014-2015 Individual Coursework'
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

2. A perfect number is a natural number that is equal to the sum of its divisors (excluding itself). For example \\(1,2,4,7\\) and \\(14\\) divide \\(28\\) and \\(28=1+2+4+7+14\\).

    Write code in SAS that allows one to write to a csv file a data set with all natural numbers less than a given parameter \\(N\\) as well as a boolean variable indicating if the number is perfect or not.
    For example, for \\(N=6\\) the csv file would contain the following:

        1, False
        2, False
        3, False
        4, False
        5, False
        6, True

    [25]

3. Using R:

    Consider the data files [Admissions.csv](./Data/Admissions.csv) and [Discharges.csv](./Data/Discharges.csv) which contain admission and discharge data for two categories of patients.

    - Obtain distributions of the overall inter arrival rates (reciprocal of the time between arrivals).
    - Obtain distributions of the overall service rate (reciprocal of the length of stay).
    - Visualise and discuss the differences of arrival and service rates between patient categories.

    [25]

4. Using SAS or R:

    Consider the data set [personality_performance.csv](Data/personality_performance.csv) which contains data for student personality and performance in two separate subjects.

    The personality traits are measured according to the following 6 dimensions:

    - Openness-A
    - Openness-B
    - Conscientiousness
    - Extraversion
    - Agreeableness
    - Neuroticism


    Answer the following questions:


    1. Obtain summary statistics for each personality trait. [5]
    2. Obtain a suitable visualisation for the personality traits. [5]
    3. Identify a measure that indicates performance in subject 1 relative to subject 2 ('How much better/worse students did in subject 1 relative to subject 2'). [5]
    4. Explore and attempt to indicate parameters that influence:
        - Performance in subject 1
        - Performance in subject 2
        - Relative performance

    [10]
