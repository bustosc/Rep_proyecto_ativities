from typing import Any
from typing_extensions import Self

from sympy.polys.domains.ring import Ring

class Field(Ring):
    is_Field = ...
    is_PID = ...
    def get_ring(self): ...
    def get_field(self) -> Self: ...
    def exquo(self, a, b): ...
    def quo(self, a, b): ...
    def rem(self, a, b): ...
    def div(self, a, b) -> tuple[Any, Any]: ...
    def gcd(self, a, b): ...
    def lcm(self, a, b): ...
    def revert(self, a): ...
    def is_unit(self, a) -> bool: ...
