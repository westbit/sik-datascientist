import json
import os

from features.web_scraping_service.domain.entities.website import Website


class WebsiteNetwork:
    def __init__(self):
        self.websites = []

    def add_website(self, website: Website):
        self.websites.append({"url": website.url, "links": website.links})

    def to_json(self):
        nodes = [{"id": website["url"]} for website in self.websites]
        edges = []
        for website in self.websites:
            for link in website["links"]:
                edges.append({"source": website["url"], "target": link})
        network_dict = {"nodes": nodes, "edges": edges}
        return json.dumps(network_dict, indent=4)

    def from_json(self, data):
        self.websites.clear()  # Clear existing data
        for node in data["nodes"]:
            website = Website(url=node["id"], links=[])
            self.websites.append({"url": website.url, "links": website.links})
        for edge in data["edges"]:
            for website in self.websites:
                if website["url"] == edge["source"]:
                    website["links"].append(edge["target"])
                    break

    def save(self, file_name="website_network.json"):
        json_data = self.to_json()
        root_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
        )
        file_path = os.path.join(root_dir, file_name)
        with open(file_path, "w") as file:
            file.write(json_data)

    def load(self, file_name="website_network.json"):
        root_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
        )
        file_path = os.path.join(root_dir, file_name)
        with open(file_path, "r") as file:
            data = json.load(file)
        self.from_json(data)
