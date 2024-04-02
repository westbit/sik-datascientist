from features.web_scraping_service.domain.entities.website import Website


class WebsiteModel:
    def __init__(self, url: str, links: list[str]):
        self.url = url
        self.links = links

    def from_entity(self, entity: Website):
        return WebsiteModel(entity.url, entity.links)

    def to_entity(self):
        return Website(self.url, self.links)
