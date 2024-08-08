import pandas as pd
from pymongo import MongoClient
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load accommodation ratings from CSV and insert into MongoDB'

    def handle(self, *args, **kwargs):
        # CSV 파일 경로
        csv_file_path = r'C:\Users\Playdata\Downloads\fillna_acc_ratings.csv'

        # CSV 파일을 pandas DataFrame으로 불러오기
        df = pd.read_csv(csv_file_path)

        # MongoDB 연결 설정
        mongo_uri = "mongodb+srv://Seora:youlove4154@mydiary.727yxhm.mongodb.net/MyDiary?retryWrites=true&w=majority"
        client = MongoClient(mongo_uri)
        db = client['MyDiary']
        collection = db['accommodations_ratings']

        # 기존 컬렉션 삭제 (있을 경우)
        collection.drop()

        # DataFrame의 각 행을 MongoDB 컬렉션에 삽입
        collection.insert_many(df.to_dict('records'))

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))