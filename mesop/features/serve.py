from typing import Callable

from mesop.runtime import runtime


def serve(
  *,
  rule: str,
) -> Callable[[Callable[[], None]], Callable[[], None]]:
  def decorator(func: Callable[[], None]) -> Callable[[], None]:
    runtime().register_handler(
      rule=rule,
      handler=func,
    )
    return func

  return decorator
