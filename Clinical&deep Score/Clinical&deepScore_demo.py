import os
import numpy as np
import pandas as pd


# important clinical features
clinical_feature = pd.read_csv(r'.\model\Clinical_information\Clinical data.csv')
PL = np.array(clinical_feature['PL(event=1)'])
PFS = np.array(clinical_feature['PFS'])
age = np.array(clinical_feature['age'])
T = np.array(clinical_feature['T'])
N = np.array(clinical_feature['N'])


# deep score
deep_score_predicted = pd.read_csv(r'.\model\DeepScore\DeepScoreCalculate\results\score_predicted.csv')
deep_score = np.array(deep_score_predicted['deep score'])


# Clinical-deep score was implemented according to packages "survival" and "survminer" in R version 4.0.1
# The index was derived from the following formula for the COX survival analysis:
# 0.017*age + 0.090*T stage + 0.363*N stage + 4.685*deep score.
