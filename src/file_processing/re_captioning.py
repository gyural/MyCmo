import os

directory = "/Users/imgyuseong/PycharmProjects/stable-diffusion/datas/imgs/train_imgs"

def rename_txt_files(directory):
    # 주어진 디렉토리의 모든 파일을 가져오기
    for idx, filename in enumerate(os.listdir(directory)):
        # 파일 확장자가 .png인 파일만 선택
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()

            # 첫 번째 라인 앞에 "ad" 추가
            if lines:
                lines[0] = 'ad ' + lines[0]

            # 변경된 내용을 다시 파일에 쓰기
            with open(file_path, 'w') as file:
                file.writelines(lines)

            print(f'Updated file: {file_path}')

if __name__ == '__main__':
    rename_txt_files(directory)