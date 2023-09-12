"""
Copyright (c) 2022 Luke Kreczko. All rights reserved.

dask-dirac: DIRAC Executor for Dask
"""


from __future__ import annotations

from ._dask import DiracCluster
from . import _version


__version__ = _version.get_versions()['version']

__all__ = ("__version__", "DiracCluster")
