# -*- coding: utf-8 -*-

"""Top-level package for mrcpy."""

__author__ = """Sebastian Haase"""
__maintainer__ = "Talley Lambert"
__email__ = "talley@hms.harvard.edu"
__license__ = "BSD license - see LICENSE file"
__version__ = "0.1.2"

from mrc import (
    bindFile,
    Mrc,
    open,
    load,
    save,
    Mrc2,
    shapeFromHdr,
    makeHdrArray,
    hdrInfo,
    initHdrArrayFrom,
)

__all__ = [
    "bindFile",
    "Mrc",
    "open",
    "load",
    "save",
    "Mrc2",
    "shapeFromHdr",
    "makeHdrArray",
    "hdrInfo",
    "initHdrArrayFrom",
]
