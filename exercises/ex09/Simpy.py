"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """Simpy class list of floats."""
    values: list[float]

    def __init__(self, values: list[float] = []):
        """Init function."""
        self.values = values

    def __str__(self) -> str:
        """Str lit print of class."""
        return f'Simpy({self.values})'

    def fill(self, value: float, times: int) -> None:
        """Fills the values attribute with a list of float x times long."""
        self.values = []
        for i in range(times):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates an ascending or descending list of flaots."""
        # Check validity of step in relation to the start and stop called.
        assert step != 0.0

        direction: float = stop - start

        if direction > 0.0:
            assert step > 0.0

        elif direction < 0.0:
            assert step < 0.0
        
        self.values = []
        
        while (start < stop) if (direction > 0) else (start > stop):
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Adds up the contents of Simpy object."""
        sum: float = 0

        for num in self.values:
            sum += num
        
        return sum

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Defines addition for Simpy object."""
        result: list[float] = []

        # If rhs is Simpy obj
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)

            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        
        # If rhs is float
        else:
            for num in self.values:
                result.append(num + rhs)
        
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Defines exponentiation for Simpy obj."""
        result: list[float] = []

        # If rhs is Simpy
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)

            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        
        # If rhs is float
        else:
            for num in self.values:
                result.append(num ** rhs)

        return Simpy(result)
    
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Equality overload for Simpy."""
        result: list[bool] = []

        # If rhs is Simpy
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        
        # If rhs is float
        else:
            for num in self.values:
                if num == rhs:
                    result.append(True)
                else:
                    result.append(False)

        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Greater than overload for Simpy."""
        result: list[bool] = []

        # If rhs is Simpy
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        
        # If rhs is float
        else:
            for num in self.values:
                if num > rhs:
                    result.append(True)
                else:
                    result.append(False)

        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription notation for Simpy."""
        # If rhs is int
        if isinstance(rhs, int):
            return self.values[rhs]
        
        # If rhs is list[bool]
        else:
            assert len(self.values) == len(rhs)
            result: list[float] = []

            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
        
        return Simpy(result)