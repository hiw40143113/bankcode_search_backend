import csv
from django.core.management.base import BaseCommand
from apis.models import Bank, Branch

class Command(BaseCommand):
    help = 'Load bank data from CSV file'

    def handle(self, *args, **kwargs):
        with open('/static/datafile/bank_code_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # 只處理包含"銀行"及"信用合作社"的資料(其他非屬金管會定義之銀行)
                if '銀行' not in row['機構名稱'] and '信用合作社' not in row['機構名稱']:
                    continue
                
                # 清除多餘字
                bank_name = row['機構名稱']
                if '銀行' in bank_name:
                    bank_name = bank_name.replace('股份有限公司', '').strip()
                elif '信用合作社' in bank_name:
                    bank_name = bank_name.replace('有限責任', '').replace('保證責任', '').strip()

                bank_code = row['總機構代號'].zfill(3)

                bank, created = Bank.objects.get_or_create(name=bank_name, code=bank_code)
                
                # 如果機構代號為空(總行)，跳過不進入分行資料庫
                if not row['機構代號']:
                    continue
                
                branch_code = bank_code + row['機構代號'].zfill(4)
                # 去掉銀行名稱只留分行名稱
                branch_name = row['機構名稱'].replace(bank_name, '').strip()
                branch_address = row['地址']
                
                # 替換電話中的錯誤格式"="為"+"
                branch_phone = row['電話'].replace('=', '+')
                
                Branch.objects.get_or_create(
                    bank=bank,
                    name=branch_name,
                    code=branch_code,
                    address=branch_address,
                    phone=branch_phone
                )
