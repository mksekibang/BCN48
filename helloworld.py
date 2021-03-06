#!-*- coding:utf-8 -*-"
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import os
import voting
import crpt

class MainPage(webapp.RequestHandler):
    
    def get(self):
        params = {
            'Title':'BCN48第1回総選挙！！！',
            'form':voting.votingform()
        }
        fpath = os.path.join(os.path.dirname(__file__),'htmldir','write.html')
        html = template.render(fpath,params)
        self.response.out.write(html)
        
    def post(self):
        form = voting.votingform(self.request.POST)
        params = {
            'Title':'入力エラーです。未入力の必須項目があります',
            'form':form
        }
        if form.is_valid():
            entity = form.save(commit=False)
            ErrorFlg = False
            ErrorMsg = ""
            # シリアルコードの桁数チェックをいれること（シリアルコードは16文字）
            if len(entity.serialno) <> 16:
                ErrorFlg = True
                ErrorMsg = "シリアルコードの桁数が間違っています。"
            else:
                serial_check = voting.votingdata.gql("WHERE serialno = :checkno",checkno = entity.serialno)
                if serial_check.count() == 0:
                    serial_decrypt = crpt.DecryptionMessage(entity.serialno)
                    if serial_decrypt > '00000000' and serial_decrypt < '100000000':
                        params = {
                            'name': entity.name,
                            'serialno': entity.serialno
                            }
                        fpath = os.path.join(os.path.dirname(__file__),'htmldir','preview.html')
                    else:
                        ErrorFlg = True
                        ErrorMsg = "不正なシリアルコードです。"
                else:
                    ErrorFlg = True
                    ErrorMsg = "すでに使用済みのシリアルコードです。"
            if ErrorFlg:
                params = {
                    'Title':ErrorMsg,
                    'form':voting.votingform()
                    }
                fpath = os.path.join(os.path.dirname(__file__),'htmldir','write.html')
        else:
            fpath = os.path.join(os.path.dirname(__file__),'htmldir','write.html')
        html = template.render(fpath,params)
        self.response.out.write(html)

        
application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
