import requests
import os

img_url_prefix = "https://res.cloudinary.com/dtysyyt3a/"

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

url = "https://web-production-2275.up.railway.app/courses/"

response = requests.get(url)

if response.status_code == 200:
    courses = response.json()
    for course in courses:
        title = course["title"]
        description = course["title"]
        thumbnail = img_url_prefix + course["thumbnail"]
        slug = course_slugs[title]
        course["image"] = {
        "src": thumbnail,
        "alt": title,
        }
        course.pop("id", None)
        course.pop("slug", None)
        with open(f"course/{slug}.md", "w", encoding="utf-8") as file:
            file.write(f"---\ntitle: {title}\ndescription: {description}\nthumbnail: {thumbnail}\nimage: {{\n src: "{course['image']['src']}",\n alt: "{course['image']['alt']}"\n}}\n---")
    else:
        print("Failed to fetch data from the API")




