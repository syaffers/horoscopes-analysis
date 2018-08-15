# Horoscopes Analysis

Lots to write here but I'll let the IPYNB explain more of it.

## Getting started

Create a new Anaconda environment with the `.yml` file:

    conda env create --file=environment.yml

To run the scraper:

    scrapy crawl horoscope_com -o horoscope_com.json
    scrapy crawl astrology -o astrology.json

To play around with the analysis:

    jupyter-notebook
