#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
stations.py - 从data.html文件中提取站点名称列表并写入stations.csv文件
"""

from bs4 import BeautifulSoup
import csv
import os

def extract_stations():
    """
    从data.html文件中提取站点名称列表
    
    Returns:
        list: 站点名称列表
    """
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 读取data.html文件
    html_path = os.path.join(script_dir, 'data.html')
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 找到第一个表格（Stations表格）
    stations_table = soup.find('h1', text='Stations').find_next('table')
    
    # 提取站点名称列表
    stations = []
    for row in stations_table.find_all('tr')[1:]:  # 跳过表头行
        columns = row.find_all('td')
        if len(columns) >= 2:  # 确保行有足够的列
            station_name = columns[1].text.strip()  # 第二列是站点名称
            stations.append(station_name)
    
    return stations

def write_to_csv(stations):
    """
    将站点名称列表写入stations.csv文件
    
    Args:
        stations (list): 站点名称列表
    """
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 写入stations.csv文件
    csv_path = os.path.join(script_dir, 'stations.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for station in stations:
            writer.writerow([station])  # 每行一个站点名称

def main():
    """
    主函数
    """
    # 提取站点名称列表
    stations = extract_stations()
    
    # 写入stations.csv文件
    write_to_csv(stations)
    
    print(f"成功提取 {len(stations)} 个站点名称并写入 stations.csv 文件")

if __name__ == "__main__":
    main()
