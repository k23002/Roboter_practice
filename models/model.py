import csv
import os

class Model:
    def __init__(self, filename="restaurants_data.csv"):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        """
        csvファイルを読み込んで、データを辞書としてロードする。
        """
        if os.path.exists(self.filename):
            data = {}
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        restaurant_name, count = row
                        data[restaurant_name] = int(count)
            return data
        else:
            print("ファイルが見つかりませんでした。")
        return {}
    
    def _save_data(self):
        """
        データをcsvファイルに保存する
        """
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for restaurant_name, count in self.data.items():
                writer.writerow([restaurant_name, count])

    def update(self, restaurant_name):
        """
        お店の名前の追加やおすすめ回数を更新する
        """
        if restaurant_name in self.data:
            self.data[restaurant_name] += 1
        else:
            self.data[restaurant_name] = 1
        self._save_data()