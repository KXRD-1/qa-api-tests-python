# QA API Tests (Python)

Practice API test automation project built with Python + Pytest.
Includes API client abstraction, fixtures, parametrized tests, JSON Schema validation, and **GitHub Actions CI**.

## CI Status
![CI](https://github.com/KXRD-1/qa-api-tests-python/actions/workflows/ci.yml/badge.svg)

## Tech Stack
- Python
- Pytest
- Requests
- jsonschema
- GitHub Actions (CI)

## Project Structure
```text
.
├── src/
│   └── qa_api/
│       ├── __init__.py
│       ├── api_client.py
│       └── config.py
├── tests/
│   ├── conftest.py
│   └── test_reqres_users.py
├── requirements.txt
├── pytest.ini
└── .github/workflows/ci.yml
