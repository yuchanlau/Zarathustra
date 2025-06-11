import sys
import random
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox

class RandomExcelViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("电子算命")
        self.resize(400, 300)
        self.layout = QVBoxLayout()

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("请输入内容...")
        self.input_box.setFixedHeight(40)
        self.layout.addWidget(self.input_box)

        self.show_btn = QPushButton("确定")
        self.show_btn.clicked.connect(self.show_random_answer)
        self.layout.addWidget(self.show_btn)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        self.result_label.setMinimumHeight(180)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

       
        self.excel_path = "output.csv"
        try:
            self.df = pd.read_csv(self.excel_path)
        except Exception as e:
            QMessageBox.critical(self, "错误", f"查拉图斯特拉生气了: {e}")
            self.df = pd.DataFrame()

    def on_confirm(self):
        user_text = self.input_box.toPlainText().strip()
        if user_text:
            self.result_label.setText(f"你输入了: {user_text}")
        else:
            self.result_label.setText("请输入内容！")

    def show_random_answer(self):
        if not self.df.empty and "答案" in self.df.columns:
            row = self.df.sample(1).iloc[0]
            self.result_label.setText(str(row["答案"]))
        else:
            self.result_label.setText("未找到可用的答案数据。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = RandomExcelViewer()
    viewer.show()
    sys.exit(app.exec_())