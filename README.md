# Predicting Wine Quality
Midterm for Data 602, Machine Learning
By <a href="https://github.com/Jcc329">Jessica Conroy Styer</a>

## Table of Contents

<ul>
  <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/tree/main/Data%20Files">Data Files</a> - The csv file used in the technical report</li>
  <li><b>Notebooks</b> - The Jupyter notebooks used to complete this project. These links lead to the updated version of the notebook as of 10/18/2020. Older versions can also be found in the folder</li>
  <ul>
    <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/blob/main/Jupyter%20Notebooks/Project%201%20Initial%20Data%20Cleaning.ipynb">1. Data Cleaning</a></li> - The notebook showing how the initial data was processed to create the cleaned dataset.
    <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/blob/main/Jupyter%20Notebooks/Project%201%20Exploratory%20Analysis.ipynb">2. Exploratory Analysis</a> - The notebook containing exploratory analyses </li>
    <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/blob/main/Jupyter%20Notebooks/Project%201%20Technical%20Report.ipynb">3. Technical Report</a> - The technical notebook containing the report and final models used.</li>
  </ul>
  <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/blob/main/README.md">README.md</a> - An overview of the project and results</li> 
  <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/tree/main/Supplemental%20Files">Suplemental files</a> - The .py file containing functions called in the notebooks</li>
</ul>

### Overview

Using a dataset of the chemical characteristics of vinho verde wines, this project aimed to determine the general quality of the wine, as good, bad, or okay. The target category was determined based on the the quality variable of the original dataset, which used sensory data to score wines on a scale of 0 to 10, 0 being the worst and 10 being best. The size of the dataset is <b> 6,497 rows and 13 columns </b>, with 12 columns representing the chemical attributes of the wine (predictors) and 1 representing the quality (target).

During data exploration, logistic regression, decision tree, and random forest models were tested to determine which would produce the most accurate predictions. The random forest model performed the best in terms of accuracy, and since the aim is to obtain accurate predictions than to understand exactly why the wine is good or bad, I chose to use the more accurate method. Finally, I used gridsearch for parameter tuning and the feature selection module in sklearn to attempt identification of the most important features  which did not improve the model significantly and in the case of feature selection, decreased accuracy, for a final accuracy of 65%. Since the 'Just Okay Wines' made up 77% of the sample. This represents worse performance than if the model had just set all values to 'Just Okay' and ultimately, the model fails to be effective.

### Goals and Research Questions
The aim of this project is to apply classification machine learning methods to produce a predicive model. I will use a dataset containing characteristics of different wines to answer the following questions:

1. Is a given wine good, bad, or just okay? 
2. What factors/features influence the quality determination of the wine?
3. What model will produce the most accuracy in predicting wine quality?

### Motivation & Background

As I was considering what data to use for this project, I ran into the Wine quality data set and was inspired by a recent struggle I had. I am not a big wine drinker, and to me, all wine is relatively the same. HOWEVER, two weeks ago, I married my now husband, who comes from a long line of Italians, and, not too stereotype, but they take their wine very seriously. The motivation for this project comes from the very real struggle I faced when selecting the wine for my wedding (although this became less stressful as the pandemic greatly decreased the guest list. Silver linings...). It is my belief that a simple tool which takes the chemical components of a wine, and tells the user whether or not the wine would be considered high quality, would be extremely useful for those of us who have low wine knowledge but a desire to appear knowledgeable to our in-laws (an eternal struggle). 

### Data

Data were retrieved from https://archive.ics.uci.edu/ml/datasets/Wine+Quality in the form of two distinct sets, one for red and one for white. The data consisted of 6,497 rows and 13 columns in total. I added a column for the type of wine (white or red) and the predicted category (Good Wine, Okay Wine, Bad Wine) 

Direct links to the csvs are: 
- <a href='https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'>winequality-red.csv</a>
- <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv">winequality-white.csv</a>
<a href="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names">Additional Documentation</a>

### Conclusion

Based on the outcome of these analysis, this model is is not really useful for predicting wine quality. (And is likely not sufficient to impress my in-laws). However, I did gain a significant amount of experience and practice with respect to using different categorical machine learning models, and the start to finish process of performing a machine learning project. I am also far more familiar now with the sklearn library than I was before, and look forward to further exploring it's capabilities. 

### Packages and Software
Software:
Python 3.0
Anaconda 3
Jupyter Notebooks

Packages:
pandas
numpy
sklearn
matplotlib
seaborn
timeit

### Presentation link - Youtube presentation of project

https://youtu.be/pN3rmUDsQI4
