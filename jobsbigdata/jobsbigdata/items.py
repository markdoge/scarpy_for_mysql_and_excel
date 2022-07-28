# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsbigdataItem(scrapy.Item):
    job_name = scrapy.Field()
    job_exp = scrapy.Field()
    job_location = scrapy.Field()
    job_corporate = scrapy.Field()
    job_link = scrapy.Field()
    job_type = scrapy.Field()
    job_Recruiter = scrapy.Field()
    job_salary_low = scrapy.Field()
    job_salary_high = scrapy.Field()
    job_salary_bounty = scrapy.Field()
    pass
