books=["book1","book2","book3"]
good_books=0

for book in books:
    
    page_numebr=int(input("No of pages: "))
    if page_numebr>=80:
        good_books+=1

print(good_books)