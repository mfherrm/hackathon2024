import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQUAT MANIA")
        self.setFixedSize(800, 600)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)

        self.central_widget.setLayout(self.layout)

        # Timer to continuously update the image
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(16)  # Update every 1000 milliseconds (1 second)

        # Member variable to store the current image content
        self.current_image = None
            
        self.stats_widget = StatsWidget()

    def update_image(self):
        """Update the displayed image"""
        if self.current_image is not None:
            # Convert the numpy array to a QImage
            h, w, c = self.current_image.shape
            q_image = QImage(self.current_image.data, w, h, w * c, QImage.Format_RGB888)

            # Convert QImage to QPixmap
            pixmap = QPixmap.fromImage(q_image)

            # Set the pixmap onto the label
            self.image_label.setPixmap(pixmap)

class StatsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stats_label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.stats_label)
        self.setLayout(layout)

    def update_stats(self, stats):
        self.stats_label.setText(stats)

def get_next_image():
    """Function to get the next image from the model"""

    return np.random.randint(0, 256, size=(224, 224, 3), dtype=np.uint8)
def get_next_text():
    """Function to get the next text content"""
    return "Hello, World!"

def main(frame):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Continuously update the current image content
    while True:
        window.current_image = frame
        window.current_text = get_next_text()
        QApplication.processEvents()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()