"""
jfnk_hookstep: Python bindings for the JFNK-Hookstep / GMRESm Fortran solvers.

Public API:
- gmresm
- newtonhook
"""

from . import _fortran_backend

# Public functions
gmresm = _fortran_backend.gmresm
newtonhook = _fortran_backend.newtonhook

# Optional: expose the compiled extension for advanced use/debugging
NewtonHook = _fortran_backend

__all__ = [
    "gmresm",
    "newtonhook",
    "_fortran_backend",
]