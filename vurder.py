import injector
from ansoegning import PyUdvikler
from core.di.app_module import AppModule
from features.web_scraping_service.domain.usecases.perform_depth_limited_scraping import PerformDepthLimitedScraping
from functools import partial


def main():
    # Dependency injection
    inj = injector.Injector([AppModule])

    # Forudkonfigurer PerformDepthLimitedScraping med 'sik.dk' og ønsket dybde
    configured_scraping = partial(inj.get(PerformDepthLimitedScraping), url="http://sik.dk", depth=2)
    
    pyudv = PyUdvikler()
    pyudv.add_case(configured_scraping)
    
    
    
    print(
        f"{pyudv.kaldenavn} har sgt jobbet som py-udvikler.\n"
        f"Dette er en gennemgang af {pyudv.stedord.ejefald} ansøgning.\n"
        f"Nu gennemgår vi de {len(pyudv.cases)} cases:"
    )

    for n in range(len(pyudv.cases)):
        res = pyudv.cases[n].beregn()
        print(
            f"case nummer {n + 1} er beregnet for {pyudv.kaldenavn}.\n"
            f"{pyudv.stedord.grundform.title()} får resultatet:"
        )
        print(res)


if __name__ == "__main__":
    main()
