import os


def get_base_url() -> str:
    # Allow override via env var (useful for CI and future real APIs)
    return os.getenv("QA_API_BASE_URL", "https://jsonplaceholder.typicode.com")


def get_timeout() -> int:
    value = os.getenv("QA_API_TIMEOUT", "10")
    return int(value)
