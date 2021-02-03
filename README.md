# hacker_news_scraper

The purpose of this program is to allow individuals to check whether or not a password has been hacked to help in determining if the individual might want to use the password for an account.

Made with Python version 3.9.1

**IMPORTANT: To ensure no issues, use Python 3.9.1 or newer.
This is intended for personal use, but it may be used for greater uses if an individual wants to do so.**

NOTICE: Do not use this project maliciously, you are responsible for your actions when using web scrapers so use this as it was intended to, which is to grab *x* (default first 4) amount of pages of news stories that have 100 or more likes on them. (From https://news.ycombinator.com/news)

# Installation/Setup

If you know how, get the files into a folder, make it a virtual environment, and install dependencies using requirements.txt.

Otherwise: 

#### Step 1: 
Get all of the files in a separate folder on your machine.

#### Step 2: 
Make the folder you have stored only the files obtained from this project a virtual envrionment.

From the command prompt for windows users:

```sh
$ python3 -m venv <path_folder_whereof_files>
```
or
>try using 
py to replace python3 depending on the alias that is on the machine.

From the terminal:
```sh
$ python3 -m venv <path_folder_whereof_files>
```
or
>try using python or py to replace python3 depending on the alias that is on the machine.

#### Step 3: 
Activate the virtual environment.
Replace venv with the folder like in the previous steps that use <path_folder_whereof_files>
```sh
$ ./<venv>/Scripts/activate
```
After you enter that correctly, you will notice added text besides the command line name, reading the virtual environment name, which should be the folder name if you've followed the steps.

#### Step 4: 
Install dependencies.
Using the *requirements.txt* file, install the dependencies listed.
Try the following command while in the folder:
```sh
(<venv>)$ pip3 install -r requirements.txt
```
Note: you may use pip as long as it uses python3.

# Usage
Assuming everything you get everything installed and setup correctly, whether through Pycharm or other means necessary, you may now use the program through the terminal or through a IDE, command prompt, etc.

#### Step 1:
Make sure you are in the folder with *scape.py* then start the function with the following command:

```sh
$ python3 scrape.txt
```

The output will look similar to:

```sh
[{'link': 'https://www.aboutamazon.com/news/company-news/email-from-jeff-bezos-to-employees',
  'title': 'Email from Jeff Bezos to employees',
  'votes': 1806},
 {'link': 'https://www.videolan.org/press/videolan-20.html',
  'title': 'VideoLAN is 20 years old today',
  'votes': 1326},
 {'link': 'https://carltheperson.com/posts/10-things-linux',
  'title': 'Getting better at Linux with mini-projects',
  'votes': 951},
...]
```

Using an IDE like Pycharm allows you to click the links verses command prompt of copy and pasting to a browser.

Now you can easily have the top stories without opening up a browser, typing in the hacker news url, and sifting through countless stories just to get to the best ones.

# Modifications

## Amount of Pages
This section explains how to set the amount of pages the program will sift through to get the top stories from the program.

In the main function:

```sh
def main():
    pprint.pprint(get_hacker_news(4))
```

You can change the *get_hacker_news(***4***)* arguement of ***4*** to be a number in the range of 1 to 18.

**IMPORTANT:**
I am strongly against setting it to anything greater than 6 due to the slight chance that it may cause a web server to lag so if you know about the time module please utilize it in order to stay in accordance to using this program ethically.

## Likes on Post
This section explains how to set the amount of likes a story must have in order to make it the final result when displaying the stories onto the screen.

In the create_custom_hn function):

```sh
def create_custom_hn(links, subtext):
    hn = []
    pts_bigger_than = **99**
```

Change the pts_bigger_than = **99** value to the desired amount of likes the post must be greater than.

For example if I set pts_bigger_than = 399
then post **greater but NOT equal to 399** would be displayed.

# Why

