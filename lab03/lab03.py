import urllib.request
import unittest
from typing import TypeVar, Callable, List

T = TypeVar('T')
S = TypeVar('S')

class Student():
    """Custom class to test generic sorting and searching."""
    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.name == other.name

#################################################################################
# EXERCISE 1
#################################################################################
def mysort(lst: List[T], compare: Callable[[T, T], int]) -> List[T]:      
    """
    This method should sort input list lst of elements of some type T.

    Elements of the list are compared using function compare that takes two
    elements of type T as input and returns -1 if the left is smaller than the
    right element, 1 if the left is larger than the right, and 0 if the two
    elements are equal.
    
    mysort accepts a list called list with elements of type T in it and a 
    lambda function compare. Compare compares two elements of type T and returns an
    integer indicating their relationship.
    """
    for i in range(1, len(lst)): #Insertion sort. Inserts elements into premade, sorted lists. Steps up by 1 each time
        for j in range(i, 0, -1): #goes from i backwards in order to put i into the right spot
            a = compare(lst[j-1], lst[j]) #comparing j and the element less than it
            if a != -1: #if it isnt -1, meaning the left is NOT smaller then the right, swap the two elements :)     
               lst[j - 1], lst[j] = lst[j], lst[j - 1]
            else:       #otherwise, the loop can be broken out of because everything is in place
                break
    return lst

def mybinsearch(lst: List[T], elem: S, compare: Callable[[T, S], int]) -> int:
    """
    This method search for elem in lst using binary search.

    The elements of lst are compared using function compare. Returns the
    position of the first (leftmost) match for elem in lst. If elem does not
    exist in lst, then return -1.

    mybinsearch will accept a list object named lst, an element S that itll search for,
    and a lambda function that will compare another element T to S to see if it is higher
    or lower. mybinsearch is O(log n) 
    """
    low = 0
    high = len(lst) - 1 
    while(low <= high):                 #while the low index is still lower than the high index
        mid = (high + low)//2           #taking average of low and high to get the middle of the leftover indices to check
        a = compare(lst[mid], elem)     #compare the element in the middle to the one we are searching for
        if a == 0:                      #if equal, return the current middle index
            return mid
        elif a == 1:                    #if a == 1 then the current element is larger than key elem
            high = mid - 1 
        elif a == -1:                   #if a == -1 then the current element is smaller than key elem
            low = mid + 1
    return -1                           #return -1 if the key is not in the list at all


# 30 Points (total)
def test1():
    """Tests for generic sorting and binary search."""
    print(80 * "#" + "\nTests for generic sorting and binary search.")
    test1_1()
    test1_2()
    test1_3()
    test1_4()
    test1_5()

# 6 Points
def test1_1():
    """Sort ints."""
    print("\t-sort ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(sortedints, [2, 3, 4, 7, 9, 10])

# 6 Points
def test1_2():
    """Sort strings based on their last character."""
    print("\t-sort strings on their last character")
    tc = unittest.TestCase()
    strs = [ 'abcd', 'aacz',  'zasa' ]
    suffixcmp = lambda x,y: 0 if x[-1] == y[-1] else (-1 if x[-1] < y[-1] else 1)
    sortedstrs = mysort(strs,suffixcmp)
    tc.assertEqual(sortedstrs, [ 'zasa', 'abcd', 'aacz' ])

# 6 Points
def test1_3():
    """Sort students based on their GPA."""
    print("\t-sort students on their GPA.")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    sortedstudents = mysort(students, lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1))
    expected = [ Student('Angela', 2.5), Student('Josh', 3.0), Student('Jia',  3.5), Student('Vinesh', 3.8) ]
    tc.assertEqual(sortedstudents, expected)

# 6 Points
def test1_4():
    """Binary search for ints."""
    print("\t-binsearch ints")
    tc = unittest.TestCase()
    ints = [ 4, 3, 7, 10, 9, 2 ]
    intcmp = lambda x,y:  0 if x == y else (-1 if x < y else 1)
    sortedints = mysort(ints, intcmp)
    tc.assertEqual(mybinsearch(sortedints, 3, intcmp), 1)
    tc.assertEqual(mybinsearch(sortedints, 10, intcmp), 5)
    tc.assertEqual(mybinsearch(sortedints, 11, intcmp), -1)

# 6 Points
def test1_5():
    """Binary search for students by gpa."""
    print("\t-binsearch students")
    tc = unittest.TestCase()
    students = [ Student('Josh', 3.0), Student('Angela', 2.5), Student('Vinesh', 3.8),  Student('Jia',  3.5) ]
    stcmp = lambda x,y: 0 if x.gpa == y.gpa else (-1 if x.gpa < y.gpa else 1)
    stbincmp = lambda x,y: 0 if x.gpa == y else (-1 if x.gpa < y else 1)
    sortedstudents = mysort(students, stcmp)
    tc.assertEqual(mybinsearch(sortedstudents, 3.5, stbincmp), 2)
    tc.assertEqual(mybinsearch(sortedstudents, 3.7, stbincmp), -1)

