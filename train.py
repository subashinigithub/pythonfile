import requests 
def get_live_train_status(traino):
    base_url="https://rappid.in/apis/train.php?train_no={}".format(traino)
    response=requests.get(base_url)
    data=response.json()
    return data

train_number=22675
train_status=get_live_train_status(train_number)
print("****************************************************")
print("\t\tTrain Name: ",train_status["train_name"])
print("****************************************************")
for station_info in train_status["data"]:
    if station_info["is_current_station"]:
        print("Now Station\t\t\t\t: ",station_info["station_name"])
        print("Distance From the Starting\t: ",station_info["distance"])
        print("Timing\t\t\t\t\t\t: ",station_info["timing"])
        print("Delay\t\t\t\t\t: ",station_info["delay"])
        print("platform no\t\t\t\t: ",station_info["platform"])
        print("Halt Timing\t\t\t\t: ",station_info["halt"])
    else:
        print(station_info["station_name"])
print("******************************************************")
print("\t\tMessage\t\t: ",train_status["message"])
print("\t\tMessage Updated: ",train_status["updated_time"])
print("******************************************************")