import numpy as np
import scipy.stats as st
from typing import Tuple

class DataGenerator():

    def __init__(self, N, w, x_min, x_max, std=1) -> None:
        self.N = N
        self.w = w
        self.x_min = x_min
        self.x_max = x_max
        self.std = std

    def get_data(self):
        x0 = np.ones((self.N, 1))
        x1 = np.array([np.linspace(
            self.x_min,self.x_max,self.N)]).T
        X = np.column_stack([x0,x1])
        y = X.dot(self.w)
        e = st.norm.rvs(size=self.N, scale=self.std, loc=0)
        e.shape = (self.N,1)
        y = y + e
        return x1, y