from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a combo box
        combo_box = QComboBox(self)
        combo_box.addItem("AND")
        combo_box.addItem("OR")

        # Connect a function to handle the change in the combo box
        combo_box.currentIndexChanged.connect(self.on_combobox_change)

        # Add the combo box to the layout
        layout.addWidget(combo_box)

        self.setLayout(layout)

    def on_combobox_change(self, index):
        # Handle the change in the combo box selection
        selected_option = self.sender().itemText(index)
        print(f"Selected Option: {selected_option}")

if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    window.show()
    app.exec_()
