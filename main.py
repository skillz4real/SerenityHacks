import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import datetime

con = sqlite3.connect("cashcalm.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS calendar(date DATE PRIMARY KEY, details TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(idx INTEGER PRIMARY KEY, details TEXT);")
con.commit()
con.close()

class main_interface(QDialog):
    def __init__(self):
        super(main_interface, self).__init__()
        uic.loadUi("main.ui", self)
        
        calendar_win = calendar_interface()
        budget_win = budget_interface()
#        tm_win = tm_interface()
        
        global widget
        widget.addWidget(self)
        widget.addWidget(calendar_win)
        widget.addWidget(budget_win)
#        self.widget.addWidget(tm_win)
        widget.show()
        
        self.calendar_btn.clicked.connect(self.spawn_calendar)
        self.budget_btn.clicked.connect(self.spawn_budget)
    #    self.tm_btn.clicked.connect(self.spawn_tm)

    def spawn_calendar(self):
        widget.setCurrentIndex(1)

    def spawn_budget(self):
        widget.setCurrentIndex(2)
    
    #def spawn_tm(self):
    #    self.widget.setCurrentIndex(3)

class calendar_interface(QDialog):
    def __init__(self):
        global widget
        super(calendar_interface, self).__init__()
        uic.loadUi("calendar.ui", self)
        self.back_btn.clicked.connect(self.return_main)
        self.add_event_btn.clicked.connect(self.add_event)
        self.remove_event_btn.clicked.connect(self.remove_event)
        self.calendar.clicked.connect(self.view_events)
        self.remove_event_btn.clicked.connect(self.remove_event)

    def return_main(self):
        widget.setCurrentIndex(0)

    def add_event(self):
        details = self.new_event_details.toPlainText()
        qdate = self.calendar.selectedDate()
        year = qdate.year()
        month = qdate.month()
        day = qdate.day()

        date = datetime.date(year, month, day)
        print(details)
        print(date)
        con = sqlite3.connect("cashcalm.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO calendar VALUES (?,?);", (date, details))
        con.commit()
        con.close()
        self.new_event_details.clear()
        self.view_events()        

    def remove_event(self):
        qdate = self.calendar.selectedDate()
        year = qdate.year()
        month = qdate.month()
        day = qdate.day()
        date = datetime.date(year, month, day)

        con = sqlite3.connect("cashcalm.db")
        cursor = con.cursor()

        res = cursor.execute("DELETE FROM calendar WHERE date=?", (str(date),))
        con.commit()
        con.close()
        self.view_events()

    def view_events(self):
        qdate = self.calendar.selectedDate()
        year = qdate.year()
        month = qdate.month()
        day = qdate.day()
        date = datetime.date(year, month, day)

        con = sqlite3.connect("cashcalm.db")
        cursor = con.cursor()

        res = cursor.execute("SELECT date, details FROM calendar WHERE date=?", (str(date),))
        values = res.fetchall()
        #res = cursor.execute("SELECT date, details FROM calendar WHERE date")
        ul_tag = "<ul>"           
        ul_ctag = "</ul>"
        content = ""
        for value in values:
            content += f"<li>{value[1]}</li>"
        self.events_display.setHtml(f"{ul_tag}{content}{ul_ctag}")
        con.close()


class budget_interface(QDialog):
    def __init__(self):
        global widget
        super(budget_interface, self).__init__()
        uic.loadUi("budget.ui", self)
        self.back_btn.clicked.connect(self.return_main)
        self.add_expense_btn.clicked.connect(self.add_expense)
        #self.show()
    
    def return_main(self):
        widget.setCurrentIndex(0)

    
    def add_expense(self):
        expense = self.new_expense.text()
        budget = str(self.budget.toPlainText()).split('$')[1]
        balance = str(self.balance.toPlainText()).split('$')[1]

        try:
            with open("expense_sheet.csv", 'x') as f:
                f.write(f"{datetime.datetime.now()},{budget},{expense},{balance}")
        except:
            with open("expense_sheet.csv", 'a') as f:
                f.write(f"{datetime.datetime.now()},{budget},{expense},{balance}")
        
        self.new_expense.clear()




    def remove_expense(self):
        pass

    def update_budget(self):
        budget = str(self.budget.toPlainText()).split('$')[1]

        """
        qdate = self.calendar.selectedDate()
        year = qdate.year()
        month = qdate.month()
        day = qdate.day()
        date = datetime.date(year, month, day)

        con = sqlite3.connect("cashcalm.db")
        cursor = con.cursor()

        res = cursor.execute("SELECT date, details FROM calendar WHERE date=?", (str(date),))
        values = res.fetchall()
        #res = cursor.execute("SELECT date, details FROM calendar WHERE date")
        ul_tag = "<ul>"           
        ul_ctag = "</ul>"
        content = ""
        for value in values:
            content += f"<li>{value[1]}</li>"
        self.events_display.setHtml(f"{ul_tag}{content}{ul_ctag}")
        con.close()

 
        """
        

class tm_interface(QDialog):
    def __init__(self):
        super(tm_interface, self).__init__()
        uic.loadUi("tm.ui", self)
        self.back_btn.clicked.connect(self.return_main)
        #self.show()
  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_window =  main_interface()
    app.exec()