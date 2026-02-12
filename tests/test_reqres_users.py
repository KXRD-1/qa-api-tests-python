import pytest
from jsonschema import validate

from qa_api.api_client import ApiClient


@pytest.mark.parametrize(
    "path, expected_status",
    [
        ("/posts", 200),
        ("/posts/1", 200),
        ("/posts/999999", 404),
        ("/users", 200),
        ("/users/1", 200),
        ("/users/999999", 404),
    ],
)
def test_endpoints_status_codes(api_client: ApiClient, path: str, expected_status: int):
    response = api_client.get(path)
    assert response.status_code == expected_status


def test_posts_list_has_expected_fields(api_client: ApiClient):
    response = api_client.get("/posts")
    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0

    first = body[0]
    assert "userId" in first
    assert "id" in first
    assert "title" in first
    assert "body" in first


def test_single_post_matches_schema(api_client: ApiClient):
    response = api_client.get("/posts/1")
    assert response.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"},
        },
        "required": ["userId", "id", "title", "body"],
        "additionalProperties": True,
    }

    validate(instance=response.json(), schema=schema)
