import argparse

from modules.github import GitHubModule
from modules.username import UsernameModule
from modules.ipinfo import IPInfoModule
from modules.domain import DomainModule
from modules.dns import DNSModule

from utils.output import banner, print_json, save_json


def create_parser():
    parser = argparse.ArgumentParser(
        prog="pyosint",
        description="Public-data OSINT toolkit"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # -------------------------
    # Username
    # -------------------------

    username = subparsers.add_parser(
        "username",
        help="Search for a username on public platforms"
    )

    username.add_argument(
        "username",
        help="Username to search"
    )

    # -------------------------
    # GitHub
    # -------------------------

    github = subparsers.add_parser(
        "github",
        help="Collect public GitHub information"
    )

    github.add_argument(
        "username",
        help="GitHub username"
    )

    github.add_argument(
        "--repos",
        type=int,
        default=20,
        help="Maximum number of repositories"
    )

    github.add_argument(
        "--events",
        type=int,
        default=10,
        help="Number of recent public events"
    )

    # -------------------------
    # IP
    # -------------------------

    ip = subparsers.add_parser(
        "ip",
        help="Look up public information about an IP"
    )

    ip.add_argument(
        "address",
        help="IPv4 or IPv6 address"
    )

    # -------------------------
    # Domain
    # -------------------------

    domain = subparsers.add_parser(
        "domain",
        help="Analyze a domain"
    )

    domain.add_argument(
        "domain",
        help="Domain name"
    )

    # -------------------------
    # DNS
    # -------------------------

    dns = subparsers.add_parser(
        "dns",
        help="Query common DNS records"
    )

    dns.add_argument(
        "domain",
        help="Domain name"
    )

    # -------------------------
    # All
    # -------------------------

    all_command = subparsers.add_parser(
        "all",
        help="Run multiple public-data checks"
    )

    all_command.add_argument(
        "target",
        help="Username or target"
    )

    return parser


def run_all(target):
    result = {
        "target": target,
        "checks": {}
    }

    result["checks"]["username"] = (
        UsernameModule().search(target)
    )

    result["checks"]["github"] = (
        GitHubModule().search(
            target,
            repo_limit=10,
            event_limit=5
        )
    )

    return result


def main():
    parser = create_parser()
    args = parser.parse_args()

    banner()

    try:

        if args.command == "username":

            result = UsernameModule().search(
                args.username
            )

            filename_target = args.username

        elif args.command == "github":

            result = GitHubModule().search(
                args.username,
                repo_limit=args.repos,
                event_limit=args.events
            )

            filename_target = args.username

        elif args.command == "ip":

            result = IPInfoModule().lookup(
                args.address
            )

            filename_target = args.address

        elif args.command == "domain":

            result = DomainModule().lookup(
                args.domain
            )

            filename_target = args.domain

        elif args.command == "dns":

            result = DNSModule().lookup(
                args.domain
            )

            filename_target = args.domain

        elif args.command == "all":

            result = run_all(
                args.target
            )

            filename_target = args.target

        else:
            parser.print_help()
            return

        print_json(result)

        save_json(
            result,
            args.command,
            filename_target
        )

    except KeyboardInterrupt:
        print("\n[!] Interrupted.")

    except Exception as error:
        print(f"\n[!] Error: {error}")


if __name__ == "__main__":
    main()