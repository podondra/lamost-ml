from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import scale


def pca_2d(X):
    """Project to 2 dimensions with PCA."""
    # when using PCA standardize the features
    return PCA(n_components=2).fit_transform(scale(X))


def tsne_2d(X):
    """Project to 2 dimensions with t-SNE."""
    return TSNE(n_components=2, verbose=2).fit_transform(X)
