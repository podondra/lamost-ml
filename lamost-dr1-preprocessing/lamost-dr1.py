import h5py
import glob
import numpy
from astropy import wcs
from astropy.io import fits

files = glob.glob('/lamost/**/*.fits')
size = len(files)
new_wave = numpy.linspace(6519, 6732, 140)

with h5py.File('/notebooks/data/lamost-dr1.hdf5') as hdf5:
    try:
        X = hdf5.create_dataset('X', (size, 140), dtype=numpy.float64)
        # create variable-len unicode datatype
        str_dtype = h5py.special_dtype(vlen=str)
        ids = hdf5.create_dataset('ids', (size, ), dtype=str_dtype)
    except RuntimeError:
        X = hdf5['X']
        ids = hdf5['ids']

    for idx, file in enumerate(files):
        print(idx, file)
        try:
            with fits.open(file) as hdulist:
                header = hdulist[0].header
                ids[idx] = header['FILENAME']
                flux = hdulist[0].data[0]
                pixcr = numpy.arange(header['NAXIS1']).reshape(-1, 1)[:, [0, 0]]
                wave = 10 ** wcs.WCS(header).wcs_pix2world(pixcr, 0)[:, 0]
                X[idx, :] = numpy.interp(new_wave, wave, flux)
        except Exception as e:
            print(e)
