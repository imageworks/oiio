#!/usr/bin/env python

# Allow some LSB slop -- necessary because of the alpha disassociation
# combined with implied sRGB conversion.
failthresh = 0.02
failpercent = 0.02
redirect = ' >> out.txt 2>&1 '
failureok = True

imagedir = OIIO_TESTSUITE_IMAGEDIR + "/jpeg2000/broken"
files = [ "issue_3427.jp2" ]
for f in files:
    command += rw_command (imagedir, f, printinfo=False)

