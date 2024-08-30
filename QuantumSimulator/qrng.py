from QuantumSimulator.interface import QuantumDevice
from QuantumSimulator.simulator import SingleQubitSimulator


def qrng(device : QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()

if __name__ == "__main__":
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QRNG returned {random_sample}.")

