import pytest
from simple_backtester import SBStrat, SBDataSrc


class SampleStrat(SBStrat):
    def __init__(self, **kwargs):
        super().__init__(kwargs)


class TestStrat:      
    @pytest.mark.filterwarnings("ignore:Could not infer format")    
    def test_add_data_csv(self, dummy_ohlc):
        strat = SampleStrat()
        
        strat.add_data(dummy_ohlc)
        
        assert strat.main_datasrc.length == len(dummy_ohlc)
        