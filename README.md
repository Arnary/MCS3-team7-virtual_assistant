# Virtual Assistant  

**Virtual Assistant** is a Python application which allows user to add/edit/remove its own **Contacts** and **Notes**. After **Contact** or **Note** was added, user can find them in the book using search by all available fields.

**Contact** entry includes next fields:
- Name - **required**
- Phone - one record can have several phone numbers
- Address
- Email
- Birthday

**Note** entry includes next fields:
- Name - **required**
- Body
- Tags - one record can have several tags

## Getting Started

Clone this repo (for help see this [tutorial](https://docs.github.com/ru/repositories/creating-and-managing-repositories/cloning-a-repository)).

### Installation

To enjoy all the application features additional you need to install additional packages: 

```python
pip install -r requirements.txt
```

### Usage
```
python main.py
```

**Virtual Assistant** is a console application. Type next commands in the console to interact with program, add your entries, modify and search them.    

| Command| Description|
| ------ | ---------- |
|**hello**|returns _"How can I help you?"_
|**add 'name' 'phone number'**|creates customer record with **name** and **phone number**, also adds additional numbers when using the command for an already created contact
|**delete-contact 'name'**|deletes contact with mentioned **name**
|**change 'name' 'old phone number' 'new phone number'**|updates phone number for the selected contact with **name** 
|**phone 'name'**|shows all phone numbers for the selected contact with **name** 
|**delete-phone 'name' 'phone number'**|deletes phone number for the selected contact with **name** 
|**add-birthday 'name' 'birthday in format DD.MM.YYYY'**|adds birthday date for the selected contact with **name** 
|**show-birthday 'name'**|shows birthday date for the selected contact with **name** 
|**birthdays 'date range'**|shows birthday guys in next **date range** days
|**all**|shows all stored contacts
|**add-email 'name' 'email'**|adds email for the selected contact with **name** 
|**delete-email 'name'**|deletes email for the selected contact with **name** 
|**add-note 'title' 'body'**|creates new **Note** with mentioned **'title'** and **'body'**
|**show-notes**|shows all available **Notes**
|**add-tags 'title' 'tags'**|adds tags to the **Note** with **'title'**. One **Note** can have several **'tags'**
|**search-by-tags 'tags'**|shows all **Notes** that contain mentioned **'tags'**. Several **'tags'** can be used for search simultaneously.
|**delete-note 'title'**|deletes **Note** with **'title'**
|**delete-birthday 'name'**|deletes birthday for the selected contact with **name** 
|**add-address 'name' 'address'**|adds address for the selected contact with **name** 
|**delete-address 'name'**|deletes address for the selected contact with **name**
|**search 'two or more characters to search for'**|searches all matches in **contacts**
|**search-note 'two or more characters to search for'**|searches all matches in **Notes**
|**help**|returns the list with all available commands
|**exit** or **close**|saves all work results into the file and exits application

All "add" commands can overwrite the content of a contact or note if used on an already created record, except "add-tags" and "add" - they add an additional tag and phone number to the note and contact respectively. 

## Project Contents
```
├── virtual_assistant         <- Code for use in this project.
│   ├── address_book.py       <- Classes and methods for Address Book.
│   ├── bot_book_commands.py  <- Functions for all bot commands for Address Book.
│   ├── bot_note_commands.py  <- Functions for all bot commands for Notes.
│   ├── dynamic_completer.py  <- Class for working with the dynamic completer.
│   ├── errors.py             <- Decorator function and Exceptions.
│   ├── main.py               <- Code to run the bot.
│   └── note.py               <- Classes and methods for Notes.
│
├── .gitignore                <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if needed.
├── README.md                 <- The top-level README for developers using this project.
└── requirements.txt          <- The requirements file for reproducing the environment.
```
## Contributed 

[Anastasiia Dushka](https://github.com/Arnary), [Oleksandr Zharuk](https://github.com/zharuk-alex), [Yevhen Zakharevych](https://github.com/yevhen-zakharevych), [Oksana Habbasova](https://github.com/oksana-habbasova), [Anatolii Bezkrovnyi](https://github.com/Anatoliy-Bezkrovnyi)
