import requests
import pandas as pd
import zipfile
import io
import csv
import uuid

def download_alexa():
    try:
        link = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
        r = requests.get(link)
        zf = zipfile.ZipFile(io.BytesIO(r.content))
        cov = pd.read_csv(zf.open("top-1m.csv", "r"), names=["alexa_score","domain"])
        with open(f"./samples/{uuid.uuid4()}.csv", 'w') as f:
          f.write(cov.to_csv(index=False))
    except Exception as e:
        print(f'Error downloading Alexa: {str(e)}')


def main():
    print('Alexa started downloading')
    download_alexa()
    print('Alexa finished downloading')


if __name__ == "__main__":
    main()
