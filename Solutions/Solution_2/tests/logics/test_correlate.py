import numpy as np
import pydantic
import pytest
import hydra
from omegaconf import OmegaConf

from Solutions.Solution_2.logics.computes.correlate import Correlate


class TestConfig(pydantic.BaseModel):
    correlate_config: Correlate.Config
    input_signal_path: str
    correct_index: pydantic.PositiveInt
    tol: pydantic.PositiveFloat = 1e-3


@pytest.fixture(scope="session")
def test_config(request) -> TestConfig:
    scenario_name = request.param
    with hydra.initialize(version_base=None, config_path="configs"):
        cfg = hydra.compose(config_name=scenario_name)
    test_cfg_dict = OmegaConf.to_container(cfg.test_config, resolve=True)
    test_cfg = TestConfig.parse_obj(test_cfg_dict)
    return test_cfg


class TestClass:
    @pytest.mark.parametrize("test_config", ["test_correlate_config"], indirect=True)
    def test_correlate(self, test_config: TestConfig):
        input_signal = np.fromfile(test_config.input_signal_path, dtype=np.float32)

        correlate = test_config.correlate_config.create_logical_instance()
        calc_output = correlate.compute(input_signal)
        index = np.argmax(calc_output)
        assert index == test_config.correct_index
