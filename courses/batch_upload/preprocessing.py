import json
import os
from PIL import Image

# 定义一个遍历目录结构的函数
def traverse_dir(path):
  # 用于存储遍历结果的列表
  result = []
  
  # 列出当前目录中的所有文件和子目录
  items = os.listdir(path)

  count = 0

  # 遍历所有的项目
  for item in items:
    # 获取项目的完整路径
    full_path = os.path.join(path, item)

    # 判断项目是否为目录
    if os.path.isdir(full_path):
      # 如果是目录，则递归调用本函数
      result.append({item: traverse_dir(full_path)})
    else:
      # 如果是.png文件，则重命名为.PNG文件
      if item.endswith('.png'):
        os.rename(full_path, full_path[:-3] + 'PNG')

      # # 如果文件是.jpg或.JPG后缀名的图片，则转换为.png格式，删除原来的图片, print出来
      #   if item.endswith('.jpg') or item.endswith('.JPG'):
      #       print(count, full_path)
      #       count += 1
      #       # 转换为png格式
      #       im = Image.open(full_path)
      #       im.save(full_path[:-3] + 'png')
      #       # 删除原来的图片
      #       os.remove(full_path)
  

# 使用遍历函数遍历指定目录
SOURCE_DIR = 'e:/00自建站课程'
dir_tree = traverse_dir(SOURCE_DIR)
