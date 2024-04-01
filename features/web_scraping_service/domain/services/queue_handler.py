from collections import deque

import injector


class QueueHandler:
    @injector.inject
    def __init__(self):
        self.queue = deque()
        self.visited = set()

    def add_url(self, url, depth):
        normalized_url = url.rstrip("/")
        if normalized_url not in self.visited:
            self.queue.append((normalized_url, depth))
            self.visited.add(normalized_url)

    def get_next_url(self):
        if self.queue:
            return self.queue.popleft()
        return None, None

    def has_urls(self):
        return len(self.queue) > 0
