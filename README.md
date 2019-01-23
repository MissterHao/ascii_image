ascii-art
==============================
![image](https://img.shields.io/pypi/v/ascii_image.svg)
![image](https://img.shields.io/pypi/l/ascii_image.svg)
![image](https://img.shields.io/pypi/pyversions/ascii_image.svg)

將所有圖片轉換成 ASCII-art 形式的文字檔。  
Turn the image into ASCII-art format text file.

## Installation
To install , simply use pip of course):
安裝方法，只要使用 pip 安裝即可。
```{.sourceCode .bash}
$ pip install requests
```

## Usage
```python
import ascii_image
ascii_image.toASCII(imagePath, outFilePath, scale)
````
+ imagePath[str]: 欲轉換的圖片路徑 Image you want to change to ascii image
+ outFilePath[str]: 輸出檔案名稱 output file name
+ scale[tuple]: 輸入為兩個 int 正整數(Width, Height), 每個 ASCII 文字代表的像素(pixels)寬(Width)與高(Height)