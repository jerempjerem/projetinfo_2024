import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton

class PlatSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sélection de plats')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.list_widget.setFocusPolicy(Qt.NoFocus)

        # Liste plus longue de plats
        plats = [
            'Pizza', 'Burger', 'Pâtes', 'Salade', 'Sushi', 'Tacos',
            'Steak', 'Curry', 'Riz frit', 'Tarte aux pommes', 'Crevettes', 'Poulet rôti',
            'Lasagne', 'Poisson grillé', 'Hamburger', 'Tiramisu', 'Fajitas', 'Spaghetti Bolognese',
            'Gâteau au chocolat', 'Fruits de mer', 'Salade César', 'Pad Thai', 'Raviolis',
            'Sorbet', 'Wrap au poulet', 'Tarte au citron', 'Nouilles ramen'
        ]

        # for plat in sorted(plats):
        #     item = self.list_widget.addItem(plat)

        self.list_widget.addItems(plats)
        layout.addWidget(self.list_widget)

        # Rendre la QListWidget scrollable
        self.list_widget.setFixedHeight(200)
        self.list_widget.setFixedWidth(300)

        select_button = QPushButton('Sélectionner')
        select_button.clicked.connect(self.get_selected_plats)
        layout.addWidget(select_button)

        self.setLayout(layout)

    def get_selected_plats(self):
        selected_items = self.list_widget.selectedItems()
        selected_plats = [item.text() for item in selected_items]
        print('Plats sélectionnés:', selected_plats)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PlatSelector()
    ex.show()
    sys.exit(app.exec_())