#################################################################################
# EXERCISE 2
#################################################################################
class PrefixSearcher():

    def __init__(self, document, k):
        """
        Initializes a prefix searcher using a document and a maximum
        search string length k.
        """
        self.n = k                             #our maximum search string length
        self.doc = []                          #stored document that'll contain the array of substrings in the doc of max length k
        for i in range(0, len(document)):      #iterate through the whole document
            a = min(i + k, len(document))      #the end index will be whichever index is smaller: the index k larger than our current, or the last doc index
            self.doc.append(document[i:a])     #go from current index to either k or end of document (allows strings shorter than k toward the end)
        

    def search(self, q):                       #just a .contains() method, not even a search method
        """
        Return true if the document contains search string q (of

        length up to n). If q is longer than n, then raise an
        Exception.
        """
        if len(q) > self.n:                         #if the string is longer then the specified maximum string length, raise exception
            raise Exception("String is too long")   
        else:
            for strings in self.doc:                #iterates through whole list until finding the one that is equal to it.
                if strings[0:len(q)] == q:          #[0:len(q)] is there so that the equality can be accurate and not skewed by the length variation
                    return True
            return False                            #if never found, return false

# 30 Points
def test2():
    print("#" * 80 + "\nSearch for substrings up to length n")
    test2_1()
    test2_2()

# 15Points
def test2_1():
    print("\t-search in hello world")
    tc = unittest.TestCase()
    p = PrefixSearcher("Hello World!", 1)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("e"))
    tc.assertFalse(p.search("h"))
    tc.assertFalse(p.search("Z"))
    tc.assertFalse(p.search("Y"))
    p = PrefixSearcher("Hello World!", 2)
    tc.assertTrue(p.search("l"))
    tc.assertTrue(p.search("ll"))
    tc.assertFalse(p.search("lW"))

# 20 Points
def test2_2():
    print("\t-search in Moby Dick")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    p = PrefixSearcher(md_text[0:1000],4)
    tc.assertTrue(p.search("Moby"))
    tc.assertTrue(p.search("Dick"))

#################################################################################
# EXERCISE 3
#################################################################################
class SuffixArray():

    def __init__(self, document: str):
        """
        Creates a suffix array for document (a string).
        """
        self.suffixArray = []
        for i in range(len(document)):
            self.suffixArray.append(document[i:]) #creating all possible suffixes
        self.comparator1 = lambda x,y:  0 if x == y else (-1 if x < y else 1)
        self.comparator = lambda x,y:  0 if x[0: len(y)] == y[0: len(y)] else (-1 if x[0: len(y)] < y[0: len(y)] else 1)
        self.suffixArray = mysort(self.suffixArray, self.comparator1) #sorting all of the suffixes

    def positions(self, searchstr: str): #only returns indices in the suffix array and not the actual doc... but you could check that with the length of the substring im sure! 
        """
        Returns all the positions of searchstr in the documented indexed by the suffix array.
        """
        final = []
        posns = []
        for i in range(len(self.suffixArray)): #cuts down the length of the suffix array to that of the search string
            a = self.suffixArray[i]
            final.append(a[:len(searchstr)])
        index = mybinsearch(final, searchstr, self.comparator) #binary searches for search string
        if index != -1 : #backtracks to ensure the first occurance is returned
            a = index
            while(final[a - 1] == searchstr):
                a -= 1
            posns.append(a)
            print(posns)
        return posns
        

    def contains(self, searchstr: str): 
        """
        Returns true if searchstr is contained in document.
        """
        a = self.positions(searchstr)  #retrieves positions of the searchstr
        if a == []:                    #if searchstr returns no positions, print false
            return False
        else:
            print(a)
            return True

# 40 Points
def test3():
    """Test suffix arrays."""
    print(80 * "#" + "\nTest suffix arrays.")
    test3_1()
    test3_2()


# 20 Points
def test3_1():
    print("\t-suffixarray on Hello World!")
    tc = unittest.TestCase()
    s = SuffixArray("Hello World!")
    tc.assertTrue(s.contains("l"))
    tc.assertTrue(s.contains("e"))
    tc.assertFalse(s.contains("h"))
    tc.assertFalse(s.contains("Z"))
    tc.assertFalse(s.contains("Y"))
    tc.assertTrue(s.contains("ello Wo"))


# 20 Points
def test3_2():
    print("\t-suffixarray on Moby Dick!")
    tc = unittest.TestCase()
    md_url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
    md_text = urllib.request.urlopen(md_url).read().decode()
    s = SuffixArray(md_text[0:1000])
    tc.assertTrue(s.contains("Moby Dick"))
    tc.assertTrue(s.contains("Herman Melville"))
    tc.assertEqual(s.positions("Moby Dick"), [427])


#################################################################################
# TEST CASES
#################################################################################
def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
