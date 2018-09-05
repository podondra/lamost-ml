import os
import numpy as np
import pandas as pd


def get_ondrejov_dataset(dataset_file):
    ondrejov_dataset = pd.read_csv(dataset_file)
    # first 12 columns are metadata
    ondrejov_flux = ondrejov_dataset.iloc[:, 12:].values
    ondrejov_labels = ondrejov_dataset['label'].values
    return ondrejov_flux, ondrejov_labels


def extract_filename(path):
    """Remove directories from path and return only filename."""
    return os.path.basename(path)


vec_extract_filename = np.vectorize(extract_filename)


def query_spectra_by_filename(filenames, hdf5):
    """Return identifiers and fluxes of spectra with filenames in query."""
    ids = vec_extract_filename(hdf5['id_lam'])
    mask = np.isin(ids, filenames)
    flux = hdf5['X_lam']
    return ids[mask], flux[mask, :]


def sample_non_candidates(candidates_filenames, hdf5, size, random_state=0):
    # remove path from filenames
    ids = vec_extract_filename(hdf5['id_lam'])
    # get non-candidates spectra
    mask = ~np.isin(ids, candidates_filenames)
    non_ids, non_flux = hdf5['id_lam'][mask], hdf5['X_lam'][mask, :]
    # get random sample
    np.random.seed(random_state)
    index = np.random.choice(non_ids.shape[0], size=size, replace=False)
    return non_ids[index], non_flux[index, :]
