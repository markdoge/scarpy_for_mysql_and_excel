import pymysql
import json
import os


class BaseDao:

    def __init__(self, config="D:\python\jobsbigdata\mysql.json"):
        self.__config = json.load(open(config, mode="r", encoding="utf-8"))
        self.__conn = None
        self.__cursor = None
        pass

    def get_connection(self):
        if self.__conn:
            return  self.__conn
        else:
            self.__conn = pymysql.connect(**self.__config)
            return self.__conn
        pass

    def execute(self, sql, params=[], ret="dict"):
        try:
            self.__conn = self.get_connection()
            if ret == "dict":
                self.__cursor = self.__conn.cursor(pymysql.cursors.DictCursor)
            else:
                self.__cursor = self.__conn.cursor()
            res = self.__cursor.execute(sql, params)
        except pymysql.DatabaseError as e:
            print("sql error")
        return res

    def fetchall(self):
        if self.__cursor:
            return self.__cursor.fetchall()
        else:
            # print("nothing is selected!")
            return None
        pass

    def close(self):
        if self.__cursor:
            self.__cursor.close()
            pass

        if self.__conn:
            self.__conn.close()
            pass
        pass

    def commit(self):
        if self.__conn:
            self.__conn.commit()
            pass
        pass

    def rollback(self):
        if self.__conn:
            self.__conn.rollback()
            pass
        pass


