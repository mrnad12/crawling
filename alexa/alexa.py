import requests


def download_alexa():
    try:
        link = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
        r = requests.get(link)
        with open("./samples/alexa.zip", 'wb') as f:
            f.write(r.content)
    except Exception as e:
        print(f'Error downloading Alexa: {str(e)}')


def main():
    print('Alexa started downloading')
    download_alexa()
    print('Alexa finished downloading')


if __name__ == "__main__":
    main()
