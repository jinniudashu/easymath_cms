# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

import environ
env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

# Set configuration parameter: return "https" URLs by setting secure=True  
# 配置Cloudinary
config = cloudinary.config(
    cloud_name=env('CLOUDINARY_CLOUD_NAME'),
    api_key=env('CLOUDINARY_API_KEY'),
    api_secret=env('CLOUDINARY_API_SECRET'),
    secure=True
)


# Log the configuration
# ==============================
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")


uploaded_image = cloudinary.uploader.upload("test.jpg", public_id="test", folder="easymath", unique_filename = False, overwrite=True)

# 上传完成后，upload()方法会返回上传文件的详细信息，
# 包括文件名、文件类型、URL等。例如：
print(uploaded_image["public_id"])  # 文件名
print(uploaded_image["format"])     # 文件类型
print(uploaded_image["url"])        # 文件URL

def uploadImage():

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  cloudinary.uploader.upload("https://cloudinary-devs.github.io/cld-docs-assets/assets/images/butterfly.jpeg", public_id="quickstart_butterfly", unique_filename = False, overwrite=True)

  # Build the URL for the image and save it in the variable 'srcURL'
  srcURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url()

  # Log the image URL to the console. 
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")