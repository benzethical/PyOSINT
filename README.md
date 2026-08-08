<p align="center">
  <img align="center" width="450px" src="https://github.com/benzethical/PyOSINT/blob/main/banner.png">
</p> 

<h1 align="center">PyOSINT</h1>
PyOSINT is a modular Python-based OSINT toolkit designed to collect and analyze publicly available information from multiple online sources.

The toolkit combines several reconnaissance utilities into a single command-line interface, including **username searching, GitHub enumeration, IP information lookup, domain analysis, and DNS reconnaissance**.

### Features

* 🔎 Username search across multiple public platforms
* 🐙 GitHub profile and repository enumeration
* 🌐 IP address information and geolocation metadata
* 🔗 Domain and HTTP information gathering
* 📡 DNS record enumeration
* 📊 Structured JSON reports
* 🛠️ Modular architecture for adding new OSINT modules
* ⚡ Command-line flags and subcommands
* 💾 Automatic report exporting

### Example

```bash
python main.py username target
python main.py github target --repos 50 --events 20
python main.py ip 8.8.8.8
python main.py domain example.com
python main.py dns example.com
```

## How to use
```bash
pip install -r requirements.txt
python main.py --help or python main.py -h
```
## Common Issues
--> pip command not working while installing the requirements.
```bash
py -m pip install requirements.txt
```
--> python command not working while using the tool.
```bash
use python3 instead of python. Make sure that python is installed.
```
## Report an issue
If you want to report any issue or bug, You can contact on Discord.
https://discord.gg/whqNrKRFtm

PyOSINT is intended for **ethical hacking, cybersecurity research, digital investigations, education, and authorized OSINT activities**. It focuses on information that is already publicly accessible and does not attempt to bypass authentication, access private accounts, or circumvent security controls.

