# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/r/circlejerk',

'https://www.reddit.com/r/gaming',

'https://www.reddit.com/r/floridaman',

'https://www.reddit.com/r/movies',

'https://www.reddit.com/r/totallynotrobots',

'https://www.reddit.com/r/videos',

'https://www.reddit.com/r/worldnews']

    def parse(self, response):
          titles=response.xpath('//*[@class="pd8yw6-0 dZOwqG"]/text()').extract()
          votes=response.xpath('//*[@class="_1rZYMD_4xY3gRcSS3p8ODO"]/text()').extract()
          times=response.xpath('//*[@class="_3jOxDPIQ0KaOWpzvSQo-1s"]/text()').extract()
          comments=response.xpath('//*[@class="FHCV02u6Cp2zYL0fhQPsO"]/text()').extract()
          for item in zip(titles,votes,times,comments):
            yield{
                  'title':item[0],
                  'vote':item[1],
                  'time':item[2],
                  'comment':item[3],

              }
        #     pd8yw6-0 dZOwqG _1rZYMD_4xY3gRcSS3p8ODO FHCV02u6Cp2zYL0fhQPsO _3jOxDPIQ0KaOWpzvSQo-1s movies and gaming
        #      scrapped_info={
        #          'title': item[0],
        #          'vote': item[1],
        #          'time': item[2],
        #          'comment': item[3],
        #         }
        #
        #      yield scrapped_info





