# Fullstack Development Milestone Project – 'Teff' E-commerce

# Context

This project focuses on the full-stack development for a mobile-responsive web-based e-commerce website called ‘Teff’. 'Teff' is an online purveyor of elecletic books and offers an interesting range of good reads for their patrons. 

The website has a login feature and requires users to create an account before they are able to check out items for purchase. 

# Demo
The e-commerce website can be found here: 
The website has been deployed successfully on heroku but currently has a couple of bugs and features that are not working. The source code, however, is available for inspection. 

# Index
1. UX
2. Technologies Used
3. Future Features To Implement
4. Testing
5. Deployment
6. Credits and Acknoledgement

# 1. User Experience (UX)
#### (i) Project Strategy

| User Stories| Features|
| ------ | ------ |
| User wants to register an account to save their checkout list and credit card details.| User Login and Authentication.|
| User wants to browse t-shirts by size, color, price and items on sale.| Navbar with product filters and Products Page.|
| User wants to view product details and photographs in a stand-alone page.| Product Detail Page.|
| User wants to review number of products selected for checkout and the total price before payment.| Checkout Page (Cart).|
| User wants to make payment using debit/credit for checked out items.| Stripe Payment Gateway.|
| Admin wants to populate details for new t-shirt launch on the website.| Able to upload t-shirt image through UploadCare.|
| Admin wants to update t-shirt inventory on the website.| Automatic update of stock count when a t-shirt is sold.|

# 2. Technologies Used
* [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
<br> The project uses HTML5 to structure the content of the website.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
<br> The project uses CSS to add stylistic touches to the website.
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
<br> The project uses Bootstrap to structure the layout of the website (i.e. Navbar, Footer) and ensure website is mobile responsiveness.
* [Django](https://flask.palletsprojects.com/en/1.1.x/)
<br> The project uses the Django python Web framework to develop the e-commerce website. 
* [Jinja 2](https://jinja.palletsprojects.com/en/2.10.x/)
<br> The project uses Jinja2 to write conditional statements to display content blocks when  certain conditions are met. Additionally, Jinja2 was used to set up template inherritance and extension of html/css files for the project.
<br> The project uses MongoDB Atlas as a cloud database to store user data and file uploads.
* [GoogleFonts](https://fonts.google.com/)
<br> The project uses GoogleFonts to style the typography on the website to enhance the visual experience of users.  
* [FontAwesome 4.7](https://fontawesome.com/v4.7.0/)
<br> The project uses the icons provided by FontAwesome 4.7 alongside call-to-action buttons to enhance the user experience by making user interaction with the application more intuitive. 
* [UploadCare](https://uploadcare.com/) 
<br> The project uses UploadCare to handle the storage and uploads of product photos. As UploadCare is a 'Service as a Product' platform, they provide scalable services should there be an increased traffic to the Teff web-application or should there be a need to increase storage for product image uploads.
* [Heroku](https://www.heroku.com/) 
<br> The project uses Heroku for the deployment and management of the web application. As Heroku provides timelogs, when an error occurs, it makes easier to identity and remedy bugs.  

# 3. Future Features To Implement
| Number| Future Features.|
| ------ | ------ |
| 1.| Customised Checkout page for customer to key in their credit card details.|
| 2.| Teff web application is able to send automated emails to customers (e.g. when a customer registers an account, when a customer makes a purchase, when a customer requests for promotional emails, etc.)|
| 3.| Dashboard for administator to track customer orders, customer issues and total revenue generated.|

# 4. Testing

Django Admin Account
ID: user
Password: password

1. Admin is able to create/edit/delete entries on the categorys.
2. Admin is able to create/edit/delete entries on the items.
3. Admin is able to create/edit/delete entries on the inventorys.
4. Admin is able to create/edit/delete entries on the sizes.
5. Admin is able to create/edit/delete entries on the tags.
6. User is able to create an account and login.
7. User is able update account information

# 5. Deployment
#### (i) Development Process
- All codes was written on Visual Studio code and codes were saved and tested locally. 
- Regular committing and pushing of codes to GitHub ensured that changes to codes can be tracked and allows for version control maintainence.
- Heroku was set up first before embarking on code development.   

# 6. Credits and Acknowledgement
- The website template was adapted from https://colorlib.com/
