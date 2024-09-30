# CCCS 106 - ADET (BSCS 3B)

**This is a submission page for CCCS 106 - Applications Development of BSCS 3B.**

## PS1

1. Write a Flask app displaying "HELLO WORLD".
2. Submit the app files by pushing and sending pull request. Folder name is
   PS1 under your folder name.
3. Set up a new Python project.
4. Create a basic Flask app:
   • Write a Python file to define your Flask application.
   • Import necessary modules.
   • Create a Flask app instance.
   • Define a route for the home page.
5. Create a template: Create an HTML file to display the initial content "Hello, World!"
6. Add a Form and Personalized Greeting:
   1. Modify the template: Add a form with a name input field.
   2. Create a route to handle the form:
      • Define a route to process the form submission.
      • Retrieve the entered name.
      • Return the greeting message "Hello World! ‹Name>, welcome to CCCS 106 - Applications Development and Emerging Technologies".
7. Submit the App:
   1. Organize your files: Place your Python file and template in a specified directory. Folder name is PS1 under your folder name.
   2. Push to your Git repository
   3. Create a pull request

## PS2

1. Modify the code for PS1 by creating a registration form with Boostrap.
2. Registration form should contain the following information:
   * First Name
   * Middle Name
   * Last Name
   * Contact Number
   * Email Address
   * Address
3. Input must be saved into a JSON file.
4. Submit the App:
   * Organize your files: Place your Python file and template in a specified directory. Folder name is PS2 under your folder name.
   * Push to your Git repository
   * Create a pull request

## PS3

1. Modify the code for PS2 by saving the input from registration form to a MySQL database.
2. Database Info:
   * Database Name: adet
   * Table Name: adet_user
3. Submit the App:
   * Organize your files: Place your Python file and template in a specified directory. Folder name is PS3 under your folder name.
   * Push to your Git repository
   * Create a pull request

## PS4

* Modify the code for PS3 by modifying the registration form (sign-up). Add a password field, that when being saved it must be encrypted using sha-256 encryption.
* Add a login page by asking for a username and password. Use session to control the access to every page.

  * When successfully logged in, user must be redirected to a Dashboard.
  * If not logged in, prevent the user access to the Dashboard. The user must be redirected to login page.
* Create a simple Dashboard with a message:

  * Hello, First Name and below this should be a table containing the user details except the password.
* Submit the App:

  * Organize your files: Place your Python file and template in a specified directory. Folder name is PS4 under your folder name.
  * Push to your Git repository
  * Create a pull request
