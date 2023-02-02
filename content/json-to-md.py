# Description: This script converts the JSON data from the API to Markdown files
# 把视频课数据从 API 转换成 Markdown 文件，按照系列课、单元、课程的顺序存放
# 为系列课生成了slug，用于系列课的目录

import os
import requests
import json

baseurl = "https://res.cloudinary.com/dtysyyt3a/"
course_slugs = {
    "1年级上": "grade-1-semester-1",
    "1年级下": "grade-1-semester-2",
    "2年级上": "grade-2-semester-1",
    "2年级下": "grade-2-semester-2",
    "3年级上": "grade-3-semester-1",
    "3年级下": "grade-3-semester-2",
    "4年级上": "grade-4-semester-1",
    "4年级下": "grade-4-semester-2",
    "5年级上": "grade-5-semester-1",
    "5年级下": "grade-5-semester-2",
    "6年级上": "grade-6-semester-1",
    "6年级下": "grade-6-semester-2",
}

# 1. Call API to get JSON array
url = "https://web-production-2275.up.railway.app/courses/"
response = requests.get(url)
courses = response.json()

# 2. Iterate through the array and convert each object element to a Markdown file
for course in courses:
    title = course.get("title")
    course_slug = course_slugs[title]
    if not os.path.exists(course_slug):
        os.mkdir(course_slug)

    url = f"https://web-production-2275.up.railway.app/courses/{course['id']}/units/"
    units = requests.get(url).json()
    for unit in units:
        unit_position = str(unit.get("position"))
        unit_title = unit.get("title")
        unit_name = f"{course_slug}/{unit_position}-{unit_title}"
        if not os.path.exists(unit_name):
            os.mkdir(unit_name)

        url = f"https://web-production-2275.up.railway.app/courses/{course['id']}/units/{unit['id']}/lessons/"
        lessons = requests.get(url).json()
        for lesson in lessons:
            if lesson.get('description') is None:
                lesson['description'] = lesson['title']

            if lesson.get('thumbnail') is None:
                lesson['thumbnail'] = ""
                print(f"Thumbnail not found for {lesson.get('title')}")
            else:
                lesson['thumbnail'] = baseurl + lesson['thumbnail']

            if lesson.get('video') is None:
                lesson['video'] = ""
                print(f"Video not found for {lesson.get('title')}")
            else:
                lesson['video'] = baseurl + lesson['video']

            if lesson.get('video_additional') is None:
                lesson['video_additional'] = ""
            else:
                lesson['video_additional'] = baseurl + lesson['video_additional']

            # Remove id and slug fields
            del lesson["id"]
            del lesson["slug"]
            del lesson["course"]
            del lesson["unit"]
            
            # Write the course data as front matter in a Markdown file
            with open(f"{unit_name}/{lesson.get('title')}.md", "w", encoding="utf-8") as file:
                file.write("---\n")
                for key in lesson:
                    file.write(f"{key}: {lesson[key]}\n")
                file.write("---\n")
