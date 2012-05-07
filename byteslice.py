#!/usr/bin/env python
# -*- coding: UTF -*-
import os.path
import sys

MB = 1024*1024
filename = sys.argv[1]


def byteslice(filename):
    filesize = os.path.getsize(filename)
    rough_slice_number = filesize / MB
    excess_size = filesize - (rough_slice_number * MB)

    if excess_size > 0:
        if excess_size > (MB * 0.75):
            print 'Slice count is {0}, most slices are {1} BYTES, final slice is {2} BYTES'.format(
                (rough_slice_number + 1),
                (MB),
                (excess_size),
            )
        else:
            distribute_excess = excess_size / rough_slice_number
            print 'Slice count is {0}, most slices are {1} BYTES, final slices is {2} BYTES'.format(
                rough_slice_number,
                (MB + distribute_excess),
                filesize - ((MB + distribute_excess)*(rough_slice_number-1)),
            )
    else:
        print 'Perfect Fit?'

