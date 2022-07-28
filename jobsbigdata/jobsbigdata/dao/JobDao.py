from jobsbigdata.dao.BaseDao import BaseDao


class JobDao(BaseDao):

    def creatJobData(self, sql, params):
        res = self.execute(sql, params)
        self.commit()
        return res

    def selectCity(self):
        res = self.execute("select jobAddress from t_jobdata group by jobAddress order by jobSalaryLow")
        city = self.fetchall()
        city_list = list()
        for per_list in city:
            for key, value in per_list.items():
                city_list.append(value)
            pass
        return city_list

    def get_avg_salary(self):
        salary_list = [[], []]
        city_list = self.selectCity()
        for per_list in city_list:
            sql = 'SELECT AVG(jobSalaryLow),AVG(jobSalaryHigh) FROM t_jobdata where jobAddress="{}"'
            sql = sql.format(per_list)
            res = self.execute(sql)
            salary = self.fetchall()
            for item in salary:
                lst = list(item.values())
                salary_list[0].append((round(lst[0], 0)))
                salary_list[1].append((round(lst[1], 0)))
        return salary_list

    def get_count_job_type(self):
        job_type = [["c++", "python", "java"], ["0", "0", "0"], ["0", "0", "0"]]
        i = 0
        for types in job_type[0]:
            sql = "SELECT count(*),avg(jobSalaryLow) FROM t_jobdata WHERE jobName LIKE %s;"
            params = ['%' + types + '%']
            res = self.execute(sql, params)
            count_type = self.fetchall()
            for item in count_type:
                lst = list(item.values())
                job_type[1][i] = lst[0]
                job_type[2][i] = str(round(lst[1], 0))
            i += 1
        sum_type = float(job_type[1][0]) + float(job_type[1][1]) + float(job_type[1][2])
        lst = list()
        lst.append(round(float(job_type[1][0]) / sum_type * 100, 2))
        lst.append(round(float(job_type[1][1]) / sum_type * 100, 2))
        lst.append(round(float(job_type[1][2]) / sum_type * 100, 2))
        return job_type, lst





