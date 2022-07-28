##基于scarpy的爬虫，使用了伪造请求头防止IP被封
>每10秒下载一次数据，如修改于settings.py的DOWNLOAD_DELAY下修改

##需要以下库
>xlsxwriter scrapy matplotlib pymysql

#数据库配置存储于mysql.json
>务必自行配置

##本项目以爬取猎聘网作为样例
>使用pipepipelines对爬到的数据进行封装，从而写入到数据库中
> 
>也可以在jobsiders.py中直接将数据写入到excel中
> 
>爬虫运行run.py开始运行
> 
>修改jobsiders.py中的URL修改网页，修改xpath来修改截取的元素
