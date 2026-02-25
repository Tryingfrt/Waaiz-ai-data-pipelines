import requests
from bs4 import BeautifulSoup
import csv # This is Python's built-in spreadsheet maker

print("🚀 Initializing Live Web Scraper & Data Pipeline...\n")

target_url = "https://realpython.github.io/fake-jobs/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
}

try:
    print(f"📡 Connecting to: {target_url}...")
    response = requests.get(target_url, headers=headers)
    
    if response.status_code == 200:
        print("✅ Access Granted! Parsing the DOM...\n")
    else:
        print(f"❌ Access Denied. Status Code: {response.status_code}")
        exit()

    soup = BeautifulSoup(response.content, "html.parser")
    listings = soup.find_all("div", class_="card-content")
    
    # --- NEW: THE DATA STORAGE PIPELINE ---
    
    # 1. Create a new file called 'market_data.csv' and open it in 'Write' mode ('w')
    file = open('market_data.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    
    # 2. Write the Header Row (like the top row of an Excel sheet)
    writer.writerow(['Job Title', 'Company Name'])
    
    print("💾 Saving data to CSV spreadsheet...")

    # 3. Loop through EVERY listing on the page (not just 3 this time)
    for listing in listings:
        title = listing.find("h2", class_="title").text.strip()
        company = listing.find("h3", class_="company").text.strip()
        
        # Write the extracted data as a new row in the spreadsheet
        writer.writerow([title, company])

    # 4. Close the file so it saves properly
    file.close()

    print("🎉 Pipeline Complete! Open 'market_data.csv' in your project folder to see the results.")

except Exception as e:
    print(f"❌ Network Error: {e}")