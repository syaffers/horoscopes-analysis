# -*- coding: utf-8 -*-
from itertools import product
import scrapy

template_url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{}.aspx?sign={}'
days = ['yesterday', 'today', 'tomorrow']
signs_n = list(range(1, 13))
signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
         'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

class HoroscopeComSpider(scrapy.Spider):
    name = 'horoscope_com'
    allowed_domains = ['horoscope.com']
    start_urls = [
        template_url.format(day, sign) for day, sign in product(days, signs_n)]

    def parse(self, response):
        day = response.url.split('-')[-1].split('.')[0]
        sign = signs[int(response.url.split('=')[-1]) - 1]

        horoscope_css = '.horoscope-content p::text'
        horoscope = \
            response.css(horoscope_css)[1].extract().strip()

        yield {
            'sign': sign,
            'day': day,
            'horoscope': horoscope[2:]
        }
