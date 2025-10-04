from utils.github_fetcher import fetch_trending_repos
from config import LANGUAGES

def display_trending():
    for lang in LANGUAGES:
        print(f"\nTrending Repositories for {lang}:\n" + "-"*40)
        repos = fetch_trending_repos(lang)
        for repo in repos:
            print(f"{repo['name']} ⭐ {repo['stars']}\n{repo['url']}\n{repo['description']}\n")

if __name__ == "__main__":
    display_trending()
