from features.web_scraping_service.domain.entities.website_network import WebsiteNetwork


class PerformDepthLimitedScrapingPresenter:
    @staticmethod
    def format_website_network(website_network: WebsiteNetwork) -> str:
        total_links = sum(len(website["links"]) for website in website_network.websites)
        formatted_resultat = (
            f"Antal unikke hjemmesider fundet: {len(website_network.websites)}\n"
            f"Totalt antal links fundet: {total_links}\n"
        )
        for website in website_network.websites:
            formatted_resultat += (
                f"- {website['url']} henviser til {len(website['links'])} andre links\n"
            )
        return formatted_resultat

    @staticmethod
    def save_website_network_to_file(website_network: WebsiteNetwork):
        website_network.save()
