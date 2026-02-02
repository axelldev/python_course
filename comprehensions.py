from typing import Callable


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
        if len(item["description"]) > 20
    }


print("==== List comprehension ====")
print(extract_titles(sample_articles))
print(extract_titles(sample_articles))
print("==== Dict comprehension ====")
print(extract_summaries(sample_articles))
