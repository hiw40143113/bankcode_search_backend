import csv
import requests
from io import StringIO
from django.core.management.base import BaseCommand
from apis.models import Bank, Branch

class Command(BaseCommand):
    help = 'Load bank data from CSV file'

    def handle(self, *args, **kwargs):
        url = 'https://stat.fsc.gov.tw/FSC_OAS3_RESTORE/api/CSV_EXPORT?TableID=B14&OUTPUT_FILE=Y'
        response = requests.get(url)
        response.encoding = 'utf-8-sig'
        
        if response.status_code == 200:
            csvfile = StringIO(response.text)
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # 只處理包含"銀行"、"信用合作社"的資料(其他非屬金管會定義之銀行)
                if not any(keyword in row.get('機構名稱', '') for keyword in ['銀行', '信用合作社']):
                    continue

                # 如果機構代號為空值(總行)，存入bank models
                if not row['機構代號']:
                    bank_name = row['機構名稱']
                    # 去除多餘文字
                    if '銀行' in bank_name:
                        bank_name = bank_name.replace('股份有限公司', '').strip()
                    elif '信用合作社' in bank_name:
                        bank_name = bank_name.replace('有限責任', '').replace('保證責任', '').strip()

                    bank_code = row['總機構代號']
                    Bank.objects.update_or_create(
                        name=bank_name,
                        defaults={'code': bank_code}
                    )
                
                # 剩下的存入branch models
                else:
                    bank_code = row['總機構代號']
                    try:
                        bank = Bank.objects.get(code=bank_code)
                    except Bank.DoesNotExist:
                        continue

                    branch_name = row['機構名稱']
                    branch_code = row['機構代號']
                    if bank.name in branch_name:
                        branch_name = branch_name.replace(bank.name, '').strip()
                    if '股份有限公司' in branch_name:
                        branch_name = branch_name.replace('股份有限公司', '').strip()
                    branch_address = row['地址']
                    branch_phone = row['電話'].replace('=', '+')

                    Branch.objects.update_or_create(
                        bank=bank,
                        code=branch_code,
                        defaults={
                            'name': branch_name,
                            'address': branch_address,
                            'phone': branch_phone
                        }
                    )

            self.stdout.write(self.style.SUCCESS('Successfully loaded and updated bank data from API'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from API'))
