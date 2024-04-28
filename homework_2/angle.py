from dataclasses import dataclass


@dataclass
class Angle:
    value: float

    def __add__(self, other: "Angle") -> "Angle":
        return Angle((self.value + other.value) % 360)
