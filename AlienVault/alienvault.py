import requests
import pandas as pd
import io
import uuid

def download_alienvault():
    try:
        link = "https://reputation.alienvault.com/reputation.data"
        r = requests.get(link)
        rt = pd.read_csv(io.StringIO(r.content.decode("utf8")), sep="#", names=["ip", "risk", "reliability", "activity",
                         "country", "city", "geolocation", "Num"])
        with open(f"./samples/{uuid.uuid4()}.csv", 'w') as f:
            f.write(rt.to_csv(sep=",", index=False))
    except Exception as e:
        print(f'Error downloading alienvault: {str(e)}')


def main():
    print('alienvault started downloading')
    download_alienvault()
    print('alienvault finished downloading')


if __name__ == "__main__":
    main()
