import os
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
import astropy.io.fits
import astropy.wcs
from astropy.utils.exceptions import AstropyWarning
import click


def get_mag_r(header):
    """Return r magnitude from FITS header or None."""
    # get magtype to locate r magnitude
    magtype = header['MAGTYPE']
    try:
        # get value of the r magnitude
        return header['MAG' + str(magtype.index('r') + 1)]
    except ValueError:
        # on exception return None
        return None


def extract_spectrum_metadata(path_and_label):
    """Extract metadata of a spectrum.

    path_and_label is tuple of path to a FITS file and a label (e.g. emission,
        double-peak and so on)

    Currectly extract filename, designation, right ascension, declination,
    subclass and profile (which is the label from path_and_label tuple).
    This function is implement to work with pandas.DataFrame.apply function.
    """
    path, profile = path_and_label
    with astropy.io.fits.open(path) as hdulist:
        header = hdulist[0].header
        # extract metadata
        filename = header['FILENAME']
        desig = header['DESIG']
        ra = header['RA']
        dec = header['DEC']
        subclass = header['SUBCLASS']
        mag_r = get_mag_r(header)
    # return the metadata with correct index
    return pd.Series(
        [filename, desig, ra, dec, subclass, mag_r, profile],
        index=['filename', 'designation', 'ra', 'dec', 'subclass', 'mag_r',
            'profile']
    )


def plot_spectrum(path, label=None, directory=''):
    """Plot spectrum from LAMOST DR1 in a specific format."""
    with astropy.io.fits.open(path) as hdulist:
        header = hdulist[0].header
        pixcr = np.arange(header['NAXIS1']).reshape(-1, 1)[:, [0, 0]]
        wave = 10 ** astropy.wcs.WCS(header).wcs_pix2world(pixcr, 0)[:, 0]
        flux = hdulist[0].data[0]
        subcontinuum = hdulist[0].data[2]
        desig = header['DESIG']
        mag_r = get_mag_r(header)
        filename = header['FILENAME']
        subclass = header['SUBCLASS']

    # plot raw data
    figsize = (12, 6)
    fig, axs = plt.subplots(nrows=2, figsize=figsize)
    safe_filename = filename.replace('_', '\_')
    title = '{{\\tt {}}} ({}, Rmag: {}, label: {}, subclass: {})'.format(
        safe_filename, desig, mag_r, label, subclass.replace('_', '\_')
    )
    axs[0].set_title(title)
    for ax in axs:
        ax.set_xlabel('vacuum wavelength (\AA)')
        ax.set_ylabel('flux (counts)')
        ax.axvline(6564.614, c='black', ls='dashed', lw=1)
        ax.grid()

    axs[0].plot(wave, flux)
    h_index = (wave > 6519) & (wave < 6732)
    h_wave = wave[h_index]
    h_flux = flux[h_index]
    axs[1].plot(h_wave, h_flux)

    fig.tight_layout()
    plt.savefig('{}.pdf'.format(
        os.path.join(directory, os.path.splitext(filename)[0]))
        )
    plt.close()

    # plot normalized data
    fig, axs = plt.subplots(nrows=2, figsize=figsize)
    axs[0].set_title(title)
    for ax in axs:
        ax.set_xlabel('vacuum wavelength (\AA)')
        ax.set_ylabel('relative flux')
        ax.axvline(6564.614, c='black', ls='dashed', lw=1)
        ax.grid()

    axs[0].plot(wave, subcontinuum)
    h_subcontinuum = subcontinuum[h_index]
    axs[1].plot(h_wave, h_subcontinuum)

    fig.tight_layout()
    plt.savefig('{}-normalized.pdf'.format(
        os.path.join(directory, os.path.splitext(filename)[0]))
        )
    plt.close()


@click.group()
def cli():
    """A simple command line tool for working with LAMOST spectra."""
    pass


@cli.command('metadata', short_help='generate CSV with spectra metadata')
@click.argument('infile', type=click.File('r'))
@click.argument('outfile', type=click.File('w'))
def metadata(infile, outfile):
    """Extract metadata from spectra in INFILE into OUTFILE.
    INFILE must be a CSV file consisting of a path to a FITS file and a label.
    """
    # read infile into pandas DataFrame
    candidates = pd.read_csv(infile)
    # extract the metadata
    metadata = candidates.apply(
            extract_spectrum_metadata,
            axis=1, result_type='expand'
            )
    # write the metadata to outfile
    metadata.to_csv(outfile, index=False)


@cli.command('preview', short_help='render spectrum into PDF')
@click.argument('infile', type=click.File('rb'))
def preview(infile):
    """Render PDF images of a spectrum from FITS file provides as INFILE."""
    plot_spectrum(infile)


@cli.command('render', short_help='render all spectra into PDFs')
@click.argument('infile', type=click.File('r'))
@click.argument('outdir', type=click.Path(exists=True))
def render(infile, outdir):
    """Render all spectra from INFILE into OUTDIR directory.
    INFILE must be a CSV file consisting of a path to a FITS file and a label.
    """
    # ignore astropy warnings
    warnings.simplefilter('ignore', category=AstropyWarning)
    # read infile into pandas DataFrame
    candidates = pd.read_csv(infile)
    with click.progressbar(length=len(candidates)) as bar:
        for candidate in candidates.itertuples():
            plot_spectrum(candidate.path, candidate.label, outdir)
            bar.update(1)


if __name__ == '__main__':
    cli()
