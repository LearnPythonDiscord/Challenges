import unittest
from unittest import mock

import challenges
class T100BeginnerTests(unittest.TestCase):
    """Tests for beginner challenge"""
    def setUp(self):
        self.store1 = challenges.Store(222.2,33333.3,3,True,['item1','item2','item3'])
    def test_101_variables(self):
        '''Check init is correct'''
        self.assertEqual(self.store1.size, 222.2)
        self.assertEqual(self.store1.item_list, ['item1','item2','item3'])
        self.assertEqual(self.store1.off_license, True)

class T200IntermediateTests(unittest.TestCase):
    '''Test for intermediate challenges'''
    def setUp(self):
        self.store1 = challenges.Store(222.2,33333.3,3,True,['item1','item2','item3'])
        self.store2 = challenges.Store(232323.3232,32323.3,5,False,['choco','beer','crisps'])
    
    def test_201_store_str(self):
        '''Check the store object prints correctly'''
        expected = 'Store size: 232323.3232 ¦ Sales of the month: 32323.3 ¦ Different category count: 5 ¦ Off license: False'
        self.assertEqual(repr(self.store2),expected)

    def test_202_update_sales(self):
        '''Check the update sales method'''
        self.store1.update_monthly(123.4)
        self.assertEqual(self.store1.sales_month, 123.4)

    def test_203_update_items(self):
        '''Check the update items method'''
        self.store1.add_item('wine')
        self.assertEqual(self.store1.item_list,['choco','beer','crisps','wine'])
    
class T300AdvancedTests(unittest.TestCase):
    '''Check for advanced tests'''
    def setUp(self):
        self.store1 = challenges.Store(222.2,33333.3,3,True,['item1','item2','item3'])
        self.store1.update_monthly(900000.0)
        self.store1.update_monthly(1.0)
        self.store1.update_monthly(3298.0)
        self.store1.update_monthly(3.0)
    def test_301_get_max(self):
        '''Check the max_sales method'''
        self.assertEqual(self.store1.max_sales(),900000.0)
    
    def test_302_get_min(self):
        '''Check the min_sales method'''
        self.assertEqual(self.store1.min_sales(), 1.0)
    
    def test_303_get_avg(self):
        '''Check the avg_sales method'''
        self.assertEqual(self.store1.avg_sales(), 225825.5)

