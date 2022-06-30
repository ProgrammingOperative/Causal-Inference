# Causal-Inference for Breast Cancer

## Introduction
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:

- “What will happen if I halve the price of my product?”
- “Which clients will pay their debts only if I call them?”

Judea Pearl and his research group have developed in the last decades a solid theoretical framework to deal with that, but the first steps toward merging it with mainstream machine learning are just beginning. 



## Data
- For this project we will work on the ** Breast Cancer Wisconsin (Diagnostic) ** Data Set which was originally used in the creation of models to predit whether the cancer is benign or malignant
- You can extract the data from (kaggle)[https://www.kaggle.com/uciml/breast-cancer-wisconsin-data] or from (UCI Machine Learning Repository)[https://archive-beta.ics.uci.edu/ml/datasets?name=breast]. 
In the latter you can find even more data that you may explore further. To understand more about the data, and how it is collectedyou should take a look at this paper:( Breast Cancer Diagnosis and Prognosis Via Linear Programming (researchgate.net) )[https://www.researchgate.net/publication/2302195_Breast_Cancer_Diagnosis_and_Prognosis_Via_Linear_Programming#pf1].

- Features in the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

#### Attribute Information:
- ID number
- Diagnosis (M = malignant, B = benign)
- The remaining (3-32)
- Ten real-valued features are computed for each cell nucleus:
- radius (mean of distances from center to points on the perimeter)
- texture (standard deviation of gray-scale values)
- Perimeter
- Area
- smoothness (local variation in radius lengths)
- compactness (perimeter^2 / area - 1.0)
- concavity (severity of concave portions of the contour)
- concave points (number of concave portions of the contour)
- Symmetry
- fractal dimension ("coastline approximation" - 1)

- The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius. All feature values are recorded with four significant digits.

- Missing attribute values: none
- Class distribution: 357 benign (not cancer), 212 malignant (cancer)

#### Tasks
The causal graph is a central object in the framework mentioned above, but it is often unknown, subject to personal knowledge and bias, or loosely connected to the available data. The main objective of the task is to highlight the importance of the matter in a concrete way. In this spirit, We will attempt the following tasks:
1. Perform a causal inference task using Pearl’s framework;
2. Infer the causal graph from observational data and then validate the graph;
3. Merge machine learning with causal inference;
