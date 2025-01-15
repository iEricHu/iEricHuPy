from PyQt6.QtWidgets import (
    QMainWindow,
    QDockWidget,
    QTextEdit,
    QApplication,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QLabel,
)
from PyQt6.QtCore import Qt


class CustomTitleBar(QWidget):
    def __init__(self, dock_widget, parent=None):
        super().__init__(parent)
        self.dock_widget = dock_widget

        # Create horizontal layout for the title bar
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 5, 0)

        # Add title label
        self.title_label = QLabel("My Dock")

        # Create dock button
        self.dock_button = QPushButton("Dock")
        self.dock_button.setFixedSize(50, 20)  # Make button smaller to fit in title bar
        self.dock_button.clicked.connect(self.dock_widget_clicked)

        # Add widgets to layout
        layout.addWidget(self.title_label)
        layout.addStretch()  # This pushes the button to the right
        layout.addWidget(self.dock_button)

        # Update button visibility based on floating state
        self.dock_widget.topLevelChanged.connect(self.update_button_visibility)

    def dock_widget_clicked(self):
        if self.dock_widget.isFloating():
            self.dock_widget.setFloating(False)

    def update_button_visibility(self, floating):
        self.dock_button.setVisible(floating)


class CustomDockWidget(QDockWidget):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)

        # Create and set custom title bar widget
        self.title_bar = CustomTitleBar(self)
        self.setTitleBarWidget(self.title_bar)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DockWidget with Custom Title Bar")
        self.resize(800, 600)

        # Create central widget
        self.central_widget = QTextEdit()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setText("Central Widget")

        # Create custom dock widget
        self.dock = CustomDockWidget("My Dock", self)
        self.dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable
            | QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetClosable
        )

        # Create and set dock content
        self.dock_content = QTextEdit()
        self.dock_content.setText("Dock Content")
        self.dock.setWidget(self.dock_content)

        # Add dock widget to main window
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

        # Store the last dock area
        self.last_dock_area = Qt.DockWidgetArea.LeftDockWidgetArea
        self.dock.dockLocationChanged.connect(self.on_dock_location_changed)

    def on_dock_location_changed(self, area):
        if area != Qt.DockWidgetArea.NoDockWidgetArea:
            self.last_dock_area = area


# if __name__ == "__main__":
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
