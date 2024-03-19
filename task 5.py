import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from PyQt5.QtCore import Qt
class ContactBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contact Book')
        self.setGeometry(100, 100, 400, 300)

        # Contact information fields
        self.name_label = QLabel('Name:')
        self.name_edit = QLineEdit()
        self.phone_label = QLabel('Phone:')
        self.phone_edit = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_edit = QLineEdit()
        self.address_label = QLabel('Address:')
        self.address_edit = QLineEdit()

        # Buttons
        self.add_button = QPushButton('Add')
        self.search_button = QPushButton('Search')
        self.update_button = QPushButton('Update')
        self.delete_button = QPushButton('Delete')

        # Contact list
        self.contact_list = QListWidget()

        # Layout setup
        main_layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_edit)
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_edit)
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_edit)
        form_layout.addWidget(self.address_label)
        form_layout.addWidget(self.address_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.contact_list)

        self.setLayout(main_layout)

        # Connect button clicks to methods
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)
        self.update_button.clicked.connect(self.update_contact)
        self.delete_button.clicked.connect(self.delete_contact)

    def add_contact(self):
        name = self.name_edit.text()
        phone = self.phone_edit.text()
        email = self.email_edit.text()
        address = self.address_edit.text()

        # Add contact to list
        self.contact_list.addItem(f"{name}: {phone}, {email}, {address}")

        # Clear input fields after adding
        self.clear_fields()

    def search_contact(self):
        search_term = self.name_edit.text()
        items = self.contact_list.findItems(search_term, Qt.MatchExactly)

        if items:
            item = items[0]
            self.contact_list.setCurrentItem(item)
        else:
            QMessageBox.information(self, "Search", "Contact not found.")

    def update_contact(self):
        current_item = self.contact_list.currentItem()
        if current_item:
            new_name = self.name_edit.text()
            new_phone = self.phone_edit.text()
            new_email = self.email_edit.text()
            new_address = self.address_edit.text()

            updated_text = f"{new_name}: {new_phone}, {new_email}, {new_address}"
            current_item.setText(updated_text)

            self.clear_fields()
        else:
            QMessageBox.information(self, "Update", "No contact selected.")

    def delete_contact(self):
        current_item = self.contact_list.currentItem()
        if current_item:
            self.contact_list.takeItem(self.contact_list.row(current_item))
            self.clear_fields()
        else:
            QMessageBox.information(self, "Delete", "No contact selected.")

    def clear_fields(self):
        self.name_edit.clear()
        self.phone_edit.clear()
        self.email_edit.clear()
        self.address_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    contact_book = ContactBook()
    contact_book.show()
    sys.exit(app.exec_())
