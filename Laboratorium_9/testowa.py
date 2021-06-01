import json


class Testowa:
    def __init__(self, name_os):
        self.name_os = name_os

    def getData(self):
        os_lower = self.name_os.lower()
        path = f"terminal_commands/{os_lower}.json"
        try:
            with open(path, "r") as read_file:
                data = json.load(read_file)
            return data
        except:
            print("No data")
            raise FileNotFoundError

    def userCommandDescription(self, userCommand):
        try:
            tdata = self.getData()
            arr = userCommand.split(' ')
            description = tdata[arr[0]][arr[1]]
            return description
        except:
            return "Something wrong.No description"
