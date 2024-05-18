import os

def rename_png_files(directory):
    # 주어진 디렉토리의 모든 파일을 가져오기
    for idx, filename in enumerate(os.listdir(directory)):
        # 파일 확장자가 .png인 파일만 선택
        if filename.endswith('.png'):
            # 새로운 파일명 생성
            new_name = f'ad{idx}' + '.png'
            # 기존 파일의 전체 경로
            old_file_path = os.path.join(directory, filename)
            # 새로운 파일의 전체 경로
            new_file_path = os.path.join(directory, new_name)
            # 파일명 변경
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} to {new_file_path}')

# 실행할 디렉토리 경로
dir_path = "/Users/imgyuseong/PycharmProjects/stable-diffusion/datas/imgs"
if __name__ == "__main__":
    rename_png_files(dir_path)