
import os
from radiomics import featureextractor

extractor = featureextractor.RadiomicsFeatureExtractor('./Params.yaml')

mask_path = './T1_mask.nii'
data_path = './T1_img.nii'
radiomic_feature = extractor.execute(data_path, mask_path)

