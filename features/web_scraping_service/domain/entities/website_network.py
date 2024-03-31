from features.web_scraping_service.domain.entities.website import Website


class WebsiteNetwork:
    def __init__(self):
        self.websites = []

    def add_website(self, website: Website):
        self.websites.append({"url": website.url, "links": website.links})
