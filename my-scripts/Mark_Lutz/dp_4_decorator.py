class Text():
    def __init__(self,text):
        self.text = text
    
    def get_text(self):
        return self.text
    
class Underline():
    def __init__(self,wrapped):
        self.wrapped = wrapped
    
    def get_text(self):
        return "<u>{}<u>".format(self.wrapped.get_text())
        
class Bold():
    def __init__(self,wrapped):
        self.wrapped = wrapped
    
    def get_text(self):
        return "<b>{}<b>".format(self.wrapped.get_text())
class Italic():
    def __init__(self,wrapped):
        self.wrapped = wrapped
    
    def get_text(self):
        return "<i>{}<i>".format(self.wrapped.get_text())

a = Text('Jaspreet Sethi')
print(a.get_text())
b = Italic(Bold(Underline(a)))
print(b.get_text())


