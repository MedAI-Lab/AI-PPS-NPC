# AI-PPS-NPC
A prognostic predictive system based on clinical and deep-learning in patients with locally advanced nasopharyngeal carcinoma


# Usage
Four testing cases were provided for the analysis. 

* Clinical_information
  * --- This section provides the clinical features of the testing cases, among which age, T stage and N stage were the important factors we have identified using univariate and multivariate Cox regression analyses.  

* MRIdata
  * --- Pre-processed T1-weighted (T1WI), T2-weighted (T2WI), and contrast-enhanced T1-weighted fat-suppressed (CE-T1WI-FS)images of the testing cases are provided, with the suffix "_img.nii". In addition, the segmentation results for the tumor volume of interest are also shared, with the suffix "_mask.nii".

* RadiomicScore
  * --- The folder named "RadiomicFeatureExtraction" lists the parameters and methods of radiomic feature extraction. See https://pyradiomics.readthedocs.io/en/latest/usage.html for detailed details
  * --- The folder named "RadiomicScoreCalculate" provides the constructed optimal radiomic model (model.pickle) and the corresponding details (normalization_train_info.csv, radiomic_feature_select_info.csv). The reader can use the significant radiomic features of the testing data (test_radiomic_data.csv), combined with the "radiomicScore_demo.py", to calculate the radiomic score of each case. 


