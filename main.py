import sys
import random
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

import ebooklib
from ebooklib import epub
from ebooklib.utils import debug

if __name__ == "__main__":
    
    book = epub.read_epub('./test/test.epub')

    # for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    #     print(item.get_content())

    print(book.get_item_with_id("xhtml1429").get_content())

    # debug(book.get_metadata('DC', 'title'))
    # debug(book.get_metadata('DC', 'creator'))
    
    app = QApplication()
    view = QQuickView()

    view.setSource("main.qml")
    view.show()
    sys.exit(app.exec())
