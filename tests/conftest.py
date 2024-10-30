import pytest
import pandas as pd
from simple_backtester import SBStrat

filenames = ["./tests/data/test_data.csv"]


class EmptyStrat(SBStrat):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SimpleStrat(SBStrat):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@pytest.fixture(params=filenames)
def dummy_ohlc(request):
    df = pd.read_csv(request.param)
    return df


# Barebones SBStrat without data added
@pytest.fixture
def dummy_strat_empty():
    return EmptyStrat()


# Barebones SBStrat with data added
@pytest.fixture
def dummy_strat(dummy_ohlc):
    strat = EmptyStrat()
    strat.add_data(dummy_ohlc)
    return strat
