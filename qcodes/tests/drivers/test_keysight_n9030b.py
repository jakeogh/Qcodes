import pytest

import qcodes.instrument_drivers.Keysight.N9030B as N9030B
import qcodes.instrument.sims as sims

VISALIB = sims.__file__.replace('__init__.py', 'Keysight_N9030B.yaml@sim')


@pytest.fixture(name="driver")
def _make_driver():
    driver = N9030B.N9030B('n9030B_sim',
                          address="GPIB::1::INSTR",
                          visalib=VISALIB)
    yield driver
    driver.close()


@pytest.fixture(name="sa")
def _activate_sa_mode(driver):
    sa = driver.SA
    yield sa

@pytest.fixture(name="pnoise")
def _activate_pnoise_mode(driver):
    pn = driver.PNoise
    yield pn


def test_idn(driver):
    assert {'firmware': '0.1',
            'model': 'N9030B',
            'serial': '1000',
            'vendor': 'Keysight Technologies'} == driver.IDN()
