# searchのレスポンス
# mail@app.py(改行)mail@app.p(改行)知っているip1(改行)知っているip2
from flask import *
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "I like Yu"

@app.route('/ping',methods=['GET'])
def ping():
    # PING : ip.txtに書かれているip一覧をレスポンスで提供し、訪問したipをip.txtに追加します
    ip_addres = request.remote_addr
    # ip.txt 読み込み
    f = open('ip.txt','r')
    ip_list = f.read().split("\n")
    f.close()
    #追加するか
    if ip_addres in ip_list:
        return '\n'.join(ip_list)
    else:
        # ip.txt追加
        f = open('ip.txt','a')
        string_ip = f"{ip_addres}\n"
        f.write(string_ip)
        f.close()
        # return
        return '\n'.join(ip_list)

@app.route('/search',methods=['GET'])
def search():
    # SEARCH: 「自分の」mail.txtだけから検索して結果を返す。
    # mail.txtオープン
    f = open('mail.txt','r')
    mail_list = f.read().split("\n")
    f.close()
    # GETのクエリ
    query = request.args.get('q')
    # マッチしたメールアドレスの一覧
    match_mail = []
    # マッチしたら上に追加して行く
    for i in range(len(mail_list)):
        # メールアドレス
        mail_addres = mail_list[i]
        # もしマッチ
        if query in mail_addres:
            # マッチしました,追加します
            match_mail.append(mail_addres)
    return '\n'.join(match_mail)

@app.route('/add',methods=['GET'])
def add():
    # ADD: 「自分の」mail.txtにメールアドレスを追加
    # GET
    email = request.args.get('mail')
    # 入力されていない
    if len(email) == 0 or email == None:
        # エラーの場合、"E"を返します
        return "E"
    # ファイルオープン
    f = open('mail.txt','r')
    # メール一覧のリスト
    mail_list = f.read().split("\n")
    f.close()
    # emailが存在しないか（した場合、即時に"E"を返して終了
    for i in range(mail_list):
        # メールアドレス
        mail_addres = mail_list[i]
        # 一致した
        if mail_addres == email:
            # "E"を返して終了
            return "E"
    # mail.txtに書き込むテキスト
    string_mail = f"{email}\n"
    # 書き込み
    f = open("mail.txt","a")
    f.write(string_mail)
    f.close()
    # 正常に終了した場合、"A"を返す
    return "A"
