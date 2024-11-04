#!/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
import json
import os
from datetime import datetime

from trending.crawler import github_trending_crawler
from trending.feeder import generate_rss


def trending_daily_scheduler():
    # params
    current_date = datetime.now()
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    today = current_date.strftime('%Y%m%d')

    # create folder
    save_folder = os.path.join('.', 'data', year, month)
    os.makedirs(save_folder, exist_ok=True)

    # fetch data
    trending_list = asyncio.run(github_trending_crawler(verbose=True))
    trending_rss = generate_rss(trending_list=trending_list)

    # save rss
    rss_save_path = os.path.join(save_folder, f'{today}-trending.xml')
    with open(rss_save_path, 'w', encoding='utf-8') as file:
        file.write(trending_rss)

    # save json
    json_save_path = os.path.join(save_folder, f'{today}-trending.json')
    with open(json_save_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(trending_list, ensure_ascii=False))

    pass


if __name__ == '__main__':
    trending_daily_scheduler()
