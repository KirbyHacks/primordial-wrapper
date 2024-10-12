import pytest
from unittest.mock import patch
from primordial_wrapper import PrimordialAPI

SUCCESS_RESPONSE = {
    "status": "success",
    "result": {
        "message": "AI response generated successfully",
        "data": "Generated content based on prompt"
    }
}

ERROR_RESPONSE = {
    "status": "error",
    "result": {
        "message": "Unauthorized access"
    }
}

@pytest.fixture
def api_client():
    return PrimordialAPI(api_key="your_api_key")

@patch('primordial_wrapper.api_wrapper.requests.get')
def test_generate_ai_response_success(mock_get, api_client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = SUCCESS_RESPONSE
    
    prompt = "Hello World!"
    response = api_client.generate_ai_response(prompt)
    
    mock_get.assert_called_once_with(
        f"{api_client.base_url}/ai/generate",
        headers=api_client.headers,
        params={"prompt": prompt}
    )
    assert response == SUCCESS_RESPONSE

@patch('primordial_wrapper.api_wrapper.requests.get')
def test_generate_ai_response_unauthorized(mock_get, api_client):
    mock_get.return_value.status_code = 401
    mock_get.return_value.json.return_value = ERROR_RESPONSE
    
    prompt = "Hello World!"
    response = api_client.generate_ai_response(prompt)
    
    mock_get.assert_called_once_with(
        f"{api_client.base_url}/ai/generate",
        headers=api_client.headers,
        params={"prompt": prompt}
    )
    assert response == ERROR_RESPONSE
