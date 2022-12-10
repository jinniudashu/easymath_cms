import json
import os

# 从json文件中读取课程目录树，返回一个迭代器
def get_dir_tree():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dir_tree.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        dir_tree_list = json.load(f)

    return dir_tree_list

courses_index = iter(get_dir_tree())
