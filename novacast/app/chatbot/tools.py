from typing import Any, Dict, List
import requests

class ExternalAPIConnector:
    def __init__(self):
        self.wiki_api_url = "https://en.wikipedia.org/w/api.php"
        self.search_api_url = "https://api.example.com/search"
        self.youtube_api_url = "https://www.googleapis.com/youtube/v3/search"

    def search_wiki(self, query: str) -> Dict[str, Any]:
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }
        response = requests.get(self.wiki_api_url, params=params)
        return response.json()

    def search_external(self, query: str) -> List[Dict[str, Any]]:
        params = {"query": query}
        response = requests.get(self.search_api_url, params=params)
        return response.json().get("results", [])

    def search_youtube(self, query: str, api_key: str) -> Dict[str, Any]:
        params = {
            "part": "snippet",
            "q": query,
            "key": api_key,
            "type": "video"
        }
        response = requests.get(self.youtube_api_url, params=params)
        return response.json()