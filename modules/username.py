import requests

from config import API_TIMEOUT, USER_AGENT


class UsernameModule:

    SITES = {
        # Social media
        "Instagram": "https://www.instagram.com/{username}/",
        "YouTube": "https://www.youtube.com/@{username}",
        "TikTok": "https://www.tiktok.com/@{username}",
        "X": "https://x.com/{username}",
        "Facebook": "https://www.facebook.com/{username}",
        "Threads": "https://www.threads.net/@{username}",
        "Pinterest": "https://www.pinterest.com/{username}/",
        "Snapchat": "https://www.snapchat.com/add/{username}",
        "Telegram": "https://t.me/{username}",
        "Twitch": "https://www.twitch.tv/{username}",
        "Discord": "https://discord.com/users/{username}",

        # Developer / tech
        "GitHub": "https://github.com/{username}",
        "GitLab": "https://gitlab.com/{username}",
        "Bitbucket": "https://bitbucket.org/{username}/",
        "Codeberg": "https://codeberg.org/{username}",
        "Dev.to": "https://dev.to/{username}",
        "Stack Overflow": "https://stackoverflow.com/users/{username}",
        "HackerRank": "https://www.hackerrank.com/profile/{username}",
        "CodePen": "https://codepen.io/{username}",
        "Replit": "https://replit.com/@{username}",
        "Kaggle": "https://www.kaggle.com/{username}",
        "LeetCode": "https://leetcode.com/u/{username}/",
        "Hugging Face": "https://huggingface.co/{username}",

        # Community
        "Reddit": "https://www.reddit.com/user/{username}/",
        "Quora": "https://www.quora.com/profile/{username}",
        "Keybase": "https://keybase.io/{username}",
        "Medium": "https://medium.com/@{username}",
        "Substack": "https://{username}.substack.com/",
        "Mastodon": "https://mastodon.social/@{username}",

        # Creative
        "Behance": "https://www.behance.net/{username}",
        "Dribbble": "https://dribbble.com/{username}",
        "DeviantArt": "https://www.deviantart.com/{username}",
        "ArtStation": "https://www.artstation.com/{username}",
        "Flickr": "https://www.flickr.com/people/{username}/",
        "500px": "https://500px.com/p/{username}",

        # Music
        "SoundCloud": "https://soundcloud.com/{username}",
        "Bandcamp": "https://{username}.bandcamp.com/",
        "Mixcloud": "https://www.mixcloud.com/{username}/",

        # Professional
        "LinkedIn": "https://www.linkedin.com/in/{username}/",
        "About.me": "https://about.me/{username}",

        # Gaming
        "Steam": "https://steamcommunity.com/id/{username}",
        "Xbox": "https://www.xbox.com/en-US/play/user/{username}",
        "Chess.com": "https://www.chess.com/member/{username}",
        "Roblox": "https://www.roblox.com/user.aspx?username={username}",

        # Other
        "Gumroad": "https://{username}.gumroad.com/",
        "Ko-fi": "https://ko-fi.com/{username}",
        "Buy Me a Coffee": "https://www.buymeacoffee.com/{username}",
    }

    def search(self, username):

        username = username.strip()

        results = {}

        session = requests.Session()

        session.headers.update({
            "User-Agent": USER_AGENT
        })

        for name, template in self.SITES.items():

            url = template.format(
                username=username
            )

            try:

                response = session.get(
                    url,
                    timeout=API_TIMEOUT,
                    allow_redirects=True
                )

                results[name] = {
                    "url": url,
                    "status": response.status_code,
                    "exists": response.status_code == 200
                }

            except requests.RequestException as error:

                results[name] = {
                    "url": url,
                    "status": None,
                    "exists": None,
                    "error": str(error)
                }

        found = {
            name: data
            for name, data in results.items()
            if data["exists"] is True
        }

        return {
            "username": username,
            "total_sites_checked": len(results),
            "possible_matches": len(found),
            "matches": found,
            "all_results": results
        }