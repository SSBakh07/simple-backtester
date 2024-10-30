import pytest
from simple_backtester import SBDataSrc
import pandas as pd
import numpy as np


### For data-related functionality


@pytest.mark.data
@pytest.mark.filterwarnings(
    "ignore:Could not infer format"
)  # Regarding date in dummy_ohlc
class TestStratData:
    # Adding a CSV as our data source
    def test_add_data_csv(self, dummy_strat_empty, dummy_ohlc):
        dummy_strat_empty.add_data(dummy_ohlc)

        assert dummy_strat_empty.main_datasrc.length == len(dummy_ohlc)

    # Adding data as a direct SBDataSrc object
    def test_add_data_sbsdata(self, dummy_strat_empty, dummy_ohlc):
        sb_datasrc = SBDataSrc(dummy_ohlc)
        dummy_strat_empty.add_data(sb_datasrc)

        assert dummy_strat_empty.main_datasrc.length == len(dummy_ohlc)

    # Test empty data / data with no rows to iterate over
    def test_empty(self, dummy_strat_empty, dummy_ohlc):
        empty_csv = pd.DataFrame(columns=dummy_ohlc.columns)

        with pytest.warns(UserWarning, match="length of 0"):
            dummy_strat_empty.add_data(empty_csv)

        dummy_strat_empty.start()

    # Test if missing columns are being handled correctly
    @pytest.mark.parametrize("column_name", ["high", "low", "open", "close"])
    def test_missing_col(self, column_name, dummy_strat_empty, dummy_ohlc):
        dummy_ohlc.drop(column_name, inplace=True, axis=1)
        with pytest.warns(UserWarning, match="not found"):
            dummy_strat_empty.add_data(dummy_ohlc)

    # Test if data type is iterating correctly
    def test_data_iteration(self, dummy_strat_empty, dummy_ohlc):
        dummy_strat_empty.add_data(dummy_ohlc)

        assert not dummy_strat_empty.is_finished

        # Manual iteration
        for i in range(len(dummy_strat_empty.data)):
            dummy_strat_empty._step()
            assert dummy_strat_empty.data.iloc[i].equals(dummy_ohlc.iloc[i])
            assert dummy_strat_empty.main_datasrc.current_idx == i

        assert dummy_strat_empty.is_finished

        # Function call iteration
        dummy_strat_empty.reset()
        assert not dummy_strat_empty.is_finished
        dummy_strat_empty.start()
        assert dummy_strat_empty.is_finished
