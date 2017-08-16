import scrapy


from goodreads_web_scraper.utils.parsing import extract_id_from_book_show_link


class GenresNewReleasesSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.goodreads.com/genres/new_releases/high-fantasy']

    def parse(self, response):
        book_cover_container = response.css('div.coverBigBox.bigBox')

        for cover in book_cover_container.css('div.coverWrapper'):
            rel_link = cover.xpath('.//a/@href').extract_first()
            id_ = extract_id_from_book_show_link(rel_link)
            title = cover.xpath('.//img/@alt').extract_first()
            yield {
                'id': id_,
                'title': title,
            }
