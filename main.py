library = []

while True:
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. View All Books")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        title = input("Enter the book title: ").strip()
        author = input("Enter the author: ").strip()

        while True:
            year = input("Enter the year of publication: ").strip()
            if year.isdigit() and int(year) > 0:
                year = int(year)
                break
            else:
                print("Invalid year. Please enter a positive number.")

        while True:
            copies = input("Enter the number of copies: ").strip()
            if copies.isdigit() and int(copies) >= 0:
                copies = int(copies)
                break
            else:
                print("Invalid number of copies. Please enter a non-negative number.")

        for book in library:
            if book['title'].lower() == title.lower():
                book['copies_available'] += copies
                print(f"Updated the number of copies for '{title}'.")
                break
        else:
            newBook = {
                'title': title,
                'author': author,
                'year': year,
                'copies_available': copies
            }
            library.append(newBook)
            print(f"Added '{title}' to the library.")

    elif choice == '2':
        title = input("Enter the book title to search: ").strip()
        for book in library:
            if book['title'].lower() == title.lower():
                print(f"Title: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nCopies Available: {book['copies_available']}")
                break
        else:
            print("The book was not found.")

    elif choice == '3':
        title = input("Enter the book title to borrow: ").strip()
        for book in library:
            if book['title'].lower() == title.lower():
                if book['copies_available'] > 0:
                    book['copies_available'] -= 1
                    print(f"You have successfully borrowed '{title}'.")
                else:
                    print(f"'{title}' is currently unavailable.")
                break
        else:
            print("The book was not found.")

    elif choice == '4':
        title = input("Enter the book title to return: ").strip()
        for book in library:
            if book['title'].lower() == title.lower():
                book['copies_available'] += 1
                print(f"You have successfully returned '{title}'.")
                break
        else:
            print("The book was not found.")

    elif choice == '5':
        if not library:
            print("No books in the library.")
        else:
            print(f"{'Title':<20} {'Author':<20} {'Year':<6} {'Copies':<7}")
            print("-" * 65)
            for book in library:
                print(f"{book['title']:<30} {book['author']:<20} {book['year']:<6} {book['copies_available']:<7}")

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
