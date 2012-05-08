#!/usr/bin/env python
# -*- coding: UTF -*-
import os.path
import sys

MB = 1024*1024


def byteslice(filename):
    """
        Determine the right number of file 'slices' to split a file into.
        Each slice should be approximately 1 MEGABYTE and no slice should 
        be less than 80% of 1 MEGABYTE.
    """
    filesize = os.path.getsize(filename)
    rough_slice_number = filesize / MB
    excess_size = filesize - (rough_slice_number * MB)

    report = 'Slice count is {0}, most slices are {1} BYTES, final slice is {2} BYTES'
    if excess_size > 0:
        if excess_size > (MB * 0.85):
            print report.format(
                (rough_slice_number + 1),
                (MB),
                (excess_size),
            )
        else:
            distribute_excess = excess_size / rough_slice_number
            print report.format(
                rough_slice_number,
                (MB + distribute_excess),
                filesize - ((MB + distribute_excess)*(rough_slice_number-1)),
            )
    else:
        print 'Perfect Fit?'


def main():
    """
        main
    """
    byteslice(sys.argv[1])

if __name__ == '__main__':
    main()
