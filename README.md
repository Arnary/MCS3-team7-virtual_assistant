# Virtual Assistant  

**Virtual Assistant** is a Python application which allows user to add/edit/remove its own **Contacts** and **Notes**. After **Contact** or **Note** was added, user can find them in the book using search by all available fields.

**Contact** entry includes next fields:
- Name - **required**
- Phone - one record can have several phone numbers
- Address
- Email
- Birthday
- Tags - one record can have several tags

**Note** entry includes next fields:
- Name - **required**
- Body

## Installation

To enjoy all the application features additional you need to install additional packages: 

```python
pip install -r requirements.txt  
mac:  
pip3 install -r requirements.txt
```

## Usage

**Virtual Assistant** is a console application. Type next commands in the console to interact with program, add your entries, modify and search them    

| Command| Description|
| ------ | ---------- |
|**hello**|returns _"How can I help you?"_
|**add 'name' 'phone number'**|creates customer record with **name** and **phone number**
|**delete-contact 'name'**|deletes contact with mentioned **name**
|**change 'name' 'old phone number' 'new phone number'**|updates phone number for the selected contact with **name** 
|**phone 'name'**|shows all phone numbers for the selected contact with **name** 
|**delete-phone 'name' 'phone number'**|deletes phone number for the selected contact with **name** 
|**add-birthday 'name' 'birthday in format DD.MM.YYYY'**|adds birthday date for the selected contact with **name** 
|**show-birthday 'name'**|shows birthday date for the selected contact with **name** 
|**birthdays 'date range'**|shows birthday guys in next **date range** days
|**all**| - shows all stored contacts
|**add-email 'name'**|adds email for the selected contact with **name** 
|**delete-email 'name'**|deletes email for the selected contact with **name** 
|**exit** or **close**|saves all work results into the file and exits application
|**add-note 'title' 'body'**|creates new **Note** with mentioned **'title'** and **'body'**
|**show-notes**| shows all available **Notes**
|**add-tags 'title' 'tags'**|adds tags to the **Note** with **'title'**. One **Note** can have several **'tags'**
|**search-by-tags 'tags'**|shows all **Notes** that contain mentioned **'tags'**. Several **'tags'** can be used for search simultaneously.
|**delete-note 'title'**|deletes **Note** with **'title'**
|**help**|returns the list with all available commands
  

## Contributing  

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
TimSim (Oleksandr Zharuk, Oksana Zakharevych, Anatolii Bezkrovnyi, Yevhen Zakharevych, Anastasia Dushka)