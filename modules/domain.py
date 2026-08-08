import socket

import requests

from urllib.parse import urlparse

from config import API_TIMEOUT
from config import USER_AGENT


class DomainModule:

    def lookup(self, domain):

        domain = domain.strip()

        if "://" not in domain:

            domain = (
                "https://" + domain
            )

        parsed = urlparse(domain)

        hostname = parsed.hostname

        if not hostname:

            raise ValueError(
                "Invalid domain."
            )

        result = {
            "domain": hostname
        }

        # DNS resolution

        try:

            addresses = socket.getaddrinfo(
                hostname,
                None
            )

            result["addresses"] = sorted(
                set(
                    item[4][0]
                    for item in addresses
                )
            )

        except socket.gaierror:

            result["addresses"] = []

        # HTTP information

        try:

            response = requests.get(
                domain,
                timeout=API_TIMEOUT,
                headers={
                    "User-Agent": USER_AGENT
                },
                allow_redirects=True
            )

            result["http"] = {

                "status":
                    response.status_code,

                "final_url":
                    response.url,

                "server":
                    response.headers.get(
                        "Server"
                    ),

                "content_type":
                    response.headers.get(
                        "Content-Type"
                    ),

                "powered_by":
                    response.headers.get(
                        "X-Powered-By"
                    )
            }

        except requests.RequestException as error:

            result["http_error"] = str(
                error
            )

        return result