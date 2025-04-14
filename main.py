from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# ✅ Path to ChromeDriver
chromedriver_path = r"C:\Users\saket\OneDrive\Desktop\PORTFOLIO WEBSITE\chromedriver.exe"

# ✅ Your Chrome user data and profile directory
chrome_user_data_dir = r"C:\Users\saket\AppData\Local\Google\Chrome\User Data"
profile_directory = "Profile 2"  # Change if needed

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
options.add_argument(f"--profile-directory={profile_directory}")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--new-window")  # 🆕 Ensures it opens in a new window
options.add_experimental_option("detach", True)
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# ❌ Do NOT use remote debugging port (removes attachment behavior)
# options.add_argument("--remote-debugging-port=9222")

# Launch Chrome fresh (new window)
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# Go to the course
driver.get("https://prepinstaprime.com/course/java")

# Wait for manual login
input("🔐 Please log in manually, then press Enter to continue...")

# Find all clickable videos
video_elements = driver.find_elements(By.CSS_SELECTOR, "h5[style*='cursor: pointer']")

print(f"🎥 Found {len(video_elements)} video elements.")

for index, video in enumerate(video_elements, start=1):
    try:
        print(f"\n▶️ Playing Video {index}: {video.text}")
        driver.execute_script("arguments[0].click();", video)
        time.sleep(3)

        # Handle iframe
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Click the YouTube button
        youtube_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Watch on YouTube']")
        youtube_button.click()

        driver.switch_to.default_content()
        time.sleep(5)

    except Exception as e:
        print(f"❌ Failed on video {index}: {e}")
        driver.switch_to.default_content()

print("\n✅ Done!")
