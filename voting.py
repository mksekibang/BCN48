#!-*- coding:utf-8 -*-"
from google.appengine.ext import db
from google.appengine.ext.db import djangoforms

#投票データのモデル
class votingdata(db.Model):
    #名前
    name = db.StringProperty(required=True,multiline=False,verbose_name='名前')
    #シリアルナンバー
    serialno = db.StringProperty(required=True,multiline=False,verbose_name='シリアルコード')

#投票フォーム
class votingform(djangoforms.ModelForm):
    class Meta:
        model = votingdata
