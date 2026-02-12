import pytest

from qa_api.api_client import ApiClient
from qa_api.config import get_base_url, get_timeout


@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient(base_url=get_base_url(), timeout=get_timeout())
