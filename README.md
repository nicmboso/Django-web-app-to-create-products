# Django-web-app-to-create-products
A Django web application about products:

Features:
To create products to save in database.
To view products which are rendered from the database.
To search for products by title.

Fields on the application:
• Title
• Category
• Price
• Quantity
• In stock (true/false)

Explanation:
The application consists of 3 sections as shown in snapshot below:
The “Search products” section is to search for products by title in the search box. When a product is searched for, the search opens a new webpage for the product details.
The “Product in stock” section lists the products in the database. The Title link opens the product details page. The delete link deletes a product from the webpage and the database, then redirects the app to remain on the homepage/products page.
The “Create Product” section creates a new product, saves it to the database and displays it on the page.

See Snapshots:
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/80d534a6-8888-420c-917a-cdb4a80be2d2)

1. The application has the ability to create products to save in database:
After clicking the add product button, the product gets added to the database.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/8d30a503-3850-48b6-8ee5-e37167aca6d7)

![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/f17ea430-c16e-4bc1-b29c-a3587e6d91b7)

2. Ability to view products which are rendered from the database:
   By clicking on the Title link of any of the products, a new page opens to show the details of the product clicked. Each product has an id as shown on each page URL.
   ![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/ee704ef9-ac6a-4ac0-899a-9cfffecd12fe)
   ![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/3c421c9a-f13e-45e7-99b8-7e1a0474ee03)
   ![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/f8763147-2574-414c-b49e-d3b60924c2c0)

3. Search products by title:
The search displays results if it exists or gives a no-found message if it does not.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/6e6e634f-eb21-4eae-85b8-b0e3a9d7e4d4)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/da22f1ac-3a1c-48a7-953e-ac268e27450d)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/88313076-9bfa-44d7-9aaf-45cf16805f3f)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/06ea02c9-a0c9-4669-aaa6-200962ff1421)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/f32c8cde-1bf4-44bf-97dc-59345cec3240)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/0236ec13-991e-4146-a730-b1d8c89abeb0)

The project involves GET and POST request-based views:
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/0fb12584-fcd3-4016-bb66-e1d7bd63d373)

Challenges encountered:
#1.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/fa1ab91d-8336-408e-99ca-b42aad209e47)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/77005aa6-06a8-4ef4-9bf3-e0fc3e2a918e)

Resolution: Resolved by changing occurrences of name=”title” to name=”Title” in products.html file.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/d07f5c19-93b6-4c47-943c-166b8582aed4)

#2.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/65f82fe4-1a81-45be-bf52-f3c78a02473e)

Resolution:
Resolved error by inputting True in the webpage form for In_stock field as this is a Boolean field.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/690f1be4-1378-4ba6-bf14-c5996a3dcc5b)

#3.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/0692e61a-30b5-4fa3-a504-0eabcfa0f92a)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/0f50f09a-d55c-4b18-a79c-1a361a89de23)

Resolution:
Traced my code to products.html file where I changed the occurrences of ‘delete_post’ to ‘delete_product’ in the file.

![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/a03748da-34dd-4d14-8cc9-17da9224c6d9)

#4.
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/ae739ab6-a73c-425d-8070-10a0cdc2331d)

Resolution:
Ensured my page route path match in url.py file match the anchor tag path in products.html file

![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/5feb3fdb-53f6-45e4-9107-99693aa1ad0a)
![image](https://github.com/nicmboso/Django-web-app-to-create-products/assets/160390032/0c1c5bfd-e569-46e3-93bd-5502bef5da4c)

Had some other errors too but could not regenerate them after resolution while working on this project.

Supported lookup resources:
1.	url ref: https://www.makeuseof.com/add-search-functionality-to-django-apps/
2.	url ref: https://www.youtube.com/watch?v=AGtae4L5BbI

















