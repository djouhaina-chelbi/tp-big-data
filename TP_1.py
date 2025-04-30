import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# قائمة لتخزين البيانات
datasets = []

# عدد الصفحات التي نريد استخراجها
num_pages = 100

for page in range(1, num_pages + 1):
    url = f"https://catalog.data.gov/dataset/?page={page}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"خطأ في تحميل الصفحة {page}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # البحث عن جميع العناصر التي تحتوي على البيانات
    items = soup.find_all('div', class_='dataset-content')

    for item in items:
        try:
            title = item.find('h3').text.strip()
            link = "https://catalog.data.gov" + item.find('h3').find('a')['href']
            
            datasets.append({
                "title": title,
                "link": link,
            })
        except Exception as e:
            print(f" خطأ في استخراج البيانات: {e}")
            continue

    print(f"تم استخراج بيانات الصفحة {page}")
    time.sleep(2)  # تأخير لتجنب الحظر

# حفظ البيانات في ملف CSV
df = pd.DataFrame(datasets)
df.to_csv("datasets_data_gov.csv", index=False, encoding='utf-8-sig')
df.to_csv("datasets_backup.csv", index=False, encoding='utf-8-sig')

print("تم حفظ البيانات في datasets_data_gov.csv و datasets_backup.csv")


