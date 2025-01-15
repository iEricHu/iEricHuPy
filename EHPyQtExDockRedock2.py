from PyQt6.QtWidgets import (
    QMainWindow,
    QDockWidget,
    QTextEdit,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DockWidget Closable Demo")
        self.resize(800, 600)

        # Create central widget with controls
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create buttons to control dock widget features
        self.toggle_close_btn = QPushButton("Toggle Closable")
        self.toggle_close_btn.clicked.connect(self.toggle_closable)
        layout.addWidget(self.toggle_close_btn)

        # Create dock widget
        self.dock = QDockWidget("My Dock", self)

        # Set initial features
        self.dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable
            | QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QDockWidget.DockWidgetFeature.DockWidgetClosable  # Initially closable
        )

        # Add content to dock widget
        self.dock_content = QTextEdit("Dock Content")
        self.dock.setWidget(self.dock_content)

        # Add dock widget to main window
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

    def toggle_closable(self):
        current_features = self.dock.features()
        closable = QDockWidget.DockWidgetFeature.DockWidgetClosable

        if current_features & closable:
            # Remove Closable feature
            new_features = current_features & ~closable
            self.toggle_close_btn.setText("Make Closable")
        else:
            # Add Closable feature
            new_features = current_features | closable
            self.toggle_close_btn.setText("Make Not Closable")

        self.dock.setFeatures(new_features)

    def get_feature_status(self):
        """Helper method to print current feature status"""
        features = self.dock.features()
        closable = bool(features & QDockWidget.DockWidgetFeature.DockWidgetClosable)
        print(f"Closable: {closable}")


# if __name__ == "__main__":
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
