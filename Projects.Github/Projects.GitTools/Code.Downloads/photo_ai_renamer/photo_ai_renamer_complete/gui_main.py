import sys
import os
import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QMessageBox
)
from rename_logic import process_images

LOG_PATH = os.path.join(os.path.dirname(__file__), 'logs')

def write_log(message):
    os.makedirs(LOG_PATH, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logfile = os.path.join(LOG_PATH, f"log_{timestamp}.txt")
    with open(logfile, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

class PhotoRenamerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Photo AI Renamer")
        self.setGeometry(200, 200, 400, 200)

        self.source_folder = ""
        self.output_folder = ""

        layout = QVBoxLayout()

        self.status_label = QLabel("Select a source folder to begin.")
        layout.addWidget(self.status_label)

        self.select_button = QPushButton("Select Source Folder")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.source_folder = folder
            time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.output_folder = os.path.join(
                os.path.dirname(folder),
                f"output_{time_stamp}"
            )
            os.makedirs(self.output_folder, exist_ok=True)

            msg = f"Source: {self.source_folder}\nOutput: {self.output_folder}"
            self.status_label.setText(msg)
            write_log(f"Selected source folder: {self.source_folder}")
            write_log(f"Created output folder: {self.output_folder}")

            process_images(self.source_folder, self.output_folder, write_log)
            QMessageBox.information(self, "Done", "Files renamed and copied.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoRenamerApp()
    window.show()
    sys.exit(app.exec_())
