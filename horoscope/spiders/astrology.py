# -*- coding: utf-8 -*-
from itertools import product
import scrapy

template_url = 'https://www.astrology.com/horoscope/daily/{}/{}.html'
days = ['yesterday', 'today', 'tomorrow']
signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
         'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

class AstrologySpider(scrapy.Spider):
    name = 'astrology'
    allowed_domains = ['astrology.com']
    start_urls = [
        template_url.format(day, sign) for day, sign in product(days, signs)]

    def parse(self, response):
        day = response.url.split('/')[-2]
        sign = response.url.split('/')[-1].split('.')[0]

        horoscope_css = '.daily-horoscope p::text'
        horoscope = response.css(horoscope_css).extract_first().strip()

        yield {
            'sign': sign,
            'day': day,
            'horoscope': horoscope
        }
