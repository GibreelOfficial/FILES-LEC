books=["one","two","three"]

book_pass=0

for book in books:
    page_count=int(input(f"Enter page number for book {book}: "))

    if page_count>100:

        book_pass+=1

print(f"The number of good books is {book_pass}")