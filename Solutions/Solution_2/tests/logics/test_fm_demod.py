import numpy as np
import pydantic
import pytest
import hydra
from omegaconf import OmegaConf

from Solutions.Solution_2.logics.computes.fm_demod import FmDemod
from Solutions.Solution_2.utils.cosine_similarity import cosine_similarity


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
    test_cfg = TestConfig.model_validate(test_cfg_dict)
    return test_cfg


class TestClass:
    @pytest.mark.parametrize("test_config", ["test_fm_demod_config"], indirect=True)
    def test_fm_demod(self, test_config: TestConfig):
        input_signal = np.fromfile(test_config.input_signal_path, dtype=np.complex64)

        module = test_config.module_config.create_logical_instance()
        calc_output = module.compute(input_signal)

        test_output = np.fromfile(test_config.test_signal_path, dtype=np.float32)

        assert calc_output.shape == test_output.shape
        assert cosine_similarity(calc_output, test_output) > 1 - test_config.tol
