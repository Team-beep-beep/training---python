import numpy as np
import pydantic
import pytest
import hydra
from omegaconf import OmegaConf

from Solutions.Solution_2.logics.computes.fm_demod import FmDemod


class TestConfig(pydantic.BaseModel):
    module_config: FmDemod.Config
    input_signal_path: str
    test_signal_path: str
    tol: pydantic.PositiveFloat = 1e-2


@pytest.fixture(scope="session")
def test_config(request) -> TestConfig:
    scenario_name = request.param
    with hydra.initialize(version_base=None, config_path="configs"):
        cfg = hydra.compose(config_name=scenario_name)
    test_cfg_dict = OmegaConf.to_container(cfg.test_config, resolve=True)
    test_cfg = TestConfig.parse_obj(test_cfg_dict)
    return test_cfg


class TestClass:
    @pytest.mark.parametrize("test_config", ["test_fm_demod_config"], indirect=True)
    def test_fm_demod(self, test_config: TestConfig):
        input_signal = np.fromfile(test_config.input_signal_path, dtype=np.complex64)

        module = test_config.module_config.create_logical_instance()
        calc_output = module.compute(input_signal)

        test_output = np.fromfile(test_config.test_signal_path, dtype=np.float32)
        print(np.max(calc_output))
        print(np.max(test_output))
        print(np.max(calc_output) / np.max(test_output))
        # import matplotlib.pyplot as plt
        # plt.figure()
        # plt.plot(calc_output, label="calc")
        # plt.plot(test_output, label="test")
        # plt.legend()
        # plt.show()

        assert calc_output.shape == test_output.shape
        max_value = np.max(np.abs(np.concat([calc_output, test_output])))
        assert np.mean(np.abs(calc_output - test_output)) < test_config.tol * max_value
