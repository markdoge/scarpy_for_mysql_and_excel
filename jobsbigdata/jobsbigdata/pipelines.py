# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from jobsbigdata.dao.JobDao import JobDao


class JobsbigdataPipeline:
    def process_item(self, item, spider):
        sql = "insert into t_jobdata" \
              "(jobName, jobEXP, jobAddress, jobCompany, jobRecruiter, jobLink, jobType, jobSalaryLow, jobSalaryHigh, jobSalaryBounty) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = [item['job_name'], item['job_exp'], item['job_location'], item['job_corporate'], item['job_Recruiter'],
                  item['job_link'], item['job_type'], item['job_salary_low'], item['job_salary_high'], item['job_salary_bounty']]
        try:
            jobdao = JobDao()
            res = jobdao.creatJobData(sql, params)
            if res > 0:
                print("写入成功")
        except Exception as e:
            print(e)
        finally:
            jobdao.close()
        return item
