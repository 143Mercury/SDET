
 https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter


class MyprojectPipeline:
    def process_item(self, item, spider):
        return item
