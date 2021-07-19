import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://www.bnr.ro/files/xml/nbrfxrates2019.htm")
table = browser.find_element_by_xpath('//*[@id="Data_table"]')
table_text = table.text
list = table_text.split('\n')

header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
dictionar = {i: [] for i in header}

for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(list), len(header)):
        if '-' in list[i]:
            dictionar[header[int(j)]].append(list[i])
        else:
            dictionar[header[int(j)]].append(float(list[i]))

df = pd.DataFrame(dictionar)
df.to_csv("BNR_FROM_SELENIUM.xls")

print(table_text)

browser.close()