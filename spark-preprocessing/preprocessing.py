import sys
from pyspark import SparkContext, SparkConf
from spectraml.utils import gen_files_with_ext
from spectraml.lamost import read_spectrum, preprocess_spectrum


# create a SparkContext object
conf = SparkConf().setAppName('preprocessing')
sc = SparkContext(conf=conf)

# TODO use click and create CLI
path = sys.argv[1]

# TODO let specify extension e.g. '.fits', '.fits.gz'
# TODO parametrize start, end, and number of wavelengths
# TODO save the proprocessed spectra to csv
# TODO let choose a filename
sc.parallelize(gen_files_with_ext(path, '.fits')) \
        .map(read_spectrum) \
        .map(lambda s: (s[0], preprocess_spectrum(s[1], s[2])[1])) \
        .map(lambda s: s[0] + ',' + ','.join(map(str, s[1]))) \
        .saveAsTextFile('data')
