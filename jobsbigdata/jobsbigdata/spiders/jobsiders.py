import xlsxwriter as xw
import scrapy
from jobsbigdata.items import JobsbigdataItem

# workbook = xw.Workbook("Hispanic.xlsx")
# f = workbook.add_worksheet("sheet1")
# title = ["名称", "经验", "学历", "薪资", "薪资最低", "薪资最高", "奖金", "地点", "公司", "类型", "链接"]
# f.write_row('A1', title)


class JobsidersSpider(scrapy.Spider):
    name = 'jobsiders'
    page = 0
    counter = 2
    baseURl = "https://www.liepin.com/zhaopin/?headId=8f9ff24a0572d19ed3dbbe486f3a621c&ckId=w19h7yat71j9mylw345ylqj319t2qzb8&oldCkId=8f9ff24a0572d19ed3dbbe486f3a621c&fkId=eiwvgjswvfc646yy6x0brph7pyt1vpqa&skId=eiwvgjswvfc646yy6x0brph7pyt1vpqa&sfrom=search_job_pc&key=python&currentPage={0}&scene=page"
    start_urls = [baseURl.format(0)]

    def parse(self, response):
        selceter_list = response.xpath("//div[@class='job-list-item']")  # 返回选择器对象列表
        print("采集第%d页" % JobsidersSpider.page)
        for item in selceter_list:
            pipe_item = JobsbigdataItem()
            job_name = str(item.xpath("./div/div/div/a/div/div/div/text()").extract()[0])  # 使用xpath
            job_exp = str(item.xpath(".//div[@class='job-labels-box']/span/text()").extract()[0])
            job_degree = item.xpath(".//div[@class='job-labels-box']/span[2]/text()").extract()[0]
            print(job_degree)
            job_salary = str(item.xpath(".//div[@class='job-detail-header-box']/span[@class='job-salary']/text()").extract()[0])
            job_location = str(item.xpath(".//span[@class='ellipsis-1']/text()").extract()[0])
            job_corporate = item.xpath(".//span[@class='company-name ellipsis-1']/text()").extract()[0]
            job_link = item.xpath("./div/div/div/a/@href").extract()[0]
            try:
                job_type = item.xpath(".//div[@class='company-tags-box ellipsis-1']/span/text()").extract()[0]
            except Exception as e:
                print(e)
                job_type = "无"
            row = 'A' + str(JobsidersSpider.counter)

            JobsidersSpider.counter += 1
            job_recruiter = item.xpath(".//div[@class='recruiter-name ellipsis-1']/text()").extract()[0]
            job_salary_list = job_salary.split(sep='-', maxsplit=1)
            job_location_wide = job_location.split(sep='-', maxsplit=1)
            try:
                num1 = int(job_salary_list[0]) * 1000
                job_salary_low = str(num1)
                temp = job_salary_list[1].split(sep="·", maxsplit=1)
                num1 = int(temp[0].replace("k", "")) * 1000
                job_salary_high = str(num1)
                try:
                    if temp[1]:
                        job_salary_bounty = temp[1]
                except Exception as e:
                    job_salary_bounty = "None"
                    print(e)
            except Exception as e:
                job_salary_bounty = "面议"
                job_salary_high = "面议"
                job_salary_low = "面议"
            # data = [job_name, job_exp, job_degree, job_salary, job_salary_low, job_salary_high, job_salary_bounty, job_location, job_corporate, job_type, job_link]
            # f.write_row(row, data)

            pipe_item['job_name'] = job_name
            pipe_item['job_exp'] = job_exp
            pipe_item['job_salary_low'] = job_salary_low
            pipe_item['job_salary_high'] = job_salary_high
            pipe_item['job_salary_bounty'] = job_salary_bounty
            pipe_item['job_location'] = job_location_wide[0]
            pipe_item['job_corporate'] = job_corporate
            pipe_item['job_link'] = job_link
            pipe_item['job_type'] = job_type
            pipe_item['job_Recruiter'] = job_recruiter
            yield pipe_item

            pass
        JobsidersSpider.page += 1
        # if JobsidersSpider.page > 7:
            # workbook.close()
            # print("my job is done")
            # exit(0)
        print("-"*73+"第"+str(JobsidersSpider.page+1)+"页"+"-"*73)
        next_url = JobsidersSpider.baseURl.format(JobsidersSpider.page)
        yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
        pass

