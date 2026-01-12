"""checkpl - Simple inline data validation for Polars."""

from checkpl.core import hello, verify
from checkpl.errors import CheckError
from checkpl.predicates import is_uniq

__version__ = "0.0.1"
__all__ = ["hello", "verify", "CheckError", "is_uniq", "__version__"]
