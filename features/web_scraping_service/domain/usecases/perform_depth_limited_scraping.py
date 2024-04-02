import injector

from features.web_scraping_service.domain.entities.website_network import WebsiteNetwork
from features.web_scraping_service.domain.services.queue_handler import QueueHandler
from features.web_scraping_service.domain.usecases.scrape_website import ScrapeWebsite


class PerformDepthLimitedScraping:
    @injector.inject
    def __init__(self, scrape_website: ScrapeWebsite, queue_handler: QueueHandler):
        self.scrape_website = scrape_website
        self.queue_handler = queue_handler

    def execute(self, url: str, depth: int = 1) -> WebsiteNetwork:
        website_network = WebsiteNetwork()
        self.queue_handler.add_url(url, 0)

        while self.queue_handler.has_urls():
            current_url, current_depth = self.queue_handler.get_next_url()
            if current_depth > depth:
                break

            try:
                result = self.scrape_website.execute(current_url)
                website_network.add_website(result)
                if current_depth < depth:
                    for link in result.links:
                        self.queue_handler.add_url(link, current_depth + 1)
            except Exception as e:
                raise Exception(f"Fejl ved scraping af {current_url}: {e}")

        return website_network
