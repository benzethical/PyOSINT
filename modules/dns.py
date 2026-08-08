import dns.resolver


class DNSModule:

    RECORD_TYPES = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME"
    ]

    def lookup(self, domain):

        domain = domain.strip()

        result = {
            "domain": domain,
            "records": {}
        }

        resolver = dns.resolver.Resolver()

        resolver.lifetime = 5

        for record_type in self.RECORD_TYPES:

            try:

                answers = resolver.resolve(
                    domain,
                    record_type
                )

                result["records"][
                    record_type
                ] = [
                    answer.to_text()
                    for answer in answers
                ]

            except Exception:

                result["records"][
                    record_type
                ] = []

        return result