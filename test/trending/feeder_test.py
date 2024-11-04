#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from pprint import pprint

from trending.feeder import generate_rss


def rss_feed_gen_test():
    # read trending data
    file_path = '20241104.json'
    json_list = __load_json_file(file_path)
    # pprint(json_list)

    # feed generator
    xml_rss = generate_rss(trending_list=json_list)

    __write_xml('rss.xml', xml_rss)


def __load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def __write_xml(file_path, file_content):
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(file_content)
        file.flush()


if __name__ == '__main__':
    rss_feed_gen_test()
