class Figure:

    def __init__(self):
        self.color = 'white'

    def changecolor(self, newcolor):
        self.color = newcolor
 
class Oval(Figure):
    def __init__(self):
        Figure.__init__(self)
        self.form = 'oval'
