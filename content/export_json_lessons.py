import requests
import json

# API
url = "https://web-production-2275.up.railway.app/courses/lessons/"
res = requests.get(url)
lessons = res.json()

# 创建最终的lessons数组
final_lessons = []

# 循环所有视频课
for lesson in lessons:
    final_lessons.append({
        "id": lesson["id"],
        "title": lesson["title"],
        "description": lesson["description"],
        "position": lesson["position"],
        "video": lesson["video"],
        "video_additional": lesson["video_additional"],
        "thumbnail": lesson["thumbnail"],
        "thumbnail_name": lesson["thumbnail_name"],
        "is_free": lesson["is_free"],
        "course": lesson["course"],
        "unit": lesson["unit"]
    })

# 写入courses.json文件
with open("lessons.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(final_lessons, ensure_ascii=False, indent=4))


