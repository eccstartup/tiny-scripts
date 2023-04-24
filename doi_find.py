import requests


def get_doi(title, author=None):
    url = "https://api.crossref.org/works"
    params = {
        "query.title": '+'.join(title.lower().split()),
        "query.author": '+'.join(author.lower().split()) if author else None,
        "rows": 10
    }
    r = requests.get(url, params=params)
    # print(r.json())
    data = r.json()["message"]
    print(data["total-results"])
    if data["total-results"] > 0:
        doi = data["items"][0]["URL"]
        print(f"Found DOI for {title}: {doi}")
        return doi
    else:
        print(f"No DOI found for {title}")
        return None


if __name__ == "__main__":
    title = 'Differential Neural Networks (DNN)'
    author = 'SERGIO LEDESMA'
    doi = get_doi(title, author)
