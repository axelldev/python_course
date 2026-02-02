sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_trad(data: list) -> list[str]:
    """Extracts and returns all the titles from the data."""
    titles: list[str] = []
    for item in data:
        titles.append(item["title"])
    return titles


def extract_titles(data: list) -> list[str]:
    """Extracts and returns all the titles from the data."""
    return [item["title"] for item in data if len(item["title"]) > 10]


def extract_summaries(data: list) -> dict:
    return {
        item["title"]: item["description"]
        for item in data
        if len(item["description"]) > 10
    }


def get_unique_sources_trad(data: list[dict]) -> set[str]:
    sources = set[str]()
    for item in data:
        if item.get("source") and item.get("source").get("name"):
            sources.add(item.get("source").get("name"))
    return sources


def get_unique_sources(data: list[dict]) -> set[str]:
    return {
        item.get("source").get("name")
        for item in data
        if item.get("source") and item.get("source").get("name")
    }


print("==== List comprehension ====")
print(extract_titles(sample_articles))
print(extract_titles(sample_articles))
print("==== Dict comprehension ====")
print(extract_summaries(sample_articles))
print("==== Set comprehension ====")
print(get_unique_sources(sample_articles))
print(get_unique_sources_trad(sample_articles))
