from flask import Flask, jsonify
from flask import request as request_obj

from hash import hash_func 

import time


app = Flask(__name__)

@app.route('/checkCollision', methods=['POST'])
def checkCollision():
    success = False
    time.sleep(5)
    message = "I am sorry that is not an actual collision."
    try:
        request_json = request_obj.get_json()
        if request_json is None or ('str1' not in request_json or 'str2' not in request_json):
            message = "You forgot to pass both strings as JSON Params :( - or didn't set Content-Type"
        else:
            digest1 = hash_func(str(request_json['str1']))
            digest2 = hash_func(str(request_json['str2']))
            digest_str1 = ''.join('{:02x}'.format(x) for x in digest1) 
            digest_str2 = ''.join('{:02x}'.format(x) for x in digest2) 
            if digest1 != digest2:
                message += " The digests provided were 0x{} and 0x{} respectively.".format(digest_str1, digest_str2)
            else:
                success = True
    except:
        pass
    if success:
        resp = jsonify({"success": success, "flag": "RS{I_am_th3_gr3@t3st_h@XOR_3v@}"})
        resp.status_code = 202
    else:
        resp = jsonify({"success": success, "message": message})
        resp.status_code = 403
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
