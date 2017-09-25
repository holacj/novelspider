#!/usr/bin/env python
#   -*- coding: UTF-8 -*-
#
#   Copyright (C) 2017 Chenji
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novelspider.items import NovelspiderItem


class BookSpider(CrawlSpider):
    print '================================11111111111111111111'
    name = 'book'
    allowed_domains = ['jjxsw.com']
    start_urls = ['http://jjxsw.com/']

    rules = (
        # 获取分类链接
        Rule(LinkExtractor(allow=(r'/[a-z]+/[a-zA-Z]+/$')), follow=True),
        # 获取小说入口链接
        Rule(LinkExtractor(allow=(r'/txt/\d+.htm')), follow=True),
        # 获取小说下载入口链接
        Rule(LinkExtractor(allow=(r'/txt/dl.+.html')), callback='parse_item'),
        # 获取分页链接
        Rule(LinkExtractor(allow=(r'/txt/\w+/')), follow=True),

    )



    def parse_item(self, response):

        item = NovelspiderItem()
        item["title"] = response.xpath("//div[@id='path']/a[2]/text()").extract()
        url = response.xpath("//a[@class='strong green'][1]/@href").extract()[0]
        item["size"] = response.xpath("//td[3]/span/text()").extract()

        item['url'] = 'http://www.jjxsw.com' + str(url)

        yield item




