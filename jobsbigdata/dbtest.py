from jobsbigdata.dao.JobDao import JobDao
import matplotlib.pyplot as plt

jobdao = JobDao()
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
amx1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
amx2 = plt.subplot2grid((5, 5), (2, 2))
amx3 = plt.subplot2grid((3, 3), (2, 0), colspan=3)
city_list = jobdao.selectCity()
salary_avg = jobdao.get_avg_salary()
salary_avg_low = salary_avg[0]
salary_avg_high = salary_avg[1]
amx1.set_title("各城市薪资柱状折线图", fontsize=10)
amx1.bar(city_list, salary_avg_low)
amx1.set_xlabel("城市", fontsize=10)
amx1.set_ylabel("元/月", fontsize=10)
amx1.plot(city_list, salary_avg_high, "r", marker='*', ms=10, label="最高工资")
amx1.legend(loc="upper left")
for x, y in zip(city_list, salary_avg_high):
    amx1.text(x, y+1, str(y), ha='center', va='bottom', fontsize=7, rotation=0)
data, percent = jobdao.get_count_job_type()
label = data[0]
explode = [0, 0.1, 0.2]
amx2.set_title("各种语言工作岗位占比", fontsize=10)
amx2.pie(percent, labels=label, explode=explode, autopct='%1.1f%%')
amx3.bar(label, data[1])
amx3.set_xlabel("语言", fontsize=10)
amx3.set_ylabel("岗位数", fontsize=10)
amx3.set_title("各语言柱状图", fontsize=10)
for x, y in zip(label, data[1]):
    amx3.text(x, y+1, str(y), ha='center', va='bottom', fontsize=7, rotation=0)
plt.show()

