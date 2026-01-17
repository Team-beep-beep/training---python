import numpy as np
import pydantic
import pytest
import hydra
from omegaconf import OmegaConf

from Solutions.Solution_2.logics.computes.extract_channel import ExtractChannel
from Solutions.Solution_2.logics.computes.fm_demod import FmDemod
from Solutions.Solution_2.logics.computes.correlate import Correlate


class TestConfig(pydantic.BaseModel):
    extract_channel_config: ExtractChannel.Config
    fm_demod_config: FmDemod.Config
    correlate_config: Correlate.Config
    input_signal_path: str
    correct_index: pydantic.PositiveInt


@pytest.fixture(scope="session")
def test_config(request) -> TestConfig:
    scenario_name = request.param
    with hydra.initialize(version_base=None, config_path="configs"):
        cfg = hydra.compose(config_name=scenario_name)
    test_cfg_dict = OmegaConf.to_container(cfg.test_config, resolve=True)
    test_cfg = TestConfig.parse_obj(test_cfg_dict)
    return test_cfg


class TestClass:
    @pytest.mark.parametrize("test_config", ["test_system_config.yaml"], indirect=True)
    def test_system(self, test_config: TestConfig):
        input_signal = np.fromfile(test_config.input_signal_path, dtype=np.complex64)

        extract_channel = test_config.extract_channel_config.create_logical_instance()
        fm_demod = test_config.fm_demod_config.create_logical_instance()
        correlate = test_config.correlate_config.create_logical_instance()

        channel = extract_channel.compute(input_signal)
        demodulated = fm_demod.compute(channel)
        corr = correlate.compute(demodulated)
        index = np.argmax(corr)

        assert index == test_config.correct_index
