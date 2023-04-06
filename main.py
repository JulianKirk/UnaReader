import sys
import random
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

import ebooklib
from ebooklib import epub
from ebooklib.utils import debug

if __name__ == "__main__":
    
    book = epub.read_epub('./test/test.epub')

    debug(book.metadata)
    
    app = QApplication()
    view = QQuickView()

    view.setSource("main.qml")
    view.show()
    sys.exit(app.exec())
