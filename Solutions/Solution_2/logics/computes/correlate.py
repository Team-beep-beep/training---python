import numpy as np

from Solutions.Solution_2.logics.compute_base import ComputeBase


class Correlate(ComputeBase):
    class Config(ComputeBase.Config):
        easter_egg_path: str

        def create_logical_instance(self):
            return Correlate(config=self)

    def initialize(self):
        easter_egg = np.fromfile(self.config.easter_egg_path, dtype=np.float32)
        self.easter_egg_no_mean = easter_egg - np.mean(easter_egg)
        self.easter_egg_norm = np.sqrt(np.sum(self.easter_egg_no_mean ** 2))
        self.window = np.ones(self.easter_egg_no_mean.shape[-1], dtype=self.easter_egg_no_mean.dtype)
        self.zero_pad = np.zeros((self.easter_egg_no_mean.shape[-1] - 1, ))

    def compute(self, data: np.ndarray) -> np.ndarray:
        """

        :param data:
        :return:
        """
        data_no_mean = data - np.mean(data)

        corr = np.correlate(data_no_mean, self.easter_egg_no_mean, mode='valid')
        corr = np.concatenate([corr, self.zero_pad])
        localized_data_norm = np.sqrt(np.convolve(data_no_mean ** 2, self.window, mode='valid'))
        localized_data_norm = np.concatenate([localized_data_norm, self.zero_pad+1])
        corr = corr / localized_data_norm / self.easter_egg_norm
        return corr
