from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


@dataclass
class ApiClient:
    """
    Small wrapper around requests to keep tests clean.
    Adds:
      - default headers
      - retries for transient failures
      - shared session for performance
    """
    base_url: str
    timeout: int = 10
    headers: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.session = requests.Session()

        # Reasonable retry strategy for flaky network/5xx
        retry = Retry(
            total=3,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 503, 504),
            allowed_methods=("GET", "POST", "PUT", "DELETE"),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Set default headers (helpful for some public endpoints / future real APIs)
        if "User-Agent" not in self.headers:
            self.headers["User-Agent"] = "qa-api-tests-python/1.0"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        return self.session.get(url, params=params, headers=self.headers, timeout=self.timeout)
