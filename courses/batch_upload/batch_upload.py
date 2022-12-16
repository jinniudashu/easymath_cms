import json
import os

import cloudinary.uploader
import cloudinary.api

from courses.models import Course, Unit, Lesson, Exercises


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

    # 保存课程
    course = Course.objects.create(title=course_name)

    for unit in units:
      # 判断item类型是dict还是str
      if isinstance(unit, dict):
        unit_name, videos = unit.popitem()

        title=unit_name[4:]
        position=int(unit_name[0:2])

        # 打印键名
        print(position, '单元', title)

        # 保存单元
        unit = Unit.objects.create(title=title, position=position, course=course)

        for video in videos:
          if isinstance(video, str):
            path = f'{SOURCE_DIR}/{course_name}/{unit_name}/{video}'
            if video[-4:] == '.mp4':
              print('视频', path)

              title=video[3:-4]
              position=int(video[1:3])

              # 保存视频
              lesson = Lesson.objects.create(title=title, position=position, unit=unit, course=course)

              # 上传视频
              uploaded_video = cloudinary.uploader.upload(path, public_id=title, folder=f'easymath/{course_name}/{unit_name}', unique_filename = True, overwrite=True, resource_type="video")

              # 保存视频URL
              lesson.video = uploaded_video['url']
              lesson.save()

            else:
              # 上传封面图片
              print('封面', path)
              lesson = Lesson.objects.get(title=video[3:-4])
              uploaded_image = cloudinary.uploader.upload(path, public_id=title, folder=f'easymath/{course_name}/{unit_name}', unique_filename = True, overwrite=True)

              # 保存封面URL
              lesson.thumbnail = uploaded_image['url']
              lesson.save()

          elif isinstance(video, dict):
            print('解答视频', video)
            _name, videos_additional = video.popitem()
            path = f'{SOURCE_DIR}/{course_name}/{unit_name}/{_name}'
            for video_additional in videos_additional:
                position = int(video_additional[1:3])
                lesson = Lesson.objects.get(position=position, unit=unit, course=course)

                # 上传视频
                uploaded_video = cloudinary.uploader.upload(f'{path}/{video_additional}', folder=f'easymath/{course_name}/{unit_name}/{_name}', unique_filename = True, overwrite=True, resource_type="video")
                
                # 保存视频URL
                lesson.video_additional = uploaded_video['url']
                lesson.save()

      else:
        # 构造目录位置
        path = f'{SOURCE_DIR}/{course_name}/{unit}'
        print('封面', path)

        # 上传封面图片
        uploaded_image = cloudinary.uploader.upload(path, public_id=course_name, folder=f'easymath/{course_name}', unique_filename = True, overwrite=True)

        # 保存封面URL
        course.thumbnail = uploaded_image['url']
        course.save()



#   # Upload the image.
#   # Set the asset's public ID and allow overwriting the asset with new versions
#   cloudinary.uploader.upload("https://cloudinary-devs.github.io/cld-docs-assets/assets/images/butterfly.jpeg", public_id="quickstart_butterfly", unique_filename = False, overwrite=True)

#   # Build the URL for the image and save it in the variable 'srcURL'
#   srcURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url()


