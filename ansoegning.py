from functools import partial
from typing import List

from injector import Injector

from features.network_analysis_service.domain.usecases.analyze_network import (
    AnalyzeNetwork,
)
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
        analyze_network_instance = inj.get(AnalyzeNetwork)
        combined_func = partial(
            combined_usecase,
            scraping_instance,
            analyze_network_instance,
            "https://sik.dk",
            1,
        )
        self.add_case(CaseWrapper(combined_func))

    def add_case(self, case):
        self.cases.append(case)


class Stedord:
    def __init__(self, grundform, ejefald):
        self.grundform = grundform
        self.ejefald = ejefald


class CaseWrapper:
    def __init__(self, func, formatter=None, saver=None):
        self.func = func
        self.formatter = formatter
        self.saver = saver

    def beregn(self):
        result = self.func()
        if self.formatter:
            result = self.formatter(result)
        if self.saver:
            self.saver(result)
        return result


def combined_usecase(scraping_instance, analyze_instance, url, depth):
    website_network = scraping_instance.execute(url, depth)
    print(PerformDepthLimitedScrapingPresenter.format_website_network(website_network))
    PerformDepthLimitedScrapingPresenter.save_website_network_to_file(website_network)
    analysis_result = analyze_instance.execute()
    return analysis_result
