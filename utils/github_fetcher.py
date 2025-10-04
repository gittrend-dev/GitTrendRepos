import requests
from config import GITHUB_API_URL, TOP_N

def fetch_trending_repos(language):
    """
    Fetch top N trending repositories for a language
    """
    params = {
        "q": f"language:{language}",
        "sort": "stars",
        "order": "desc",
        "per_page": TOP_N
    }
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(GITHUB_API_URL, params=params, headers=headers)
    if response.status_code == 200:
        repos = response.json().get("items", [])
        trending_list = []
        for r in repos:
            trending_list.append({
                "name": r["full_name"],
                "stars": r["stargazers_count"],
                "url": r["html_url"],
                "description": r["description"]
            })
        return trending_list
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
