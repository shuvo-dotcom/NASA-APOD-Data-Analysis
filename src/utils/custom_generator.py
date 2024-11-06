import numpy as np
class CustomRandomGenerator(np.random.Generator):
    def __init__(self, rng: np.random.PCG64):
        super().__init__(rng)

    def custom_integers(self, low, high, size=None):
        integers = self.integers(low, high, size=size)
        if size and size[1] > 1:
            row_sums = np.sum(integers[:, :-1], axis=1)
            last_elements = self.integers(low, high, size=size[0])
            last_elements += (row_sums + last_elements) % 2
            integers[:, -1] = last_elements
        return integers

    def custom_array(self, shape, low=10, high=100):
        array = self.custom_integers(low, high, size=shape)
        total_sum = np.sum(array)
        remainder = total_sum % 5
        if remainder != 0:
            adjustment = 5 - remainder
            array[-1, -1] += adjustment
        return array