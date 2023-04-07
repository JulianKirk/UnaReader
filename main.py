import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
#  from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

import ebooklib
from ebooklib import epub
from ebooklib.utils import debug

if __name__ == "__main__":
    
    book = epub.read_epub('./test/test.epub')

    # for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    #     print(item.get_content())

    # print(book.spine);
    # debug(book.get_item_with_id("xhtml1429").get_body_content())

    # debug(book.get_metadata('DC', 'title'))
    # debug(book.get_metadata('DC', 'creator'))
    
    app = QGuiApplication()
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()
    engine.load(QUrl("main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
