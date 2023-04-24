import requests

sharepoint_config = {
    "clientId" : "c8799c05-7389-4c4d-907f-05943cebe94e",
    "tenantId" : "1b78f26c-9ddc-4301-aebc-41fd55591d80",
    "resourceId": "0d10361e-ea7e-4176-9487-b4c72a6cc571",
    "secId" : "a5Q8Q~mW82VazxJegOM6zM1GMnS5J_4ccx70CcaC"

}
### ------------------------------------------------
## This function will generate token for Sharepoint
###-------------------------------------------------

def getToken(sharepoint_config):
    access_token = ""
    try:
        reqURL = "https://accounts.accesscontrol.windows.net/{}/tokens/OAuth/2".format(
            sharepoint_config["tenantId"])
        reqPayload = {
            'grant_type': 'client_credentials',
            'client_id': f'{sharepoint_config["clientId"]}@{sharepoint_config["tenantId"]}',
            'client_secret': sharepoint_config["secId"],
            'resource': f'{sharepoint_config["resourceId"]}@{sharepoint_config["tenantId"]}'
        }
        reqHeader = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.post(reqURL, data=reqPayload, headers=reqHeader)
        if response.status_code in [200, 201] and (not response.json().get('access_token', "")== ""):
            access_token = response.json().get('access_token')
            print(f'--- Access token Received {access_token}')
        else:
            print(f'--- Access token not received failed response code :{response.status_code} text : {response.text}')
    except Exception as e:
        print("Exception while getting the token:", e)
    return access_token