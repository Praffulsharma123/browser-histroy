class BrowserHistroy(object):

    def __init__(self,homepage) :  # initailize the histroy page
       self.histroy=[homepage]
       self.current_index = 0

    def visit(self,url):
        self.histroy = self.histroy[:self.current_index+1]
        self.histroy.append(url)
        self.current_index = len(self.histroy) - 1

    def back(self,steps):
        self.current_index = max(0, self.current_index - steps)
        return self.histroy[self.current_index]

    def forward(self,steps):
        self.current_index = min(len(self.histroy)- 1, self.current_index + steps)
        return self.histroy[self.current_index]

