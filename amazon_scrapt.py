import requests
import re
from time import sleep
import urllib.request
from selenium import webdriver

####################  Get Setting ###################################
import json
with open('Setting_InventoryManager.json', 'r', encoding='utf-8') as f:
    Data_dict = json.load(f)[0]
    ProductImages_path = Data_dict['ProductImages_path']

####################  Class Amazon scrapt ###########################
class AmazonScrapt():
    def __init__(self, asin):
        self.asin = asin
        self.url = 'https://www.amazon.co.jp/dp/%s/' % self.asin
        self.html = self.request()
        # self.html = self.request_selenium()
        # self.html = self.open_html()

    # Get html using request, may be block by Amazon
    def request(self):
        html = requests.get(self.url).text
        return html
      
    # Get html using chrome
    def request_selenium(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        # sleep(5)
        html = driver.page_source
        driver.quit()
        return html

    # Get html by open file
    def open_html(self):
        with open('test.html', encoding='utf-8') as f:
            html = f.read()
            return html

    def scrapt_fist_image_url(self):
        try:
            fist_images = re.search(r'data-old-hires="https://.*?.jpg', self.html).group(0)
            fist_images = fist_images.replace('data-old-hires="', '')
        except:
            print('Can not get the fist image url.')
        return fist_images

    def scrapt_all_image_urls(self):
        all_images = []

        try:
            # HTML by request
            new_html = self.html.replace('\n', '')
            child_html = re.findall(r'ImageBlockATF.*?AboveTheFold', new_html)[0]
        except:
            try:
                # If block by Amazon => Get html by Chrome
                self.html = self.request_selenium()
                new_html = self.html.replace('\n', '')
                child_html = re.findall(r'ImageBlockATF.*?AboveTheFold', new_html)[0]
            except:
                print('HTML not found')

        images_link = re.findall(r'"hiRes":".*?jpg', child_html)
        for url in images_link:
            url = re.search(r'https.*?jpg', url).group(0)
            all_images.append(url)

        return all_images

    def dowload_fist_image(self):
        try:
            url = self.scrapt_all_image_urls()[0]
            save_path = ProductImages_path + '/' + self.asin + '.jpg'
            urllib.request.urlretrieve(url, save_path)
        except:
            return {'error': 'Picture not found'}
        
        
#################################################
if __name__ == '__main__':
    pass
    # AmazonScrapt = AmazonScrapt(asin='B07PFFMQ64')
    # AmazonScrapt.dowload_fist_image()





