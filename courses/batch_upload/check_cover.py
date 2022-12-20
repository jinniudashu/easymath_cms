import json
import os


# 从json文件中读取课程目录树，返回一个迭代器
def get_dir_tree():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dir_tree.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        dir_tree_list = json.load(f)

    return dir_tree_list

# 上传课程目录树中的所有文件
def batch_upload():

  SOURCE_DIR = 'e:/00自建站课程'
  courses_index = iter(get_dir_tree())

  for course in courses_index:
    # 获取course的键名和键值
    course_name, units = course.popitem()
    print(course_name)

    for unit in units:
      # 判断item类型是dict还是str
      if isinstance(unit, dict):
        unit_name, videos = unit.popitem()

        for video in videos:
          if isinstance(video, str):
            path = f'{SOURCE_DIR}/{course_name}/{unit_name}/{video}'
            if video[-4:] == '.mp4':
              # 尝试打开同名的封面图片文件（.png 或 .PNG）, 如果失败则写入一个日志文件
              try:
                cover_path = f'{SOURCE_DIR}/{course_name}/{unit_name}/{video[:-4]}.PNG'
                cover = open(cover_path, 'rb')
              except FileNotFoundError:
                with open('missing_cover.txt', 'w', encoding='utf-8') as f:
                    print('封面不存在:', path)
                    f.write(path+'\n')
                    
                continue

batch_upload()

# 封面不存在: e:/00自建站课程/应用题课/1~3年级/先导课地球同盟军大作战：寻找丢失的数学记忆.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/01露营计划.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/02飞机遇险.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/05海鲜大餐.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/06荒岛第一夜.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/07搭建树屋.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/08岛上游戏.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/09解密漂流瓶.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/10储备淡水.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/11深入探索.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/12发现古船残骸.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/13建造方舟.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/14令人头疼的帆船.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/15启航.mp4
# 封面不存在: e:/00自建站课程/应用题课/4~6年级/荒岛历险记先导片.mp4