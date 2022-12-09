import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定义一个遍历目录结构的函数
def traverse_dir(path):
  # 用于存储遍历结果的列表
  result = []
  
  # 列出当前目录中的所有文件和子目录
  items = os.listdir(path)
  
  # 遍历所有的项目
  for item in items:
    # 获取项目的完整路径
    full_path = os.path.join(path, item)
    # 判断项目是否为目录
    if os.path.isdir(full_path):
      # 如果是目录，则递归调用本函数
      result.append({item: traverse_dir(full_path)})
    else:
      # 如果不是目录，则将项目的完整路径添加到结果列表中
      file_name = os.path.basename(full_path)
      result.append(file_name)
  
  # 返回遍历结果
  return result

# 使用遍历函数遍历指定目录
dir_tree = traverse_dir(BASE_DIR)

# 将遍历结果转换为 JSON 格式并写入文件
with open('dir_tree.json', 'w') as f:
  json.dump(dir_tree, f)
