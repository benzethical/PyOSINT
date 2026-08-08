import json

from pathlib import Path

from datetime import datetime


def banner():

    print(r"""
 ____        ___  ____ ___ _   _ _____
|  _ \ _   _/ _ \/ ___/ _ \ \ | |_   _|
| |_) | | | | | | |  | | | |\ \| | | |
|  __/| |_| | |_| |__| |_| | |\   | | |
|_|    \__, |\___/ \____\___/ |_| \_| |_|
       |___/

        Public OSINT Toolkit
""")


def print_json(data):

    print(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )
    )


def save_json(
    data,
    command,
    target
):

    output_directory = Path(
        "output"
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    # Make filename filesystem-safe

    safe_target = (
        str(target)
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{command}_"
        f"{safe_target}_"
        f"{timestamp}.json"
    )

    path = (
        output_directory /
        filename
    )

    path.write_text(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    print(
        f"\n[+] Report saved: {path}"
    )