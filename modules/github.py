import requests

from config import GITHUB_API, API_TIMEOUT, USER_AGENT


class GitHubModule:

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/vnd.github+json",
            "User-Agent": USER_AGENT
        })

    def get(self, endpoint, params=None):

        url = GITHUB_API + endpoint

        response = self.session.get(
            url,
            params=params,
            timeout=API_TIMEOUT
        )

        if response.status_code == 404:
            return None

        if response.status_code == 403:
            raise RuntimeError(
                "GitHub API rate limit reached."
            )

        response.raise_for_status()

        return response.json()

    def search(
        self,
        username,
        repo_limit=20,
        event_limit=10
    ):

        user = self.get(
            f"/users/{username}"
        )

        if not user:

            return {
                "found": False,
                "username": username
            }

        repo_limit = max(
            1,
            min(repo_limit, 100)
        )

        event_limit = max(
            1,
            min(event_limit, 30)
        )

        repositories = self.get(
            f"/users/{username}/repos",
            params={
                "sort": "updated",
                "direction": "desc",
                "per_page": repo_limit
            }
        ) or []

        events = self.get(
            f"/users/{username}/events/public",
            params={
                "per_page": event_limit
            }
        ) or []

        profile = {
            "username": user.get("login"),
            "name": user.get("name"),
            "bio": user.get("bio"),
            "company": user.get("company"),
            "location": user.get("location"),
            "website": user.get("blog"),
            "twitter": user.get("twitter_username"),
            "followers": user.get("followers"),
            "following": user.get("following"),
            "public_repositories": user.get(
                "public_repos"
            ),
            "public_gists": user.get(
                "public_gists"
            ),
            "created_at": user.get(
                "created_at"
            ),
            "updated_at": user.get(
                "updated_at"
            ),
            "profile_url": user.get(
                "html_url"
            ),
            "avatar_url": user.get(
                "avatar_url"
            )
        }

        repo_data = []

        for repo in repositories:

            repo_data.append({
                "name": repo.get("name"),
                "description": repo.get(
                    "description"
                ),
                "language": repo.get(
                    "language"
                ),
                "stars": repo.get(
                    "stargazers_count"
                ),
                "forks": repo.get(
                    "forks_count"
                ),
                "watchers": repo.get(
                    "watchers_count"
                ),
                "open_issues": repo.get(
                    "open_issues_count"
                ),
                "is_fork": repo.get(
                    "fork"
                ),
                "created_at": repo.get(
                    "created_at"
                ),
                "updated_at": repo.get(
                    "updated_at"
                ),
                "default_branch": repo.get(
                    "default_branch"
                ),
                "url": repo.get(
                    "html_url"
                )
            })

        event_data = []

        for event in events:

            event_data.append({
                "type": event.get(
                    "type"
                ),
                "repository": event.get(
                    "repo", {}
                ).get(
                    "name"
                ),
                "created_at": event.get(
                    "created_at"
                )
            })

        return {
            "found": True,
            "profile": profile,
            "repositories": repo_data,
            "recent_activity": event_data
        }