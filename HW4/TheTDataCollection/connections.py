#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
connections.py - 从data.html文件中提取连接数据并写入connections.csv文件
"""

from bs4 import BeautifulSoup
import csv
import os

def extract_connections():
    """
    从data.html文件中提取连接数据
    
    Returns:
        list: 连接数据列表，每个连接包含From, To, Color, Minutes四个字段
    """
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 读取data.html文件
    html_path = os.path.join(script_dir, 'data.html')
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 找到第二个表格（Connections表格）
    connections_table = soup.find('h1', text='Connections').find_next('table')
    
    # 提取连接数据
    connections = []
    for row in connections_table.find_all('tr')[1:]:  # 跳过表头行
        columns = row.find_all('td')
        if len(columns) >= 5:  # 确保行有足够的列
            # 提取From, To, Color, Minutes四个字段
            from_station = columns[1].text.strip()
            to_station = columns[2].text.strip()
            color = columns[3].text.strip()
            minutes = columns[4].text.strip()
            
            connections.append({
                'From': from_station,
                'To': to_station,
                'Color': color,
                'Minutes': minutes
            })
    
    return connections

def write_to_csv(connections):
    """
    将连接数据写入connections.csv文件
    
    Args:
        connections (list): 连接数据列表
    """
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 写入connections.csv文件
    csv_path = os.path.join(script_dir, 'connections.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['From', 'To', 'Color', 'Minutes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # 写入数据
        for connection in connections:
            writer.writerow(connection)

def main():
    """
    主函数
    """
    # 提取连接数据
    connections = extract_connections()
    
    # 写入connections.csv文件
    write_to_csv(connections)
    
    print(f"成功提取 {len(connections)} 条连接数据并写入 connections.csv 文件")

if __name__ == "__main__":
    main()
