from functools import partial
from typing import List

from injector import Injector

from features.web_scraping_service.domain.usecases.perform_depth_limited_scraping import (
    PerformDepthLimitedScraping,
)
from features.web_scraping_service.presentation.perform_depth_limited_scraping_presenter import (
    PerformDepthLimitedScrapingPresenter,
)


class PyUdvikler:
    def __init__(self, inj: Injector):
        self.cases: List[CaseWrapper] = []
        self.kaldenavn = "Erik Valbjørn Jensen"
        self.stedord = Stedord("Erik", "Eriks")
        scraping_instance = inj.get(PerformDepthLimitedScraping)
        configured_scraping = partial(
            scraping_instance.execute, url="https://sik.dk", depth=1
        )
        self.add_case(
            CaseWrapper(
                configured_scraping,
                PerformDepthLimitedScrapingPresenter.format_website_network,
            )
        )

    def add_case(self, case):
        self.cases.append(case)


class Stedord:
    def __init__(self, grundform, ejefald):
        self.grundform = grundform
        self.ejefald = ejefald


class CaseWrapper:
    def __init__(self, func, formatter=None):
        self.func = func
        self.formatter = formatter

    def beregn(self):
        result = self.func()
        if self.formatter:
            formatted_result = self.formatter(result)
            PerformDepthLimitedScrapingPresenter.save_website_network_to_file(result)
            return formatted_result
        return result
