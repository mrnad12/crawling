import requests
import time
import json
import uuid

url = ""
file = ""
ip = ""
domain = ""

def get_input_type_url():
    """
    The function checks inputs given by the user and retrieves the correct api urls

    Parameters:

    Returns:
        array: array of urls to be queried
    """
    urls = []
    if file != '':
        urls.append({'method': 'GET', 'input': file,
                        'url': 'https://www.virustotal.com/vtapi/v2/file/report', 'ioc': 'ioc_virustotal_file'})
    if ip != '':
        urls.append({'method': 'GET', 'input': ip,
                       'url': 'https://www.virustotal.com/vtapi/v2/ip-address/report', 'ioc': 'ioc_virustotal_ip'})
    if domain != '':
        urls.append({'method': 'GET', 'input': domain,
                        'url': 'https://www.virustotal.com/vtapi/v2/domain/report', 'ioc':'ioc_virustotal_domain'})
    if url != '':
        urls.append({'method': 'POST', 'input': url,
                        'url': 'https://www.virustotal.com/vtapi/v2/url/report', 'ioc':'ioc_virustotal_url'})
    return urls

def get_correct_params(url):
    """
    The function returns the correct parameters for a request to the api

    Parameters:
        url (dict): dictionary that represent url data

    Returns:
            json: json object with correct parameters for thr request.
    """
    if 'domain' in url['url']:
        params = {'apikey': "b85a2f41ed99619bca920712f0333a9ac736dbebe916b750fc70d05354bf0293", 'domain': url['input']}
    elif 'ip' in url['url']:
        params = {'apikey': "b85a2f41ed99619bca920712f0333a9ac736dbebe916b750fc70d05354bf0293", 'ip': url['input']}
    else:
        params = {'apikey': "b85a2f41ed99619bca920712f0333a9ac736dbebe916b750fc70d05354bf0293", 'resource': url['input']}

    return params

def crawl():
    """
        The crawl function is a requisite for the RTE package, in this case the function calls
        iterate the urls and send an api request for each url and saves the response

        Parameters:

        Returns:
            Nothing. saves response.
        """
    try:
        urls = get_input_type_url()
        for url in urls:
            params = get_correct_params(url)
            headers = {
                'Accept-Encoding': 'gzip, deflate'
            }
            # time.sleep(16)
            if url['method'] == 'GET':
                response = requests.get(url["url"], headers=headers, params=params)
            else:
                response = requests.post(url["url"], headers=headers, params=params)

            data = json.loads(response.content)
            if 'domain' in url['ioc']:
                data["domain"] = params["domain"]
            if 'ip' in url['ioc']:
                data["ip"] = params["ip"]
            if 'url' in url['ioc']:
                data["url"] = params["resource"]
            if 'file' in url['ioc']:
                data["file"] = params["resource"]

            with open(f"./samples/{str(uuid.uuid4())}.json", "a") as f:
                json.dump(data, f)
    except Exception as e:
        print(f'Error occurred while running virus total api calls, error: {str(e)}')


if __name__ == "__main__":
    crawl()