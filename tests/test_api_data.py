import pytest
import json
from requests.models import Response
import pickle

from src.api_data import coinmarket_api_data

def test_successful_call(mocker):
    """This method tests the phone number validator."""

    with open('./resources/response_200.pkl', 'rb') as f:
        mock_response = pickle.load(f)
    mock = mocker.patch("src.api_data.requests")
    mock.get.return_value = mock_response
    response = coinmarket_api_data("fake_api_key")
    assert response == json.loads(mock_response.text)

def test_no_valid_api_key_call(mocker):
    """This method tests the phone number validator."""
    with pytest.raises(Exception):

        with open('./resources/response_401.pkl', 'rb') as f:
            mock_response = pickle.load(f)
        mock = mocker.patch("src.api_data.requests")
        mock.get.return_value = mock_response
        response = coinmarket_api_data("fake_api_key")
