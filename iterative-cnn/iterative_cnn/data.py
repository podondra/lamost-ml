import pandas as pd


def get_ondrejov_dataset(dataset_file):
    ondrejov_dataset = pd.read_csv(dataset_file)
    # first 12 columns are metadata
    ondrejov_flux = ondrejov_dataset.iloc[:, 12:].values
    ondrejov_labels = ondrejov_dataset['label'].values
    return ondrejov_flux, ondrejov_labels
