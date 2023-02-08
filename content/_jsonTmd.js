import axios from 'axios';
import fs from 'fs';

const imgUrlPrefix = "https://res.cloudinary.com/dtysyyt3a/"

const course_slugs = {
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

// 1. Call API to get JSON array
const url = "https://web-production-2275.up.railway.app/courses/";

axios.get(url)
  .then(response => {
    const courses = response.data;
    // 2. Iterate through the array and convert each object element to a Markdown file
    courses.forEach(course => {
      const title = course.title;
      const description = course.title;
      const thumbnail = imgUrlPrefix + course.thumbnail;
      const slug = course_slugs[title];
      // Add image field based on thumbnail field
      course.image = {
        src: thumbnail,
        alt: title,
      };
      // Remove id and slug fields
      delete course.id;
      delete course.slug;
      // Write the course data as front matter in a Markdown file in the course directory
      fs.writeFile(`course/${slug}.md`, `---\ntitle: ${title}\ndescription: ${description}\nthumbnail: ${thumbnail}\nimage: {\n  src: "${course.image.src}",\n  alt: "${course.image.alt}"\n}\n---`, (err) => {
        if (err) throw err;
      });
    });
  })
  .catch(error => {
    console.error(error);
  });
