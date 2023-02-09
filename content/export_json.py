import requests
import json

# API1
url1 = "https://web-production-2275.up.railway.app/courses/"
res1 = requests.get(url1)
courses = res1.json()

# 创建最终的courses数组
final_courses = []

# 循环所有课程
for course in courses:

    print('Course: ', course["title"])
    # API3
    url3 = f"https://web-production-2275.up.railway.app/courses/{course['id']}/units/"
    res3 = requests.get(url3)
    units = res3.json()

    # 创建最终的units数组
    final_units = []

    # 循环所有单元
    for unit in units:
        # API4
        url4 = f"https://web-production-2275.up.railway.app/courses/{course['id']}/units/{unit['id']}/lessons/"
        res4 = requests.get(url4)
        unit_lessons = res4.json()

        # 创建单元的lessons数组
        final_unit_lessons = []

        # 循环所有视频课
        for lesson in unit_lessons:
            final_unit_lessons.append({
                "id": lesson["id"],
                "title": lesson["title"],
                "description": lesson["description"],
                "position": lesson["position"],
                "video": lesson["video"],
                "video_additional": lesson["video_additional"],
                "thumbnail": lesson["thumbnail"],
                "is_free": lesson["is_free"],
                "course": lesson["course"],
                "unit": lesson["unit"]
            })

        final_units.append({
            "id": unit["id"],
            "position": unit["position"],
            "title": unit["title"],
            "description": unit["description"],
            "course": unit["course"],
            "lessons": final_unit_lessons
        })

    final_courses.append({
        "id": course["id"],
        "slug": course["slug"],
        "title": course["title"],
        "description": course["description"],
        "thumbnail": course["thumbnail"],
        "units": final_units
    })

# 写入courses.json文件
with open("courses.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(final_courses, ensure_ascii=False, indent=4))
