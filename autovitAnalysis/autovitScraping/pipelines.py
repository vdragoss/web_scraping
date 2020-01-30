# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class AutovitscrapingPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('autovit.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS autovit_db""")
        self.curr.execute("""create table autovit_db(
                            Make text,
                            Model text,
                            Version text,
                            Body_style text,
                            Year integer,
                            Mileage integer,
                            Engine_size text,
                            Fuel text,
                            Horsepower text,
                            Polution_standard text,
                            Transmission text,
                            Drivetrain text,
                            Condition text,
                            No_accident text,
                            Service_history text,
                            Registered_in_RO text,
                            Country_of_origin text,
                            Seller text,
                            Price integer,
                            Currency text,
                            Location text
                            )""")

    def store_db(self, item):
        self.curr.execute("""insert into autovit_db values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """,
                            (
                            item['make'][0],
                            item['model'][0],
                            item['version'][0],
                            item['body_style'][0],
                            item['year'][0],
                            item['km'][0],
                            item['engine_size'][0],
                            item['fuel'][0],
                            item['power'][0],
                            item['euro'][0],
                            item['transmission'][0],
                            item['drive'][0],
                            item['condition'][0],
                            item['no_accident'][0],
                            item['service_history'][0],
                            item['registered'][0],
                            item['country'][0],
                            item['seller'][0],
                            item['price'],
                            # item['link'][0], autovit_carinfo.start_urls
                            item['currency'],
                            item['location']
                            ))
        self.conn.commit()


    def process_item(self, item, spider):
        self.store_db(item)
        return item
