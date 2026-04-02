"""Simple retry utility for flaky browser interactions."""

from __future__ import annotations

import time
from typing import Callable, TypeVar


T = TypeVar("T")


def retry(operation: Callable[[], T], attempts: int = 3, delay: float = 0.5) -> T:
    """Retry an operation for a fixed number of attempts."""
    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            return operation()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(delay)
    assert last_error is not None
    raise last_error
