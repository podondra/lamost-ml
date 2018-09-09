#!/usr/bin/env bash

# generate FITS files list
LAMOST_DR2_LST='data/lamost-dr2.lst'
find /lamost -name '*.fits' > $LAMOST_DR2_LST

# run preprocessing
spectraml preprocessing \
       --start 6519 --end 6732 --wavelenghts 140 \
	data/lamost-dr2.hdf5 lamost_dr2 "$LAMOST_DR2_LST"
