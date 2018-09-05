import h5py
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import minmax_scale
from iterative_cnn.data import query_spectra_by_filename, sample_non_candidates
from iterative_cnn.projection import tsne_2d
from iterative_cnn.visualize import plot_2d_projection


SAMPLE_SIZE = 50000


# read data
with h5py.File('data/lamost-dr1.hdf5') as hdf5:
    candidates = pd.read_csv('data/candidates-with-metadata.csv', index_col=0)
    filenames = candidates.index.values

    # query only for candidates
    ids, flux = query_spectra_by_filename(filenames, hdf5)

    # bound flux between (-1, 1) to be focused on shape
    scaled_flux = minmax_scale(flux, feature_range=(-1, 1), axis=1)

    # merge the data with candidates to map labels
    candidates_df = pd.merge(
        candidates[['profile']],
        pd.DataFrame(data=scaled_flux, index=ids),
        left_index=True, right_index=True
    )

    # add random sample of non-candidates
    non_ids, non_flux = sample_non_candidates(filenames, hdf5, SAMPLE_SIZE)
    scaled_non_flux = minmax_scale(non_flux, feature_range=(-1, 1), axis=1)
    non_candidates_df = pd.DataFrame(data=scaled_non_flux, index=non_ids)
    non_candidates_df['profile'] = 'other'

    # merge all data
    data_df = pd.concat([candidates_df, non_candidates_df], sort=False)

# use t-SNE to project to 2d for visualization
coords = tsne_2d(data_df[list(range(139))])

# plot the projection
x = coords[:, 0]
y = coords[:, 1]
ax = plot_2d_projection('t-SNE', x, y, data_df['profile'])
# save the projection
plt.savefig('figures/candidates-tsne.pdf')
