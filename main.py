#!/usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
from datetime import datetime

from trending.crawler import github_trending_crawler
from trending.feeder import generate_rss


def trending_daily_scheduler():
    # fetch data
    trending_list = asyncio.run(github_trending_crawler(verbose=True))
    trending_rss = generate_rss(trending_list=trending_list)

    # params
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y%m%d')

    # save rss
    save_path = f'./data/{formatted_date}-trending.xml'
    with open(save_path, 'w+', encoding='utf-8') as file:
        file.write(trending_rss)
        file.flush()

    pass


if __name__ == '__main__':
    trending_daily_scheduler()
