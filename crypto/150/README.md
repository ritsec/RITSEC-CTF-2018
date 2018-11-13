# Crypto 150: CictroHash

**Author**: Cictrone

**Description**: _None_300
See the attached PDF for an amazing new Cryptographic Hash Function called
CictroHash. For this challenge you must implement the described Hash Function
and then find a collision of two strings. Once a collision is found send both 
strings to {{INSERT_SERVER}} as a HTTP POST request like below:


```
curl -X POST http://{{INSERT_SERVER}}/checkCollision \
--header "Content-Type: application/json" \
--data '{"str1": "{{INSERT_STR1}}", "str2": "{{INSERT_STR2}}"}'
```

If the strings are a valid collision then the flag will be returned.

**Files**: `CictroHash.pdf`