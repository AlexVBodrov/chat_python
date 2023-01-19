import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import sqlite3
import bcrypt
from time import sleep


DATABASE = 'client/users_info.db'
UI_login_form = 'client\login_form\login.ui'
UI_create_acc = 'client\login_form\create_acc.ui'


class Login(QDialog):
    """
        QDialog Login to chat client.
    """
    def __init__(self):
        super(Login, self).__init__()
        loadUi(UI_login_form, self)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_login.clicked.connect(self.loginfuntion)
        self.btn_create_account.clicked.connect(self.goto_create_account)
    
    
    def loginfuntion(self):
        """Login to chat client."""
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()
        if len(name) == 0 or len(password) == 0:
            self.label_error_message.setText('Ошибка. Заполните все поля!')
        else:
            self.validate_password(name, password, name_bd=DATABASE)
    
    def validate_password(self, username, password,  name_bd=DATABASE):
        """Validate password
        """
        name = username
        
        #bytes for  hash function
        password = password.encode('utf-8')
        
        # create connection to
        connect_to_bd = sqlite3.connect(DATABASE)
        # create cursor for
        cur = connect_to_bd.cursor()
        # select_query from database
        sqlite_select_query = """SELECT password from users WHERE username = ?"""
        cur.execute(sqlite_select_query, (name,))
        try:
            # Получаем Хэш из БД
            hash_password = cur.fetchone()[0]
            # Проверяем с помощью bcrypt password => hash_password
            if bcrypt.checkpw(password, hash_password):
                self.label_error_message.setText(f'Successfully logged in name={name}')
            else:
                self.label_error_message.setText('Ошибка. Неверные имя или пароль!')
        except:
            self.label_error_message.setText('Ошибка. Неверные имя или пароль!')
        connect_to_bd.close()
    
    def goto_create_account(self):
        """Goes to create a new account"""
        create_acc = CreateAcc()
        widget.addWidget(create_acc)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        

class CreateAcc(QDialog):
    """
        Create a new account
    """
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi(UI_create_acc, self)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_conform.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_sing_up.clicked.connect(self.create_acc_funtion)
        # back to login form
        self.pushButton_back_login.clicked.connect(self.goto_login)
    
    
    def create_acc_funtion(self):
        """Login to chat client."""
        name = self.lineEdit_name.text()
        email = self.lineEdit_email.text()
        
        password = self.lineEdit_password.text()
        # TODO validate to save password. check password for secure
        if len(email) == 0 or len(name) == 0 or len(password) == 0:
            self.label_info.setText(f'Ошибка. Заполните все поля!')
        elif self.lineEdit_password.text() != self.lineEdit_password_conform.text():
                self.label_info.setText(f'Ошибка. Пароли не совпадают!')
        else:
            self.create_acc(name, email, password)
      
            # back to login form
            self.goto_login()

    def create_acc(self, name, email, password):
        """Create new account"""
        # password = '1234'.encode('utf-8')
        # hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # print(hashed)
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        # create connection to
        connect_to_bd = sqlite3.connect(DATABASE)
        # create cursor for
        cur = connect_to_bd.cursor()
        # select_query from database
        query = 'INSERT INTO users (username, password, email) VALUES (?, ?, ?)'
        new_row = (name, hashed, email)
        cur.execute(query, new_row)
        connect_to_bd.commit()
        connect_to_bd.close()
        
    
    def goto_login(self):
        # back to login form
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)
      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_login = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_login)
    # widget.setFixedWidth(400)
    # widget.setFixedHeight(400)
    widget.show()
    sys.exit(app.exec_())