# ****************************************************************************************************
# 待处理视频文件
# ****************************************************************************************************
# 文件过大，跳过： 204M e:/00自建站课程\应用题课\1~3年级\01 寻找同盟军.mp4
# 文件过大，跳过： 260M e:/00自建站课程\应用题课\1~3年级\02 面包够吗？.mp4
# 文件过大，跳过： 292M e:/00自建站课程\应用题课\1~3年级\03 外星人的计划 .mp4
# 文件过大，跳过： 315M e:/00自建站课程\应用题课\1~3年级\04 走哪条路呢？.mp4
# 文件过大，跳过： 315M e:/00自建站课程\应用题课\1~3年级\05 潜入基地.mp4
# 文件过大，跳过： 342M e:/00自建站课程\应用题课\1~3年级\06 挖掘地下通道 .mp4
# 文件过大，跳过： 367M e:/00自建站课程\应用题课\1~3年级\07 爸爸妈妈在哪里？.mp4
# 文件过大，跳过： 365M e:/00自建站课程\应用题课\1~3年级\08 安放干扰器.mp4
# 文件过大，跳过： 291M e:/00自建站课程\应用题课\1~3年级\09 兵分三路.mp4
# 文件过大，跳过： 381M e:/00自建站课程\应用题课\1~3年级\10 找回数学记忆 .mp4
# 文件过大，跳过： 296M e:/00自建站课程\应用题课\1~3年级\11通关测试卷一.mp4
# 文件过大，跳过： 349M e:/00自建站课程\应用题课\1~3年级\12通关测试卷二.mp4
# 文件过大，跳过： 195M e:/00自建站课程\应用题课\4~6年级\03 迫降荒岛 .mp4
# 文件过大，跳过： 292M e:/00自建站课程\应用题课\4~6年级\04寻找食物.mp4
# 文件过大，跳过： 284M e:/00自建站课程\计算课\小数和分数篇\01小数加法入门——小数加小数.mp4
# 文件过大，跳过： 175M e:/00自建站课程\计算课\小数和分数篇\02明确“数位对齐”，掌握整数加小数.mp4
# 文件过大，跳过： 113M e:/00自建站课程\计算课\小数和分数篇\03方法迁移，进行小数减小数.mp4
# 文件过大，跳过： 204M e:/00自建站课程\计算课\小数和分数篇\04巧用“添0”法，完成整数减小数.mp4
# 文件过大，跳过： 382M e:/00自建站课程\计算课\小数和分数篇\05运用整数加减法运算定律进行小数加减法的简便计算.mp4
# 文件过大，跳过： 244M e:/00自建站课程\计算课\小数和分数篇\06运用“转化”思想完成整数乘小数.mp4
# 文件过大，跳过： 374M e:/00自建站课程\计算课\小数和分数篇\07应用积的变化规律进行小数乘小数.mp4
# 文件过大，跳过： 328M e:/00自建站课程\计算课\小数和分数篇\08小数除法入门——小数除以整数.mp4
# 文件过大，跳过： 396M e:/00自建站课程\计算课\小数和分数篇\09巧移小数点完成小数除以小数.mp4
# 文件过大，跳过： 404M e:/00自建站课程\计算课\小数和分数篇\10探究“秘密数”掌握小数乘除法的简便计算.mp4
# 文件过大，跳过： 350M e:/00自建站课程\计算课\小数和分数篇\11分数加减法入门——同分母分数加减法.mp4
# 文件过大，跳过： 432M e:/00自建站课程\计算课\小数和分数篇\12掌握“通分”技巧，进行异分母分数加减法.mp4
# 文件过大，跳过： 319M e:/00自建站课程\计算课\小数和分数篇\13运算能力升级——分数加减法的简便计算.mp4
# 文件过大，跳过： 166M e:/00自建站课程\计算课\小数和分数篇\14巧用“约分”进行分数乘整数.mp4
# 文件过大，跳过： 131M e:/00自建站课程\计算课\小数和分数篇\15运用“数形结合”思想，解析分数乘分数.mp4
# 文件过大，跳过： 169M e:/00自建站课程\计算课\小数和分数篇\16灵活“互化”解决分数乘小数.mp4
# 文件过大，跳过： 230M e:/00自建站课程\计算课\小数和分数篇\17认识“倒数”完成分数除以整数.mp4
# 文件过大，跳过： 351M e:/00自建站课程\计算课\小数和分数篇\18分数除法进阶——分数除以分数.mp4
# 文件过大，跳过： 431M e:/00自建站课程\计算课\小数和分数篇\19运算能力升级——分数乘除法的简便计算.mp4
# 文件过大，跳过： 226M e:/00自建站课程\计算课\小数和分数篇\20解方程的基础入门——等式的基本性质.mp4
# 文件过大，跳过： 398M e:/00自建站课程\计算课\小数和分数篇\21解方程的基本方法——剥洋葱大法.mp4
# 文件过大，跳过： 328M e:/00自建站课程\计算课\小数和分数篇\22解方程的进阶探究——特殊情况的解方程.mp4
# 文件过大，跳过： 314M e:/00自建站课程\计算课\小数和分数篇\23解方程的能力升级——解方程的灵活变式.mp4
# 文件过大，跳过： 180M e:/00自建站课程\计算课\自然数篇\01加法计算基础入门——不进位加法.mp4
# 文件过大，跳过： 254M e:/00自建站课程\计算课\自然数篇\02“凑十法“解决20以内进位加.mp4
# 文件过大，跳过： 192M e:/00自建站课程\计算课\自然数篇\03善用”进位一“进行多位数进位加法.mp4
# 文件过大，跳过： 100M e:/00自建站课程\计算课\自然数篇\04减法计算入门——不退位减法.mp4
# 文件过大，跳过： 157M e:/00自建站课程\计算课\自然数篇\05“破十法”解决20以内退位减.mp4
# 文件过大，跳过： 136M e:/00自建站课程\计算课\自然数篇\06巧用“退位点”准确进行连续退位减.mp4
# 文件过大，跳过： 171M e:/00自建站课程\计算课\自然数篇\07题型大揭秘——减法中千变万化的0.mp4
# 文件过大，跳过： 428M e:/00自建站课程\计算课\自然数篇\08计算法则升级——加减法的简便运算.mp4
# 文件过大，跳过： 254M e:/00自建站课程\计算课\自然数篇\09搞定乘法基础，巧记乘法口诀.mp4
# 文件过大，跳过： 337M e:/00自建站课程\计算课\自然数篇\10乘法计算初体验——两位数乘一位数.mp4
# 文件过大，跳过： 309M e:/00自建站课程\计算课\自然数篇\11乘法计算进阶——三位数乘两位数.mp4
# 文件过大，跳过： 357M e:/00自建站课程\计算课\自然数篇\12探究乘法中的特权数“0”.mp4
# 文件过大，跳过： 227M e:/00自建站课程\计算课\自然数篇\13理解“平均分”，搞定除法基础.mp4
# 文件过大，跳过： 314M e:/00自建站课程\计算课\自然数篇\14学习除法竖式算理算法，掌握除数是一位数的除法.mp4
# 文件过大，跳过： 380M e:/00自建站课程\计算课\自然数篇\15善用“试商调商”思维，掌握除数是两位数的除法.mp4
# 文件过大，跳过： 358M e:/00自建站课程\计算课\自然数篇\16运算能力升级——乘除法的简便计算.mp4