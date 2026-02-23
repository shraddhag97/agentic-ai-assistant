import requests
from bs4 import BeautifulSoup

def search_web(topic):
    """Search web using DuckDuckGo lite HTML (more stable)"""
    
    url = "https://lite.duckduckgo.com/lite/"
    data = {"q": topic}

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post(url, data=data, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "http" in href and not href.startswith("/"):
            links.append(href)
        if len(links) >= 5:
            break

    return links


def extract_text_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        return text[:3000]
    except:
        return ""