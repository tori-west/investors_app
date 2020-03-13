# investors_app
Django framework used to create a Python stocks and bonds application.

This program utilizes the Django framework with Python to create a web application. The application has three pages including two table displays of the investor’s stocks and bonds, a form to add stocks to the database and table, and a form to add new bonds to the database and table. Ideally a user login page will be added in the future, but currently only stocks and bonds for investor Bob Smith can be added. 

On the index.py, or Investor Tracking page, the original eight stocks are displayed including columns for the stock symbol, number of shares, purchase price, current price, and purchase date. Below the table is a link that says, ‘Add a New Stock.’ This link takes the user to the second page (which can also be reached in the navigation bar). Below the link is the bond table which lists only the one bond for Bob Smith. This table includes the same columns as the stock table with the addition of the bond coupon and bond yield. Below the bond table is a link to the third page called Bond Form. 

The second page is called Stock Form. This page contains a form for entering new stocks. The user enters in their investor ID number, stock symbol, number of stocks, purchase price, current price, and date they purchased the new stocks. At the bottom of the page is a button named ‘Add Stock.’ When the button is selected it adds the new stock to the database, and automatically takes the user back to the Investor Tracking page. 

The third page, titled Bond Form, does the same thing as the Stock Form page except for bonds. The user will enter the information into the form and click the ‘Add Bond’ button. The new bond information will be added to the database’s bond_table, and automatically send the user to the Investor Tracking page. 

Each page was mortified with Bootstrap3 through Django. A base.html page was created to hold the head HTML tags (including meta data, title, and bootstrap css and js), navigation bar, and heading 1.
