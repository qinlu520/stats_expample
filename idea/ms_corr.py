import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# 数据库配置：
# 用户名
db_user = 'root'
# 密码
db_password = '123456'
# IP地址
db_host = '127.0.0.1'
# 端口号
db_port = 3306
# 数据库
db_name = 'regular_monitoring'
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}', echo=True)

org_dict = {'BSBK0002': '总行营业部', 'BSBK9901': '包头分行', 'BSBK9902': '赤峰分行', 'BSBK9903': '巴彦淖尔分行',
            'BSBK9904': '通辽分行', 'BSBK9906': '鄂尔多斯分行', 'BSBK9907': '锡林郭勒分行', 'BSBK9909': '呼伦贝尔分行',
            'BSBK9911': '呼和浩特分行', 'BSBK9912': '兴安盟分行', 'BSBK9913': '乌兰察布分行', 'BSBK9915': '乌海分行',
            'BSBK9916': '阿拉善分行', 'BSBK9918': '满洲里分行', 'BSBK9919': '二连浩特分行分行', 'BSBK9999': '蒙商银行汇总',
            'BSBK0001': '清算中心', 'BSBK0004': '数字银行', 'BSBKG014': '财务会计部',
            'BSBK9X03': '金融市场部汇总', 'BSBK9X04': '信用卡部汇总'}

sql_corr_1 = "SELECT T.ORG_NUM,T.INDIC_KEY, T.IND_VAL  " \
           "FROM t09_rm_indic T WHERE 1=1 AND T.INDIC_KEY IN (\'ZCFZ_A_113\',\'LR_A_103\') " \
           "AND T.STAT_DT = DATE(\'2021-03-31\') " \
           "AND T.PERIOD = \'M\' " \
           "AND T.CURR_CD = \'HRMB\' " \
           "AND T.ORG_NUM IN ( SELECT ORG_NUM FROM V_ZH ) "

# 通过pandas读取 机构数据
data_corr_1 = pd.read_sql(sql_corr_1, engine)

# print('----------------------------资产负债输出 ----------------------------------------------------------------')
pd_corr = pd.pivot_table(data_corr_1, values='IND_VAL', index='ORG_NUM', columns='INDIC_KEY',
                         aggfunc=np.sum, fill_value=0)
pd_corr = pd_corr.reset_index()
# print(pd_corr)
pd_corr.plot.scatter(x="ZCFZ_A_113", y="LR_A_103")
plt.show()
