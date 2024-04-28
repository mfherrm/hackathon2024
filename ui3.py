import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import pandas as pd
import time
from threading import Thread

class DataFrameViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DataFrame Viewer')
        self.layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

    def display_dataframe(self, dataframe):
        self.table_widget.setRowCount(dataframe.shape[0])
        self.table_widget.setColumnCount(dataframe.shape[1])
        self.table_widget.setHorizontalHeaderLabels(dataframe.columns)

        for i in range(dataframe.shape[0]):
            for j in range(dataframe.shape[1]):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(dataframe.iat[i, j])))

        self.show()

def create_and_display_dataframe(dataframe):
    app = QApplication(sys.argv)
    window = DataFrameViewer()
    window.display_dataframe(dataframe)
    sys.exit(app.exec_())

if __name__ == '__main__':
    # Test dataframes
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})


    # Display first dataframe
    t1 = Thread(target=create_and_display_dataframe, args=(df1,))
    t1.start()

    # Sleep for 2 seconds and then display second dataframe
    time.sleep(2)
    t2 = Thread(target=create_and_display_dataframe, args=(df2,))
    t2.start()
