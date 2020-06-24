import requests
from lxml import etree
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
}


def get_urls(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    urls = html.xpath("//div[@class='media media-16x9']/a/@href")
    return urls


def parse_urls(Url):
    response = requests.get(Url, headers=headers)
    html = response.text
    imgs = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    return imgs


if __name__ == '__main__':
    url = 'https://www.vmgirls.com/'
    uls = get_urls(url)
    images = []
    for ul in uls:
        image = parse_urls(ul)
        images.append(image)

for img_urls in images:
    for img_url in img_urls:
        fine_name = img_url.split('/')[-1]
        response = requests.get(img_url, headers=headers)
        with open(fine_name, 'wb')as f:
            f.write(response.content)

