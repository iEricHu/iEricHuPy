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
    def __init__(self, placeholder_text="", is_fixed=False, fixed_pos=None):
        super().__init__()

        # Store fixed position parameters
        self.is_fixed = is_fixed
        self.fixed_pos = fixed_pos or QPoint(0, 0)

        # Main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Title bar for dragging
        self.title_bar = QFrame()
        self.title_bar.setFixedHeight(20)
        self.title_bar.setStyleSheet(
            "background-color: #e0e0e0;" + ("color: #999;" if is_fixed else "")
        )
        self.title_bar.setCursor(
            Qt.CursorShape.ArrowCursor if is_fixed else Qt.CursorShape.SizeAllCursor
        )
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

        # Set fixed position if specified
        if self.is_fixed:
            self.move(self.fixed_pos)

        # Style
        self.setStyleSheet(
            f"""
            DraggableTextEdit {{
                background-color: white;
                border: 1px solid {('#999' if not is_fixed else '#cc0000')};
            }}
        """
        )

    def eventFilter(self, obj, event):
        # Always raise to top when interacting
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.raise_()

        # Handle title bar dragging (only if not fixed)
        if obj == self.title_bar and not self.is_fixed:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.dragging = True
                    self.start_pos = event.globalPosition().toPoint()
                    self.start_geometry = self.geometry()
                    self.raise_()
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
            "Fixed TextEdit - Cannot be moved", is_fixed=True, fixed_pos=QPoint(20, 20)
        )
        self.fixed_edit.setParent(central_widget)

        # Create movable text edit
        self.movable_edit = DraggableTextEdit(
            "Movable TextEdit - Can be dragged anywhere"
        )
        self.movable_edit.setParent(central_widget)
        self.movable_edit.move(350, 20)

        # Add some sample text
        self.fixed_edit.text_edit.setPlainText(
            "This is a FIXED TextEdit.\n"
            "- Cannot be moved (fixed position)\n"
            "- Can still be resized\n"
            "- Red border indicates fixed position"
        )

        self.movable_edit.text_edit.setPlainText(
            "This is a MOVABLE TextEdit.\n"
            "- Can be dragged anywhere\n"
            "- Can be resized\n"
            "- Gray border indicates movable"
        )


# if __name__ == "__main__":
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


# You're welcome! A few tips about this implementation that might be helpful:
#
# 1. If you want to change the fixed position, just modify the `fixed_pos=QPoint(x, y)` values
# 2. The red border helps identify the fixed TextEdit
# 3. Both TextEdits can still be resized using the size grip
# 4. You can still create more movable TextEdits by creating new instances
# 5. Both TextEdits will raise to top when clicked, making them easy to work with
#
# Feel free to ask if you need any modifications or have questions about other PyQt features!