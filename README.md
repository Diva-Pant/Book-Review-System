# Book-Review-System

This is a book review application. It lets the user add reviews on the book they have read and rate them. The application also involves the functionality of adding and deleting their entries i.e reviews for a particular book.

This is how basic view looks like :
![basic view](https://user-images.githubusercontent.com/66238565/126047520-6d4dd584-74fc-49ca-aa0e-540e71c7c256.PNG)

Form to add review:

![adding review](https://user-images.githubusercontent.com/66238565/126047538-9fd836b7-edf1-4197-8e56-187179f437f0.PNG)

List of books reviewed:

![added reviews](https://user-images.githubusercontent.com/66238565/126047551-cf4e5ad8-2b6e-4aab-9c7e-4730ec6e6141.PNG)

Deleting reviews: 

![deleting reviews](https://user-images.githubusercontent.com/66238565/126047792-aa6db385-c741-4068-aa89-ff5361a30582.PNG)


Login Page:

![login page](https://user-images.githubusercontent.com/66238565/126047560-6b3d0cc9-8880-4daa-8bde-6b7baaa90e44.PNG)

Register Page:

![register page](https://user-images.githubusercontent.com/66238565/126047571-c18d6e12-7acb-40a3-acad-ad2d585ef0e9.PNG)


**Installation Steps:**
1. Add "book_review" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
       ...
       'book_review.apps.BookReviewConfig',
    ]

2. Include the book_review URLconf in your project urls.py like this::

    path('book_review/', include('book_review.urls')),

3. Run ``python manage.py migrate`` to create the book_review models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a user book review (you'll need the Admin app enabled).
   

5. Visit http://127.0.0.1:8000/book_review to add a book review.



