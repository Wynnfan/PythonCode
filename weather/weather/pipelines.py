# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import json
import codecs
import pymysql


class WeatherPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()

        filename = base_dir + '/data/weather.txt'

        with open(filename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')

        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item

class W2json(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        with open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item

class W3mysql(object):
    def process_item(self, item, spider):
        date = item['date']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']
        img = item['img']

        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = '123456789',
            db = 'scrapydb',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO weather(date,week,img,temperature,weather,wind)
                        VALUES (%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql, (date,week,img,temperature,weather,wind))
            connection.commit()
        finally:
            connection.close()

        return item