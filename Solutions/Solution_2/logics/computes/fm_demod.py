import numpy as np
import pydantic

from Solutions.Solution_2.logics.compute_base import ComputeBase


class FmDemod(ComputeBase):
    class Config(ComputeBase.Config):
        fs_hz: pydantic.PositiveInt

        def create_logical_instance(self):
            return FmDemod(config=self)

    def compute(self, data: np.ndarray) -> np.ndarray:
        """

        :param data:
        :return:
        """
        phase = np.angle(data)
        phase = phase.astype(np.float64)
        unwrapped_phase = np.unwrap(phase)
        demod = np.diff(unwrapped_phase * self.config.fs_hz)
        demod_scaled = demod
        demod_no_mean = demod_scaled - np.mean(demod_scaled)
        demod_padded = np.concatenate([[0], demod_no_mean])
        return demod_padded
