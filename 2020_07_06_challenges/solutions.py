'''
The advanced requirements are:
Implement a feature where the user can add different months of pay and then method to allow them to do the following:
-> Highest payed month
-> Lowest payed month
-> Average per month
'''

class Store:
    def __init__(self, size: float, sales_month: float, item_categories: int, off_license: bool, item_list: list) -> None:
        self.size = size
        self.sales_month = sales_month
        self.item_categories = item_categories
        self.off_license = off_license
        self.sales_track = [sales_month]
        self.item_list = item_list 
    
    def update_monthly(self, value:float) -> None:
        self.sales_track.append(value)
        self.sales_month = value
    
    def add_item(self, item:str) -> None:
        self.item_list.append(item)
    
    def get_items(self):
        print(self.item_list)

    def max_sales(self):
        return max(self.sales_track)
    
    def min_sales(self):
        return min(self.sales_track)
    
    def avg_sales(self):
        return sum(self.sales_track) / len(self.sales_track)

    def __repr__(self):
        return f'Store size: {self.size} ¦ Sales of the month: {self.sales_month} ¦ Different category count: {self.item_categories} ¦ Off license: {self.off_license}'
    

