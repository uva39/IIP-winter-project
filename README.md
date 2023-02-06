# IIP winter project - 김재상

temp 안의 "TagCrawling.py"와 "PrettierTag.ipynb"는 태그 목록(data.csv)을 크롤링하기 위해 한 번만 사용된 코드입니다.  

마땅히 사용할 태그 목록이 없는 경우엔, **TagCrawling.py**를 한 번 실행한 뒤, **PrettierTag.ipynb**를 실행하여 TagList.csv 파일을 생성해준 다음, **GenerateImage.ipynb**파일을 통해 이미지를 생성합니다.  

**GenerateImage.ipynb**에서는 **webui-user.Ink** 형태의 윈도우 바로가기 파일을 요구합니다. https://rentry.org/voldy 에서 이미지 제너레이터 GUI와 nai.ckpt를 다운로드 받은 뒤, **webui-user.bat** 파일의 바로가기 파일인 **webui-user.Ink**을 파일 위치를 맞춰서 새로 만들어주면 됩니다.  