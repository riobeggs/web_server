# web_server

This web server is based on a person's data (first name, last name, DOB) which handles user inputs as C.R.U.D operations on a database where the personal data is stored. To access the relative database operation page, the user can click one of the available buttons (Create, Read, Update, Delete). Once data has been input by the user, the data and relative C.R.U.D operation is used to operate on the database. To view the success of an operation, the user can click 'Read' to view the changes made.


## Installation
Download postgreSQL [here](https://www.postgresql.org/download/) if not downloaded already.

```bash
git clone https://github.com/riobeggs/web_server.git
```
```bash
pip install requirements.txt
```
```bash
python3 database_config.py 
```
```bash
python3 app.py 
```
[View web server in browser.](http://127.0.0.1:5000)


## Usage (example)
![1](readme_images/1.jpg?raw=true)

I click the 'READ' button to view current existing data in the database. In my case, I have already stored data for the person: Rio Beggs.
![2](readme_images/2.jpg?raw=true)

I return to the home page and click the 'DELETE' button, enter the data I wish to delete, then hit submit.
![3](readme_images/3.jpg?raw=true)

To check that the data has been successfully deleted, I return to the home page and click the 'READ' button again. No data for Rio Beggs is stored in the table so I can confirm that my data has been deleted from the database.
![4](readme_images/4.jpg?raw=true)

I return to the home page and click the 'CREATE' button. I input some test data which will be created and added to the database.
![5](readme_images/5.jpg?raw=true)

I return to the data viewing page by clicking the 'READ' button on the home page. I can see that my test data has been successfully created and added to the database.
![6](readme_images/6.jpg?raw=true)

I return home and click the 'UPDATE' button because I decide to change my test data. I input some new data which will replace the original selected data. 
![7](readme_images/7.jpg?raw=true)

To confirm the update of my data I return to the data viewing page. I can see that my test data has been successfully updated.
![8](readme_images/8.jpg?raw=true)
