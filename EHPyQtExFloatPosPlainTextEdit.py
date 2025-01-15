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
from PyQt6.QtCore import Qt, QEvent, QPoint
from PyQt6.QtGui import QMouseEvent


class DraggableTextEdit(QWidget):
    def __init__(self, placeholder_text=""):
        super().__init__()

        # Remove layout constraints from parent
        self.setParent(None)

        # Main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Title bar for dragging
        self.title_bar = QFrame()
        self.title_bar.setFixedHeight(20)
        self.title_bar.setStyleSheet("background-color: #e0e0e0;")
        self.title_bar.setCursor(Qt.CursorShape.SizeAllCursor)
        self.layout.addWidget(self.title_bar)

        # PlainTextEdit
        self.text_edit = QPlainTextEdit()
        self.text_edit.setPlaceholderText(placeholder_text)
        self.layout.addWidget(self.text_edit)

        # Bottom bar with size grip
        self.bottom_bar = QWidget()
        self.bottom_bar.setFixedHeight(16)
        bottom_layout = QHBoxLayout(self.bottom_bar)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(0)

        # Add size grip
        bottom_layout.addStretch()
        self.size_grip = QSizeGrip(self.bottom_bar)
        self.size_grip.setFixedSize(16, 16)
        bottom_layout.addWidget(self.size_grip)

        self.layout.addWidget(self.bottom_bar)

        # Set initial size
        self.resize(300, 200)

        # Install event filters
        self.size_grip.installEventFilter(self)
        self.title_bar.installEventFilter(self)
        self.text_edit.installEventFilter(self)

        # Tracking variables
        self.dragging = False
        self.resizing = False
        self.start_pos = None
        self.start_geometry = None

        # Set window flags to allow overlap
        self.setWindowFlags(Qt.WindowType.SubWindow)

        # Style
        self.setStyleSheet(
            """
            DraggableTextEdit {
                background-color: white;
                border: 1px solid #999;
            }
        """
        )

    def eventFilter(self, obj, event):
        # Raise to top when starting to interact with any part
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.raise_()

        # Handle title bar dragging
        if obj == self.title_bar:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.dragging = True
                    self.start_pos = event.globalPosition().toPoint()
                    self.start_geometry = self.geometry()
                    self.raise_()  # Raise when starting drag
                    return True

            elif event.type() == QEvent.Type.MouseMove and self.dragging:
                delta = event.globalPosition().toPoint() - self.start_pos
                self.move(self.start_geometry.topLeft() + delta)
                return True

            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.dragging = False
                return True

        # Handle size grip resizing
        elif obj == self.size_grip:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.resizing = True
                    self.start_pos = event.globalPosition().toPoint()
                    self.start_geometry = self.geometry()
                    self.raise_()  # Raise when starting resize
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

        # Handle text edit interaction
        elif obj == self.text_edit:
            if event.type() == QEvent.Type.MouseButtonPress:
                self.raise_()  # Raise when clicking in text edit

        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.raise_()  # Raise on any mouse press on the widget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Overlapping TextEdits")
        self.setFixedSize(800, 600)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create text edits with offset positions
        self.text_edit1 = DraggableTextEdit(
            "TextEdit 1 - Will raise to top when dragging"
        )
        self.text_edit1.setParent(central_widget)
        self.text_edit1.move(50, 50)

        self.text_edit2 = DraggableTextEdit(
            "TextEdit 2 - Will raise to top when dragging"
        )
        self.text_edit2.setParent(central_widget)
        self.text_edit2.move(200, 150)

        # Add some sample text
        self.text_edit1.text_edit.setPlainText(
            "This is TextEdit 1.\n"
            "- Drag title bar to move (raises to top)\n"
            "- Resize from corner (raises to top)\n"
            "- Click anywhere to bring to front"
        )

        self.text_edit2.text_edit.setPlainText(
            "This is TextEdit 2.\n"
            "- Drag title bar to move (raises to top)\n"
            "- Resize from corner (raises to top)\n"
            "- Click anywhere to bring to front"
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())