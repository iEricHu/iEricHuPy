import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
    QToolButton,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt, QEvent, QPoint, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QRect


class AutoResizeTextEdit(QWidget):
    def __init__(self, placeholder_text="", is_fixed=False, fixed_pos=None):
        super().__init__()

        # Store fixed position parameters
        self.is_fixed = is_fixed
        self.fixed_pos = fixed_pos or QPoint(0, 0)

        # Main widget setup
        self.setMinimumWidth(200)
        self.setFixedHeight(46)  # Total height = text_edit(26) + margins(20)

        # Create the text edit
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setPlaceholderText(placeholder_text)
        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.text_edit.setFixedHeight(26)

        # Create resize button
        self.resize_button = QToolButton(self)
        self.resize_button.setFixedSize(20, 20)
        self.resize_button.setStyleSheet(
            """
            QToolButton {
                border: none;
                background-color: #e0e0e0;
                border-radius: 3px;
                padding: 2px;
            }
            QToolButton:hover {
                background-color: #d0d0d0;
            }
            QToolButton:pressed {
                background-color: #c0c0c0;
            }
        """
        )
        self.resize_button.setText("⤡")
        self.resize_button.setToolTip("Click to auto-resize")
        self.resize_button.clicked.connect(self.auto_resize)

        # Set initial size
        self.resize(300, 46)

        # Position widgets
        self.updateWidgetPositions()

        # Install event filter
        self.text_edit.installEventFilter(self)

        # Set window flags to allow overlap
        self.setWindowFlags(Qt.WindowType.SubWindow)

        # Set fixed position if specified
        if self.is_fixed:
            self.move(self.fixed_pos)

        # Style
        self.setStyleSheet(
            f"""
            AutoResizeTextEdit {{
                background-color: white;
                border: 1px solid {('#999' if not is_fixed else '#cc0000')};
            }}
            QPlainTextEdit {{
                border: none;
            }}
        """
        )

    def updateWidgetPositions(self):
        # Position text edit
        self.text_edit.setGeometry(5, 10, self.width() - 30, 26)

        # Position button at bottom right
        self.resize_button.move(
            self.width() - self.resize_button.width() - 5,
            self.height() - self.resize_button.height() - 5,
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateWidgetPositions()

    def auto_resize(self):
        # Get the text width
        document = self.text_edit.document()
        text_width = document.idealWidth() + 50  # Add padding for margins and button

        # Set minimum width
        new_width = max(text_width, 200)

        # Resize the widget
        self.resize(new_width, 46)

        # Update positions
        self.updateWidgetPositions()

    def eventFilter(self, obj, event):
        if obj == self.text_edit:
            if event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.raise_()
        return super().eventFilter(obj, event)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.raise_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto-resize TextEdit")
        self.setFixedSize(800, 600)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create fixed text edit in left-top corner
        self.fixed_edit = AutoResizeTextEdit(
            "Fixed TextEdit with auto-resize", is_fixed=True, fixed_pos=QPoint(20, 20)
        )
        self.fixed_edit.setParent(central_widget)

        # Create movable text edit
        self.movable_edit = AutoResizeTextEdit("Movable TextEdit with auto-resize")
        self.movable_edit.setParent(central_widget)
        self.movable_edit.move(350, 20)

        # Add some sample text
        self.fixed_edit.text_edit.setPlainText(
            "This is a FIXED TextEdit. Click the resize button to auto-fit content."
        )

        self.movable_edit.text_edit.setPlainText(
            "This is a MOVABLE TextEdit. Click the resize button to auto-fit content."
        )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
