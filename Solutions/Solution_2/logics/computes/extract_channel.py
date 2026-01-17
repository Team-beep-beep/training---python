import numpy as np
import pydantic
from scipy.signal import resample_poly

from Solutions.Solution_2.logics.compute_base import ComputeBase


class ExtractChannel(ComputeBase):
    class Config(ComputeBase.Config):
        fs_hz: pydantic.PositiveInt
        freq_shift_hz: int
        down_sample_factor: pydantic.PositiveInt
        up_sample_factor: pydantic.PositiveInt = 1

        def create_logical_instance(self):
            return ExtractChannel(config=self)

    def compute(self, data: np.ndarray) -> np.ndarray:
        """

        :param data:
        :return:
        """
        t = np.arange(data.shape[-1]) / self.config.fs_hz
        freq_shift_exp = np.exp(1j * 2 * np.pi * self.config.freq_shift_hz * t)
        data_shifted = data * freq_shift_exp
        channel = resample_poly(data_shifted,
                                up=self.config.up_sample_factor,
                                down=self.config.down_sample_factor)
        return channel
