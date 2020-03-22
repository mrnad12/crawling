import requests


def download_alienvault():
    try:
        link = "https://reputation.alienvault.com/reputation.data"
        r = requests.get(link)
        with open("./samples/reputation.data", 'wb') as f:
            f.write(r.content)
    except Exception as e:
        print(f'Error downloading alienvault: {str(e)}')


def main():
    print('alienvault started downloading')
    download_alienvault()
    print('alienvault finished downloading')


if __name__ == "__main__":
    main()
