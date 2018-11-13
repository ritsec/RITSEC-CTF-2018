# 2018

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

| Category  | Points | Title                        | Author                    | Type          |
|-----------|--------|------------------------------|---------------------------|---------------|
| Crypto    | 150    | CictroHash                   | Cictrone                  | file & server |
| Crypto    | 300    | The Proof is in the Pudding  | Cictrone                  | file          |
| Crypto    | 500    | DarkPearAI                   | Cictrone                  | file          |
| Forensics | 250    | Think Outside the Box        | 1cysw0rdk0 & oneNutW0nder | file          |
| Forensics | 400    | Burn the candle on both ends | 1cysw0rdk0 & oneNutW0nder | file          |
| Misc      | 200    | Check out this cool filter   | 1cysw0rdk0 & oneNutW0nder | file          |
| Misc      | 300    | Lite Forensics               | knife                     | file          |
| Misc      | 400    | music.txt                    | 1cysw0rdk0 & oneNutW0nder | file          |