class Store:
    def __init__(self, size, sales_month, item_categories, off_license, item_list) -> None:
        '''Vars should be called as inputted, eg size should be self.size'''
        pass
    
    def update_monthly(self, value:float) -> None:
        '''Update monthly sales'''
        pass
    
    def add_item(self, item:str) -> None:
        '''Update item list'''
        pass

    def max_sales(self):
        '''Return max sale value'''
        pass
    
    def min_sales(self):
        '''Return min sale value'''
        pass
    
    def avg_sales(self):
        '''Return average sales'''
        pass

    def __repr__(self):
        pass

