import urllib
import pip._vendor.requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(bookurl = 'https://www.gutenberg.org/files/84/84-0.txt'):
    return BETTERradix_sort(book_to_words(bookurl))


def BETTERradix_sort(strin):
    arr = strin
    index = len(max(arr, key=len))
    #index *= -1
    sortedArr = BETTERiteration(arr, index - 1, -1)

    print("RESULT: " + str(sortedArr))
    return sortedArr

def BETTERiteration(arr, i, max):
    print("I " + str(i))
    if i == max:
        return arr
    doubleArr = [[None for x in range(1)] for y in range(256)]
    print(str(doubleArr))
    for a in arr:
        key = 0
        try:
            key = a[i]
        except:
            key = 0
        #print("KEY: " + str(key))
        doubleArr[key].append(a)
        
    
    result = []

    for bucket in doubleArr:
        if bucket != [None]:
            for key in bucket:
                if key == None:
                    continue
                result.append(key)
    print(str(result))

    return BETTERiteration(result, i - 1, max)

if __name__ == "__main__":
    x = "Those of you who want to download our Etexts before announcment can surf to them as follows, and just download by date; this is also a good way to get them instantly upon announcement, as the indexes our cataloguers produce obviously take a while after an announcement goes out in the Project Gutenberg Newsletter."
    xy = [ b'aaa', b'!ccc', b'c', b'bbb' ]
    print("starting")
    book = "https://www.gutenberg.org/files/32572/32572-0.txt"
    a = radix_a_book(book)
    print("done w a")
    b = sorted(book_to_words(book))
    print("2: " + str(a[2]) + " " + str(b[2]))
    print("12: " + str(a[12]) + " " + str(b[12]))
    print("100: " + str(a[100]) + " " + str(b[100]))
    print("352: " + str(a[352]) + " " + str(b[352]))
    print("-1: " + str(a[-1]) + " " + str(b[-1]))
    print(a == b)
    