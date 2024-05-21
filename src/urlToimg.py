from data_parse import get_banner_img
import requests
import os

directory = "/Users/imgyuseong/PycharmProjects/myCmo_crawling/datas/imgs"
def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(directory, f"{file_name}.png")
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"이미지가 '{file_path}'에 저장되었습니다.")
    else:
        print("이미지를 다운로드하는 동안 오류가 발생했습니다.")

def save_img():
    for p in range(1, 15):
        img_url = get_banner_img(p)
        for url, title in img_url:
            download_image(url, title)

if __name__ == '__main__':
    save_img()
