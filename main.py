#!/usr/bin/env python3

import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget
)

class StopWatchWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Stopwatch")
        self  .setFixedSize(400, 300)

        self.counter = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        main_layout = QVBoxLayout()

        self.time_label      = QLabel("00:00:00")
        self.time_label .setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            QLabel {
                font-size: 42px;
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0.5);
                border-radius: 50%;
                padding: 15px;
            }
        """)

        btn_layout = QHBoxLayout()

        self.btn_start = QPushButton("Start")
        self.btn_stop  = QPushButton("Stop")
        self.btn_reset = QPushButton("Reset")

        self.btn_stop .setEnabled(False)
        self.btn_reset.setEnabled(False)

        self.btn_start.clicked.connect(self.start_timer)
        self.btn_stop .clicked.connect(self.stop_timer)
        self.btn_reset.clicked.connect(self.reset_timer)

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        btn_layout.addWidget(self.btn_reset)

        main_layout.addWidget(self.time_label)

        main_layout.addLayout(btn_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def start_timer(self):
        self.timer.start(10)
        self.btn_start.setEnabled(False)
        self.btn_stop .setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.btn_stop .setEnabled(False)
        self.btn_start.setEnabled(True)
        self.btn_reset.setEnabled(True)

    def reset_timer(self):
        self.timer.stop()
        self.counter = 0
        self.time_label.setText("00:00:00")
        self.btn_start.setEnabled(True)
        self.btn_stop .setEnabled(False)
        self.btn_reset.setEnabled(False)

    def update_timer(self):
        self.counter += 1
        
        miliseconds   = self.counter % 100
        total_seconds = self.counter // 100
        seconds       = total_seconds % 60
        minutes       = total_seconds // 60

        time_str = f"{minutes:02d}:{seconds:02d}:{miliseconds:02d}"
        self.time_label.setText(time_str)

app = QApplication(sys.argv)
window = StopWatchWindow()
window.show()
sys.exit(app.exec())
