import logging
import glob
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd


logger = logging.getLogger(__name__)
# logger.addHandler(logging.NullHandler())
logger.addHandler(logging.StreamHandler())

class Reader():

    def __init__(self, cfg):
        self.config = cfg
        if self.config['base_job_filename']:
            self.base_filename = self.config['base_job_filename']

        self.base_path = cfg['data_path']

        self.list_of_xmls = glob.glob(
            self.base_path +
            '/*.xml')

        self.list_of_normalized4 = glob.glob(
            self.base_path +
            '/*.normalized4')

        if len(self.list_of_xmls) + len(self.list_of_normalized4) == 0:
            raise FileNotFoundError


    def read_all(self):
        print('reading file with name {}'.format(self.list_of_xmls[0]))
        self.read_xml(self.list_of_xmls[0])
        # norm4 = self.read_normalized4(self.list_of_normalized4[0])


    # read the base file and put it in the first thing
    def read_base(self):
        if self.base_filename:
            logging.debug('I have a base_filename')



    # still need to fix this up
    def read_xml(self, filepath):
        with open(self.base_path + '/' + self.base_filename, encoding="windows-1252") as fp:
            soup = bs(fp, 'lxml')
        res = soup.find_all('coderecord')

        print(res)
        for

        ### generate code as this is a non-numerical, but alphanumericcal

            # print(soup.CodeTable)
        # logging.error()
        # print(soup.find('CodeTable').find('CodeRecordList').findChildren())

#         < InstanceList >
#         < Instance >
#         < InstanceDescription > fashion
#         designer < / InstanceDescription >
#
#     < / Instance >
#
# < / InstanceList >




    def read_normalized4(self, filepath):
        previous_code = 0
        read_list = []
        with open(filepath) as fp:
            reader = csv.DictReader(fp, fieldnames=['code', 'synonym'], dialect='excel-tab')
            for row in reader:
                if row['code'] == '-':
                    row['code'] = previous_code
                read_list.append(row)
                previous_code = row['code']

        norm_df = pd.DataFrame(read_list)
        return norm_df

