import requests
import json
import jsondiff


def get_bitget_list():
    url = "https://www.bitget.com/v1/trigger/tracking/getOpenSymbol"
    headers = {"Content-Type": "application/json"}
    data = {"languageType": 0}

    # Check if response is different from saved data
    with open("./data/USDT_UMCBL.json", "r") as f:
        saved_data = json.load(f)

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()["data"]

    if response_json != saved_data:
        # If different, print only the differences
        changes = jsondiff.diff(saved_data, response_json, syntax="explicit")
        for k, v in changes.items():
            print(f"----{k}----")
            for i in v:
                print("Change in {}: {}".format(i[0], i[1]))

        # Save new response to file
        with open("./data/USDT_UMCBL.json", "w") as f:
            json.dump(response_json, f, indent=4)
    else:
        # If not different, print message
        print("No difference in response")


if __name__ == "__main__":
    get_bitget_list()
