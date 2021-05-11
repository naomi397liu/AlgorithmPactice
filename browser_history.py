class BrowserHistory:

    def __init__(self, homepage):
        """
        :type homepage: str
       
        """
        self.homepage = homepage
        self.pages = [homepage]
        self.current = 0
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        
        """
        if self.current != len(self.pages)-1:
            self.pages = self.pages[:self.current + 1]
            self.pages.append(url)
            self.current = len(self.pages) - 1
            return self.pages[self.current]
        else:
            self.pages.append(url)
            self.current = len(self.pages)-1
            return self.pages[self.current]
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        if the user chooses steps too big, then return homepage
    
        """
        if 0 > self.current - steps:
            self.current = 0
            return self.homepage
        else:
            self.current = self.current-steps
            return self.pages[self.current]
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        if you cannot move forward stay on current url 
        """
        if len(self.pages) <= self.current + steps:
            self.current = len(self.pages) - 1
            return self.pages[self.current]
        else:
            self.current = self.current + steps
            return self.pages[self.current]