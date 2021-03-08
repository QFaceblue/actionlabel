# actionlabel
使用pyqt编写的分类打标签软件，可以打包为exe
# 环境
python   
pyqt   
Qt Designer  
pyinstaller  
# 介绍
该程序实现对图片打标签，选择源文件夹和目标文件夹，点击开始打标签后，可以浏览图片对图片进行分类，可以查看打标签进度，实现上一张和下一张跳转，图片打标签和被存到对应的文件夹。
exe/文件夹存放已打包好的程序实例，可以直接运行  
imgs/文件夹存放图片
ui/文件夹存放ui文件，可以通过Qt Designer编辑  
# 运行
python action_label.py
# 打包
pyinstaller -F action_label.py  -w -i ./imgs/uestc.ico  
注意打包后，需将资源文件放到对应文件夹  

