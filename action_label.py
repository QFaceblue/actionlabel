from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QMessageBox
import os
import shutil

# pyinstaller -F action_label.py  -w -i ./imgs/uestc.ico

class actionLabel(QWidget):

    def __init__(self):
        super().__init__()
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("./ui/actionLabel.ui")
        self.img_path = "./imgs/uestc.jpg"
        self.img = QPixmap(self.img_path).scaled(960, 540)
        self.ui.img_label.setPixmap(self.img)

        self.list = []
        self.total = 0
        self.labels = []
        self.new_list = []
        self.index = 0

        self.source_dir = ""
        self.dest_dir = ""

        # 绑定函数
        self.ui.source_btn.clicked.connect(lambda: self.choose_source())
        self.ui.dest_btn.clicked.connect(lambda: self.choose_dest())

        self.ui.last_btn.clicked.connect(lambda: self.last())
        self.ui.next_btn.clicked.connect(lambda: self.next())

        self.ui.start_btn.clicked.connect(lambda: self.start())

        self.ui.label_0.clicked.connect(lambda: self.label(0))
        self.ui.label_1.clicked.connect(lambda: self.label(1))
        self.ui.label_2.clicked.connect(lambda: self.label(2))
        self.ui.label_3.clicked.connect(lambda: self.label(3))
        self.ui.label_4.clicked.connect(lambda: self.label(4))
        self.ui.label_5.clicked.connect(lambda: self.label(5))
        self.ui.label_6.clicked.connect(lambda: self.label(6))
        self.ui.label_7.clicked.connect(lambda: self.label(7))
        self.ui.label_8.clicked.connect(lambda: self.label(8))

        self.ui.delete_btn.clicked.connect(lambda: self.delete())

        # 设置按钮不可用
        self.ui.last_btn.setEnabled(False)
        self.ui.next_btn.setEnabled(False)
        self.ui.label_0.setEnabled(False)
        self.ui.label_1.setEnabled(False)
        self.ui.label_2.setEnabled(False)
        self.ui.label_3.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.label_6.setEnabled(False)
        self.ui.label_7.setEnabled(False)
        self.ui.label_8.setEnabled(False)
        self.ui.delete_btn.setEnabled(False)

    def choose_source(self):
        # print("choose source")
        directory = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        print("source_path:", directory)
        self.ui.source_line.setText(directory)
        self.source_dir = directory

        # 设置开始按钮不可用
        self.ui.start_btn.setEnabled(True)

    def choose_dest(self):
        # print("choose dest")
        directory = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        print("dest_path:", directory)
        self.ui.dest_line.setText(directory)
        self.dest_dir = directory
        # 设置开始按钮不可用
        self.ui.start_btn.setEnabled(True)

    def last(self):
        print("last")
        if self.index > 0:
            self.index -= 1
            self.show_img()
            self.set_progress()

    def next(self):
        print("next")
        if self.index < len(self.list) - 1:
            self.index += 1
            self.show_img()
            self.set_progress()

    def start(self):
        print("start")
        if (not os.path.isdir(self.source_dir)) or (not os.path.isdir(self.dest_dir)):
            QMessageBox.warning(self, "文件夹有误", "请选择正确的文件夹!")
        else:
            list = os.listdir(self.source_dir)
            self.list = []
            for path in list:
                if path.endswith(".jpg"):
                    full_path = os.path.join(self.source_dir, path)
                    self.list.append(full_path)
            self.total = len(self.list)
            # print(self.total)
            self.labels = [None] * self.total
            self.new_list = [None] * self.total
            # 设置进度条
            self.index = 0
            self.set_progress()
            self.show_img()

            # 恢复按钮
            self.ui.last_btn.setEnabled(True)
            self.ui.next_btn.setEnabled(True)
            self.ui.label_0.setEnabled(True)
            self.ui.label_1.setEnabled(True)
            self.ui.label_2.setEnabled(True)
            self.ui.label_3.setEnabled(True)
            self.ui.label_4.setEnabled(True)
            self.ui.label_5.setEnabled(True)
            self.ui.label_6.setEnabled(True)
            self.ui.label_7.setEnabled(True)
            self.ui.label_8.setEnabled(True)
            self.ui.delete_btn.setEnabled(True)

            # 创建文件夹
            self.create_dir()

            # 设置开始按钮不可用
            self.ui.start_btn.setEnabled(False)


    def label(self, label):
        print(label)
        dest_path = os.path.join(self.dest_dir, str(label))
        # print(dest_path)
        if self.labels[self.index] is None:
            source_path = self.list[self.index]
        else:
            source_path = self.new_list[self.index]
        new_path = os.path.join(dest_path, os.path.basename(source_path))
        if new_path != source_path:
            shutil.move(source_path, dest_path)
        self.new_list[self.index] = new_path
        self.labels[self.index] = label
        self.index += 1
        self.show_img()
        self.set_progress()

    def delete(self):
        print("delete")
        dest_path = os.path.join(self.dest_dir, "delete")
        if self.labels[self.index] is None:
            source_path = self.list[self.index]
        else:
            source_path = self.new_list[self.index]
        new_path = os.path.join(dest_path, os.path.basename(source_path))
        if new_path != source_path:
            shutil.move(source_path, dest_path)

        self.new_list[self.index] = new_path
        self.labels[self.index] = "delete"
        self.index += 1
        self.show_img()
        self.set_progress()

    def show_img(self):
        # print("show_img")
        if self.index > self.total-1:
            QMessageBox.warning(self, "已完成", "unlabel文件夹已为空!")
            self.index -= 1
            return
        if self.labels[self.index] is None:
            self.img_path = self.list[self.index]
        else:
            self.img_path = self.new_list[self.index]
        self.img = QPixmap(self.img_path).scaled(960, 540)
        self.ui.img_label.setPixmap(self.img)

    def set_progress(self):

        self.ui.progress_label.setText("进度:{}/{}".format(self.index + 1, self.total))
        self.ui.progressBar.setValue(int((self.index + 1) / self.total *100))

    def create_dir(self):

        for i in range(9):
            dir_path = os.path.join(self.dest_dir, str(i))
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
        dir_path = os.path.join(self.dest_dir, "delete")
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)


if __name__ == '__main__':
    app = QApplication([])
    # 设置程序图标
    app.setWindowIcon(QIcon('./imgs/uestc.jpg'))
    actionlabel = actionLabel()
    actionlabel.ui.show()
    app.exec_()
