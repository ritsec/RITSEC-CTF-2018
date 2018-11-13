# 2018

<<<<<<< Updated upstream
# RITSec Compeititon / Infra Tasks
## Infrastructure Needed For Challenges
- Crypto-150
## TODO 9/17/2018
### CTF
- CTFd Plugins
    - Resume collection at signin
    - Finding the user that solved a challenge (Only shows team by default)
        - Should be an administrative view
    - Programming Challenges
        - Premium CTFd has this built in
        - Potentially have CI checks that runs the code and then if the checks are passed, the code is reviewed by an admin
        - C, Python, bash
=======
# Challenge Summary

## Crypto

### 150
Name: CictroHash  
Author: Cictrone  
Type: File & server  

#### Prompt
See the attached PDF for an amazing new Cryptographic Hash Function
called CictroHash. For this challenge you must implement the
described Hash Function and then find a collision of two strings.
Once a collision is found send both strings to {{INSERT_SERVER}}
as a HTTP POST request like below:

curl -X POST http://{{INSERT_SERVER}}/checkCollision \
--header "Content-Type: application/json" \
--data '{"str1": "{{INSERT_STR1}}", "str2": "{{INSERT_STR2}}"}'

If the strings are a valid collision then the flag will be returned.

### 300
Name: The Proof is in the Pudding  
Author: Cictrone  
Type: File  

#### Prompt
_None_

### 500
Name: DarkPearAI  
Author: Cictrone  
Type: File  

#### Prompt
3:371781196966866977144706219746579136461491261

Person1: applepearblue
Person2: darkhorseai

What is their secret key?
(Submit like RC{KEY_GOES_HERE})

## Forensics

### 300
Title: Think Outside the Box  
Author: 1cysw0rdk0 & oneNutW0nder  
Type: File

#### Prompt
Look Closely

### 400
Title: Burn the candle on both ends
Author: 1cysw0rdk0 & oneNutW0nder  
Type: File

#### Prompt
It's a two step problem

### 400
Title: Burn the candle on both ends
Author: 1cysw0rdk0 & oneNutW0nder  
Type: File

#### Prompt
It's a two step problem

## Misc
>>>>>>> Stashed changes
