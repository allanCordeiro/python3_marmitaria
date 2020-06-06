import csv


class Append:

    @staticmethod
    def flush_file(data: list, file_name):
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def load_file(self, file_name):
        with open(file_name, encoding='utf-8') as file:
            csv_file = csv.reader(file)
            data: list = []
            for row in csv_file:
                data.append(row)
        return data