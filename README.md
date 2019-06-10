# Instagram_Bot
An Instagram Bot to follow users from a target page followers list. Made using selenium.

![Capture](https://user-images.githubusercontent.com/49119325/59167227-d68fc600-8b4d-11e9-950b-279b0eb04287.PNG)

## Features
1. Bot can identify between new user, requested user & following user and will only follow new users and ignore the rest.
2. Bot will always start a new fresh chrome window for each new session.
3. Bot can automatically input the ID & Password during login/every session.
4. Single Xpath can be used with inbuilt itrative variables to fit one Xpath for multiple followers.
5. Output for Each step, Itration count and follow count are printed in realtime in cmd during each session.

## Requirement
1. Python 2.7
2. pip
3. selenium
4. selenium chrome driver

#### How to Setup the requirements
** If you already have the required dependencies installed then you can skip this step

#### 1). Installing python & pip
Headover to https://www.python.org/downloads/release/python-2716/ to download python 2.7.
You can also download python 3.7 from https://www.python.org/downloads/release/python-373/

*Check the add to path option and install pip option when installing python.

#### 2). Installing selenium
You can easily install selenium using this simple command in command prompt.

```
pip install selenium

```
#### 3). Installing chrome driver
You need to check your chrome browser version for this by heading over to your browser window > Help > About Google Chrome.
and find the same version chrome driver at http://chromedriver.chromium.org/downloads .
Unzip the file and move to C drive create a folder there with name- chromedriver.

Right click on ThisPC in file explorer and go to properties > Advanced System Settings > Environment Variable 

Under system variable click on Path and Add a new entry to paths and input chrome driver's folder directory Address into the box.

#### All Set

## Getting started with Bot Code

All the basics you need to get the bot started can be entered in the starting section of the code which looks like this..

```
# The number of people you want to follow
follow_count= number of people to follow
# Login Email ID for Instagram
Login_Email = ("Insert EmailID here")
# Login Password for Instagram
Login_password = ("Insert password here")
# Link of the target page to follow users
Instapage_link = ("insert link here")

```

The bot requires few more inputs like Xpath of Followers list, User's in follow list, and follow button (ususally the follow button on Xpath doesnt need to be changed)

Xpath can be found out using this method -

1)- right click and inspect element the element you can want to get Xpath for -
![xpath 1](https://user-images.githubusercontent.com/49119325/59166059-8bbc8100-8b42-11e9-8a42-71fdfc5b2b6f.png)
and
reapeating the same once the inspet element dialoge is open, will point you to that specific element in the html code and you can copy the Xpath by right clicking the element in code- 
![xpath 3](https://user-images.githubusercontent.com/49119325/59166103-43ea2980-8b43-11e9-9991-d899ae8cb3f8.png)


Xpath for users can be found out using the same above mentioned method, for example this is the Xpath for first user in the follower's list -

```
/html/body/div[5]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[2]

```
and this for the second user in the list -

```
/html/body/div[5]/div/div[2]/ul/div/li[2]/div/div[1]/div[2]/div[2]


```
you can also short form them like 

```
//div/li[2]/div

```
and add the itration variable where the value changes between user to user in this case with "li".

```
//div/li["+itration_val+"]/div

```
#### Save the file..

## Using the Bot -

Navigate to the folder where the script is located and in the addres bar type- cmd 
to start command prompt with that directory

and type the script name- Instabot.py

## Result
Once the script finshes, it will print -"Task Finished Succesfully" with the number of people followed on the cmd terminal. like this - 

![Capture](https://user-images.githubusercontent.com/49119325/59167227-d68fc600-8b4d-11e9-950b-279b0eb04287.PNG)



