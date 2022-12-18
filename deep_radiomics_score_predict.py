import os
import numpy as np
import pandas as pd
import csv
import pickle
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
import scipy.io as sio
# from tensorflow.keras.applications.efficientnet import EfficientNetB7


def Train_info_load(model_folder):

    train_info = {}

    # Normalization parameter
    Nor_path = pd.read_csv(os.path.join(model_folder, 'normalization_train_info.csv'))
    train_info['slop'] = np.array(Nor_path['slop'])
    train_info['interception'] = np.array(Nor_path['interception'])

    # Selected features index
    Feature_path = os.path.join(model_folder, 'feature_select_info.csv')
    with open(Feature_path, 'r', newline='') as f:
        f_reader = csv.reader(f)
        for index in f_reader:
            if index[0] == 'selected_feature':
                feature_index = index[1:]
    train_info['feature_index'] = feature_index

    # Model information
    model_path = os.path.join(model_folder, 'model.pickle')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    train_info['model'] = model

    return train_info


def New_data_predict(New_data, model_folder):

    # Parameters from the training set
    train_info = Train_info_load(model_folder)

    # Loading New data
    New_data_path = os.path.join(model_folder, New_data)
    New_data = pd.read_csv(New_data_path, header=0, index_col=0)
    label = np.asarray(New_data['PL'].values)

    # Extracting selected features
    selected_array = New_data[train_info['feature_index']]
    array = np.asarray(selected_array, dtype=np.float64)

    # Normalization for new data
    array -= train_info['interception']
    array /= train_info['slop']
    array = np.nan_to_num(array)
    array_nor = array.astype(np.float64)

    # Using the model
    model = train_info['model']
    predict_score = model.predict_proba(array_nor)[:, 1]
    auc = roc_auc_score(label, predict_score)

    return predict_score, auc


if __name__ == '__main__':

    method = ['deep', 'radiomic']
    for m in range(2):
        model_folder = './' + method[m]+ 'Score/'
        New_data = 'test.csv'
        predict_score, auc = New_data_predict(New_data, model_folder)
        pd.DataFrame(predict_score).to_csv((model_folder + method[m] + '_score_predicted.csv'), header=['score'])
