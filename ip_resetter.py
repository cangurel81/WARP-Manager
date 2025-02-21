import sys
import requests
import subprocess
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QLabel, QHBoxLayout, QMessageBox, QComboBox,
                            QListWidget, QListWidgetItem)
from PyQt6.QtCore import QTimer, Qt, QTime
from PyQt6.QtGui import QIcon, QFont

def resource_path(relative_path):
    try:
        # PyInstaller'ın oluşturduğu geçici klasör
        base_path = sys._MEIPASS
    except Exception:
        # Normal çalışma durumu için geçerli dizin
        base_path = os.path.abspath(".")
    
    print(f"Resource path debug: {os.path.join(base_path, relative_path)}")  # Hata ayıklama için
    return os.path.join(base_path, relative_path)

class IPResetter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.reset_interval = 4  # Default 4 minutes
        self.is_running = False
        self.ip_history = []
        
        self.init_ui()
        self.timer = QTimer()
        self.timer.timeout.connect(self.reset_ip)
        self.ip_update_timer = QTimer()
        self.ip_update_timer.timeout.connect(self.update_ip)
        self.ip_update_timer.start(5000)
        self.setWindowIcon(QIcon(resource_path('rst.ico')))

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # IP Information
        ip_layout = QHBoxLayout()
        self.ip_label = QLabel("Current IP:")
        self.current_ip = QLabel()
        ip_layout.addWidget(self.ip_label)
        ip_layout.addWidget(self.current_ip)
        main_layout.addLayout(ip_layout)

        # IP History
        self.history_list = QListWidget()
        self.history_list.setMaximumHeight(100)
        main_layout.addWidget(QLabel("Recent IP Addresses:"))
        main_layout.addWidget(self.history_list)

        # Status
        status_layout = QHBoxLayout()
        self.status_label = QLabel("Status:")
        self.status_value = QLabel("Stopped")
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(self.status_value)
        main_layout.addLayout(status_layout)

        # Interval Selection
        interval_layout = QHBoxLayout()
        interval_label = QLabel("Refresh Interval:")
        self.interval_combo = QComboBox()
        self.interval_combo.addItems([f"{i}" for i in range(1, 11)])
        self.interval_combo.setCurrentText(str(self.reset_interval))
        self.interval_combo.currentTextChanged.connect(self.change_interval)
        interval_layout.addWidget(interval_label)
        interval_layout.addWidget(self.interval_combo)
        interval_layout.addWidget(QLabel("Minutes"))
        main_layout.addLayout(interval_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.manual_reset_button = QPushButton("Manual IP Reset")
        self.manual_reset_button.clicked.connect(self.reset_ip)
        button_layout.addWidget(self.manual_reset_button)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.clicked.connect(self.toggle_reset)
        button_layout.addWidget(self.toggle_button)
        main_layout.addLayout(button_layout)

        # Footer
        footer_layout = QHBoxLayout()
        left_footer = QLabel("WebAdHere Software")
        right_footer = QLabel("Cloudflare WARP Manager v1.0")
        
        # Footer styles
        footer_style = "color: #666666; font-size: 8pt;"
        left_footer.setStyleSheet(footer_style)
        right_footer.setStyleSheet(footer_style)

        # Hizalama ayarları
        left_footer.setAlignment(Qt.AlignmentFlag.AlignLeft)
        right_footer.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Layout'a ekleme
        footer_layout.addWidget(left_footer)
        footer_layout.addStretch()  # Araya esnek boşluk ekliyoruz
        footer_layout.addWidget(right_footer)

        main_layout.addLayout(footer_layout)

        self.update_ip()
        self.setWindowTitle("WARP Manager")
        self.setFixedSize(400, 400)

    def update_ip(self):
        try:
            new_ip = requests.get('https://ifconfig.me').text
            current_ip = self.current_ip.text()
            
            if current_ip != new_ip and current_ip != 'N/A':
                self.ip_history.insert(0, current_ip)
                if len(self.ip_history) > 10:
                    self.ip_history.pop()
                
                self.history_list.clear()
                for ip in self.ip_history:
                    self.history_list.addItem(QListWidgetItem(ip))
            
            self.current_ip.setText(new_ip)
        except:
            self.current_ip.setText('N/A')

    def change_interval(self, value):
        self.reset_interval = int(value)
        if self.is_running:
            self.timer.setInterval(self.reset_interval * 60000)

    def toggle_reset(self):
        if not self.is_running:
            self.is_running = True
            self.toggle_button.setText("Stop")
            self.status_value.setText("Running")
            self.timer.start(self.reset_interval * 60000)
            self.reset_ip()
        else:
            self.is_running = False
            self.toggle_button.setText("Start")
            self.status_value.setText("Stopped")
            self.timer.stop()

    def reset_ip(self):
        try:
            subprocess.run(['warp-cli', 'disconnect'], 
                         check=True, 
                         creationflags=subprocess.CREATE_NO_WINDOW)
            QTimer.singleShot(1000, self._connect_warp)
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Error", "WARP CLI error")

    def _connect_warp(self):
        try:
            subprocess.run(['warp-cli', 'connect'], 
                         check=True, 
                         creationflags=subprocess.CREATE_NO_WINDOW)
            QTimer.singleShot(1000, self.update_ip)
        except subprocess.CalledProcessError:
            QMessageBox.critical(self, "Error", "WARP CLI error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IPResetter()
    window.show()
    sys.exit(app.exec()) 