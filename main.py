from bs4 import BeautifulSoup
import urllib.request as req
import urllib
import os, re
import time
from urllib.parse import urljoin


def clean_html(html, strip=False):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(strip=strip)
    return text

url = "https://www.mhlw.go.jp/stf/shingi2/0000196043_00004.html"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
result = soup.select("a[href]")

link_list =[]
for link in result:
    if link and link.get("href").endswith('xlsx'):
        outfilename = f"{clean_html(str(link))}.xlsx"
        outdir = os.path.join(os.getcwd(), 'data', outfilename)
        href = link.get("href")
        print(f'url={url}')
        print(f'href={href}')
        fileurl = f'{url}{href}'
        # fileurl = url.join([url, str(href)])
        print(f'fileurl={fileurl}')
        print(outdir)
        urllib.request.urlretrieve(fileurl, outdir)
        time.sleep(2)
#
# xlsx_list = [temp for temp in link_list if temp.endswith('xlsx')]


# dbpdf_list = [temp for temp in pdf_list if '_db_' in temp]
#
# abs_dbpdf_list = []
# for relative in dbpdf_list:
#     temp_url = urljoin(url, relative)
#     abs_dbpdf_list.append(temp_url)
#
# filename_list = []
# for target in abs_dbpdf_list:
#     temp_list = target.split("/")
#     filename_list.append(temp_list[len(temp_list)-1])
#
# target_dir = "C:/Users/user/Desktop/dpc"
# savepath_list = []
# for filename in filename_list:
#     savepath_list.append(os.path.join(target_dir, filename))
#
# for (pdflink, savepath) in zip(abs_dbpdf_list, savepath_list):
#     urllib.request.urlretrieve(pdflink, savepath)
#     time.sleep(2)
