import sys
from PyQt5.QtWidgets import QApplication, QWidget 

# Create the application object
app = QApplication(sys.argv)

# Create a simple window
window = QWidget()
window.setWindowTitle('Hello, PyQt5!')
window.setGeometry(100, 100, 280, 80)  # x, y, width, height

# Show the window
window.show()

# Run the application's event loop
sys.exit(app.exec_())
