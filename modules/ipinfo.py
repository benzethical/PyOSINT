import ipaddress
import requests

from config import IPINFO_API
from config import API_TIMEOUT
from config import USER_AGENT


class IPInfoModule:

    def lookup(self, address):

        address = address.strip()

        # Validate IP
        ipaddress.ip_address(address)

        url = f"{IPINFO_API}/{address}/json"

        response = requests.get(
            url,
            timeout=API_TIMEOUT,
            headers={
                "User-Agent": USER_AGENT
            }
        )

        response.raise_for_status()

        data = response.json()

        # Extract coordinates
        latitude = None
        longitude = None

        if data.get("loc"):
            try:
                latitude, longitude = map(
                    float,
                    data["loc"].split(",")
                )
            except (ValueError, AttributeError):
                pass

        return {
            "ip": data.get("ip"),
            "hostname": data.get("hostname"),

            "location": {
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country"),
                "postal": data.get("postal"),
                "latitude": latitude,
                "longitude": longitude
            },

            "organization": data.get("org"),
            "timezone": data.get("timezone"),

            "source": "ipinfo.io"
        }