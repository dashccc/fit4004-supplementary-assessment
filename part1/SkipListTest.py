'''
Created on 3 Aug 2016

@author: Wanyu Yin
@student_id: 24141232
@version: Python 2.7
'''
from mock import patch
import unittest
from skiplist import SkipList

class SkipListTest(unittest.TestCase):
    def setUp(self):
        '''
        Basic setup for the unittest module.
        '''
        self.skiplist = SkipList(4) #Generate a maxlevel 2 ordered map
        self.aNode = [None, None, None, None]

    def test_makeNode(self):
        '''
        Test if the _makeNode method can generate the right list [None, None, None, None]
        '''
        self.assertEqual(self.aNode, self.skiplist._makeNode(0, None, None))
        
    def test_makeNode_notEqual(self):
        '''
        Test if the list [None, None, None] generated by _makeNode method is not equal to list [None, None, None, None]
        '''
        self.assertNotEqual(self.aNode, self.skiplist._makeNode(-1, None, None))
    
    @patch('random.random')
    def test_randomLevel(self, mock_rand):
        '''
        Test when random mock result is 0, the return value by _randomLevel is 1
        '''
        mock_rand.return_value = 0
        self.assertEqual(1, self.skiplist._randomLevel())
        
    @patch('random.random')
    def test_randomLevel_notEqual(self, mock_rand):
        '''
        Test when random mock result is 0, the return value 1 by _randomLevel is not equal to 0
        '''
        mock_rand.return_value = 0
        self.assertNotEqual(0, self.skiplist._randomLevel())
        
    def test_findLess(self):
        '''
        Test when given the searchKey, the _findLess method returns the part of the array which contains the searched item
        '''
        self.skiplist.head = [1,[3,4],[5,6],[7,8,[None,0]]]
        result = self.skiplist._findLess(self.skiplist._update, 1)
        self.assertEqual([1, [3, 4], [5, 6], [7, 8, [None, 0]]], result)
       
    def test_items(self):
        '''
        Test when searchKey is not None (in this case is 1) and reverse is True,
        the method finds all the key value pairs in the ordered map
        '''
        test_array = []
        self.skiplist.head[3] = [1,2,3,[7,8,[None,9,10],[None,10,11]]]
        for item in self.skiplist.items(1, False):
            test_array.append(item)
        self.assertEqual([(1, 2), (7, 8)], test_array)
        
    def test_items_found3_is_nil(self):
        '''
        Test when the self._foundLess return the save object as self.skiplist.nil.
        The value of searchKey is 1 and reverse is False, but the last item of self.skiplist.head is self.skiplist.nil
        In Python, "is not" only return False when the two comparing items is referring to the same object.
        '''
        test_array = []
        self.skiplist.head[3] = self.skiplist.nil
        for item in self.skiplist.items(1, False):
            test_array.append(item)
        self.assertEqual([], test_array)
         
    def test_items_reverse_true(self):
        '''
        Test when not given a searchKey (None) and reverse is True,
        node should be [None, None, None] because self.tail is [None, None, None]
        the generator should not be called and returns nothing.
        '''
        test_array = []
        for item in self.skiplist.items(None, True):
            test_array.append(item)
        self.assertEqual([], test_array)
    
    @patch('skiplist.SkipList._randomLevel')    
    def test_insert_has_searchKey(self, mock_randomLevel):
        '''
        Test when the searchKey exists (in this case it is 1), 
        the insert method can overwrite the value None into 100 or not
        '''
        mock_randomLevel.return_value = 1
        self.skiplist.head[3][0] = 1
        self.skiplist.insert(1, 100)
        self.assertEqual([1, 100, None], self.skiplist.head[3])
        
    @patch('skiplist.SkipList._randomLevel')
    def test_insert_no_searchKey(self, mock_randomLevel):
        '''
        Test when the searchKey does not exist (in this case it is 0),
        the insert method inserts the new value pair at index 3
        '''
        mock_randomLevel.return_value = 0
        self.skiplist.insert(0,100)
        self.assertEqual(0, self.skiplist.head[3][0])
        self.assertEqual(100, self.skiplist.head[3][1])
        
    @patch('skiplist.SkipList._randomLevel')
    def test_insert_node3_not_nil(self, mock_randomLevel):
        '''
        Test when the searchKey does not exist (in this case it is 0),
        the insert method inserts the new value pair at index 3
        also defining new head array makes node[3] is not the same as self.skiplist.nil
        '''
        self.skiplist.head[3] = [1,[3,4],[5,6],[7,8,[None,0]]]
        mock_randomLevel.return_value = 0
        self.skiplist.insert(0,100)
        self.assertEqual(0, self.skiplist.head[3][0])
        self.assertEqual(100, self.skiplist.head[3][1])
        
    def test_delete(self):
        '''
        Test when given searchKey, the method can successfully delete the searchKey and its value or not
        '''
        self.skiplist.head[3] = [7,8,[9,0],[10,11,12]]
        self.assertTrue(self.skiplist.delete(7))
        
    def test_delete_add_level(self):
        '''
        Test when the ordered map contains another inner ordered map, the delete method can work properly or not
        '''
        self.skiplist.level = 1  
        self.skiplist.head[3] = [7,8,9,[10,11,12,[13,14,15]]]
        self.assertTrue(self.skiplist.delete(10))
        
    def test_delete_node_tail(self):
        '''
        Test when there is only one ordered map in the list (where the tail is pointing at),
        deleting the searchKey (10 in this case) will cause the self.skiplist.tail changes correspondingly.
        '''
        self.skiplist.head = [7,8,9,[10,11,12,[13,14,15]]]
        self.skiplist.tail = self.skiplist.head[3]
        self.assertTrue(self.skiplist.delete(10))
        
    def test_delete_no_searchKey(self):
        '''
        Test if the searchKey does not exist, the method should return None
        '''
        self.assertIsNone(self.skiplist.delete(0))
        
    def test_search(self):
        '''
        Test if there exists the searchKey (7 in this case), the method will return the value 8 associated with key 7
        '''
        self.skiplist.head[3] = [1,[3,4],[5,6],[7,8,[9,0],[10,11,12]]]
        self.assertEqual(8, self.skiplist.search(7))
         
    def test_search_no_searchKey(self):
        '''
        Test if the searchKey cannot match, the method should return None
        '''
        self.assertIsNone(self.skiplist.search(0))

if __name__ == '__main__':
    unittest.main()        
