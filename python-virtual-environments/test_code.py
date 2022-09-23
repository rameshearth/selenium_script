import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
final_array=[{'SrNumber': 1, 'overall_rating': 7.5}]
#print(json.dumps((final_array)))
#params = {"final_array": '[{"SrNumber": 1, "overall_rating": 7.5}]'}
params = {"final_array": json.dumps(final_array)}
print(params);

data = MultipartEncoder(fields = params)

headers = {
    'Content-type': data.content_type
}
response = requests.post(
    'http://localhost/Xplore-new-22-12-21/xplore/index.php/apis/insertPlaceDetail',
    data = data,
    headers = headers
)
print(response.text)
"""
import json
import urllib.request 
import requests
headers = {'cache-control': 'no-cache','content-type': 'application/json'}
conditionsSetURL= 'http://localhost/Xplore-new-22-12-21/xplore/index.php/apis/insertPlaceDetail';
payload={"SrNumber": 1}
response = requests.request("POST",conditionsSetURL,headers=headers,data=json.dumps(payload))
print(response);
"""
