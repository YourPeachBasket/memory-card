from random import randint, shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QButtonGroup
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
but = QPushButton('Ответить')
text = QLabel('Какой национальости не существует?')
Box = QGroupBox('Варианты ответа:')
answ1 = QRadioButton('Энцы')
answ2 = QRadioButton('Смурфы')
answ3 = QRadioButton('Чулымцы')
answ4 = QRadioButton('Алеуты')
AnsGroupBox = QGroupBox('Результата теста')
show1 = QLabel('Правильно/Неправильно')
show2 = QLabel('Правильный ответ')
answers = [answ1, answ2, answ3, answ4]
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def ask(q: Question):
    shuffle(answers)
    text.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show2.setText(q.right_answer)
    show_qst()
def check_answer():
    if answers[0].isChecked():
        show1.setText('Правильно')
        start_check()
    else:
        show1.setText('Неправильно')
        start_check()
main_win.cur_question = -1    
layoutRez = QVBoxLayout()
layoutRez.addWidget(show1, alignment= (Qt.AlignLeft | Qt.AlignTop))
layoutRez.addWidget(show2, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layoutRez)

layout1 = QHBoxLayout()
layout2  = QVBoxLayout()
layout3 = QVBoxLayout()
layout2.addWidget(answ1)
layout2.addWidget(answ2)
layout3.addWidget(answ3)
layout3.addWidget(answ4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
Box.setLayout(layout1)
RadioGroup = QButtonGroup()
RadioGroup.addButton(answ1)
RadioGroup.addButton(answ2)
RadioGroup.addButton(answ3)
RadioGroup.addButton(answ4)
line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()
line_v3 = QVBoxLayout()
line_v1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line_v2.addWidget(Box)
line_v2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
line_v3.addStretch(1)
line_v3.addWidget(but, stretch=2)
line_v3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(line_v1, stretch=2)
layout_card.addLayout(line_v2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(line_v3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)
def show_result():
    Box.hide()
    AnsGroupBox.show()
    but.setText('Следующий вопрос')
def show_qst():
    Box.show()
    AnsGroupBox.hide()
    RadioGroup.setExclusive(False)
    answ1.setChecked(False)
    answ2.setChecked(False)
    answ3.setChecked(False)
    answ4.setChecked(False)
    RadioGroup.setExclusive(True)
    but.setText('Ответить')
def start_check():
    if but.text() == 'Ответить':
        show_result()
    else:
        next_question()
questions = list()
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Итальянский', 'Испанский')
questions.append(q1)
q2 = Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Синий', 'Белый')
questions.append(q2)
q3 = Question('Государственный язык Португалии', 'Португальский', 'Испанский', 'Французский', 'Немецкий')
questions.append(q3)
q4 = Question('Как называют математические примеры на английском', 'Problem', 'Example', 'Question', 'Prime')
questions.append(q4)
q5 = Question('Какое название у переменной на английском?', 'Variable', 'Change', 'Variant', 'Value')
questions.append(q5)
def next_question():
    q = questions[randint(0, len(questions)-1)]
    ask(q)
but.clicked.connect(check_answer)
main_win.resize(400,300)
main_win.show()
app.exec()