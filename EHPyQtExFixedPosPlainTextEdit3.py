import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
    QSizeGrip,
    QHBoxLayout,
    QFrame,
)
from PyQt6.QtCore import Qt, QEvent, QPoint, QRect
from PyQt6.QtGui import QMouseEvent


class DraggableTextEdit(QWidget):
    def __init__(self, placeholder_text="", fixed_pos=None):
        super().__init__()

        # Store fixed position parameters
        self.fixed_pos = fixed_pos or QPoint(0, 0)

        # Main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.text_edit = QPlainTextEdit()
        self.layout.addWidget(self.text_edit)
        self.size_grip = QSizeGrip(self)
        self.size_grip.setFixedSize(16, 16)
        self.layout.addWidget(self.size_grip, alignment = Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)


        # Set initial size
        self.resize(300, 200)

        # Install event filters
        self.size_grip.installEventFilter(self)
        # self.title_bar.installEventFilter(self)
        self.text_edit.installEventFilter(self)

        # Tracking variables
        self.dragging = False
        self.resizing = False
        self.start_pos = None
        self.start_geometry = None

        # Set window flags to allow overlap
        self.setWindowFlags(Qt.WindowType.SubWindow)

        self.move(self.fixed_pos)

        # Style
        self.setStyleSheet(
            f"""
            DraggableTextEdit {{
                background-color: white;
                border: 1px solid {('#999')};
            }}
        """
        )

    def eventFilter(self, obj, event):
        # Always raise to top when interacting
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.raise_()

        # Handle size grip resizing
        if obj == self.size_grip:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.resizing = True
                    self.start_pos = event.globalPosition().toPoint()
                    self.start_geometry = self.geometry()
                    self.raise_()
                    return True

            elif event.type() == QEvent.Type.MouseMove and self.resizing:
                delta = event.globalPosition().toPoint() - self.start_pos
                new_width = self.start_geometry.width() + delta.x()
                new_height = self.start_geometry.height() + delta.y()
                self.resize(max(50, new_width), max(50, new_height))
                return True

            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.resizing = False
                return True

        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.raise_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fixed and Movable TextEdits")
        self.setFixedSize(800, 600)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create fixed text edit in left-top corner
        self.fixed_edit = DraggableTextEdit(
            "Fixed TextEdit - Cannot be moved", fixed_pos=QPoint(20, 20)
        )
        self.fixed_edit.setParent(central_widget)

        # Add some sample text
        self.fixed_edit.text_edit.setPlainText(
            "This is a FIXED TextEdit.\n"
            "- Cannot be moved (fixed position)\n"
            "- Can still be resized\n"
            "- Red border indicates fixed position"
        )

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

