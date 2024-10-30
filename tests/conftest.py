import pytest
import pandas as pd


filenames = ["./tests/data/test_data.csv"] 

@pytest.fixture(params=filenames)
def dummy_ohlc(request):
    df = pd.read_csv(request.param)
    return df



