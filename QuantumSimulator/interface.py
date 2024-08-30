from abc import ABCMeta, abstractmethod
from contextlib import contextmanager


class Qubit(metaclass=ABCMeta):
    # Hadamard operation, puts into superposition
    @abstractmethod
    def h(self): pass

    # QNOT, inverses it
    @abstractmethod
    def x(self): pass

    @abstractmethod
    def measure(self) -> bool: pass

    @abstractmethod
    def reset(self): pass

class QuantumDevice(metaclass=ABCMeta):
    @abstractmethod
    def allocate_qubit(self) -> Qubit:
        pass

    @abstractmethod
    def deallocate_qubit(self, qubit: Qubit):
        pass

    @contextmanager
    def using_qubit(self):
        qubit = self.allocate_qubit()
        try:
            yield qubit
        finally:
            qubit.reset()
            self.deallocate_qubit(qubit)


