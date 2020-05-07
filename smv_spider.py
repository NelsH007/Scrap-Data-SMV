# -*- coding: utf-8 -*-
import scrapy


class SmvSpiderSpider(scrapy.Spider):
    name = 'smv_spider'
    allowed_domains = ['https://www.smv.gob.pe']
    start_urls = ['https://www.smv.gob.pe/Frm_ReglamentoParticipacion1?data=52BDACCC78F35E9A17703490F4E40D4352FAF6A60C']

    def parse(self, response):
        tr = response.xpath('//tr[@class="item-grid"]')
        for row in tr:
            tipo_fm = row.xpath('.//td/text()').getall()[0].strip()
            den_social = row.xpath('.//td/text()').getall()[1].strip()
            desc = row.xpath('.//td/text()').getall()[2].strip()
            resol = row.xpath('.//td/text()').getall()[3].strip()
            fecha_ini = row.xpath('.//td/text()').getall()[4].strip()
            ps = row.xpath('.//td/a/@href').get()

            yield {'Tipo FM':tipo_fm,
                    'Denominación':den_social,
                    'Descripción':desc,
                    'Resolución': resol,
                    'Fecha de Inicio':fecha_ini,
                    'PS': ps}






