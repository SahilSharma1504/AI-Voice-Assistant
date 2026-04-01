import webbrowser
import urllib.parse


def open_google():
    """
    Open Google homepage
    """
    webbrowser.open("https://www.google.com")
    return "Opening Google"


def open_youtube():
    """
    Open YouTube homepage
    """
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"


def search_google(query):
    """
    Search something on Google
    """
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"

    webbrowser.open(url)

    return f"Searching Google for {query}"


def open_website(url):
    """
    Open a specific website
    """

    if not url.startswith("http"):
        url = "https://" + url

    webbrowser.open(url)

    return f"Opening {url}"


def search_youtube(query):
    """
    Search videos on YouTube
    """

    encoded_query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}"

    webbrowser.open(url)

    return f"Searching YouTube for {query}"