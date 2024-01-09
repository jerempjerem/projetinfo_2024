import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Créer une table
        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        # Remplir la table avec des données
        for row in range(4):
            for col in range(3):
                item = QTableWidgetItem(f"({row}, {col})")
                tableWidget.setItem(row, col, item)

        # Définir la fusion des cellules pour un élément
        item_span = QTableWidgetItem("Element Span")
        tableWidget.setSpan(1, 1, 2, 1)  # (row, col, rowspan, colspan)
        tableWidget.setItem(1, 1, item_span)

        # Connecter le signal cellClicked à la fonction de gestion des clics
        tableWidget.cellClicked.connect(self.cell_clicked)

        # Mise en page
        layout = QVBoxLayout()
        layout.addWidget(tableWidget)
        self.setLayout(layout)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Table avec élément fusionné')
        self.show()

    def cell_clicked(self, row, col):
        print(f"Clic sur la cellule ({row}, {col})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    sys.exit(app.exec_())

