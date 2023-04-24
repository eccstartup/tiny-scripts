import requests


def get_doi(title):
    url = "https://api.crossref.org/works"
    params = {
        "query.title": title,
        "rows": 1
    }
    r = requests.get(url, params=params)
    print(r.json())
    data = r.json()["message"]
    if data["total-results"] > 0:
        doi = data["items"][0]["URL"]
        print(f"Found DOI for {title}: {doi}")
        return doi
    else:
        print(f"No DOI found for {title}")
        return None


if __name__ == "__main__":
    title = '联邦学习系统攻击与防御技术研究综述'
    doi = get_doi(title)
