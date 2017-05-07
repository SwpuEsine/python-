# coding:utf-8
import random
import smtplib
from email.mime.text import MIMEText
import time


def send_mail(mailto):
    print
    'Setting MIMEText'
    CT = open('content.txt', 'r')  # 读取发送邮件内容
    content = CT.read().decode('utf-8')
    msg = MIMEText(content.encode('utf8'), _subtype='html')

    CT.close()  # 关闭文件
    msg['From'] = mail_user
    msg['SUbject'] = u'Python邮件发送测试'
    msg['To'] = mailto

    try:
        print
        'Connectting', mail_host
        s = smtplib.SMTP_SSL(mail_host, 465)

        print
        'Login to mail_host'
        s.login(mail_user, mail_pwd)

        print
        'Send mail'
        s.sendmail(mail_user, mailto, msg.as_string())

        print
        'Close the connection between the mail server'
        s.close()
    except Exception as e:
        print
        "Exceptioin ", e


def sendqunmail():
    try:
        f = open(filelist, 'r')
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i].find('(') <> -1 and lines[i].find(')') <> -1:
            qqnum = lines[i].split('(')[1].split(')')[0]
            if qqnum.isdigit():
                mailto = qqnum + '@qq.com'
                print
                'Sendmail to:' + mailto
                send_mail(mailto)
                time.sleep(10)
    except Exception, ex:
    print
    filelist, ex


if __name__ == "__main__":
    mail_host = 'smtp.163.com'
    mail_user = 'test@163.com'
    mail_pwd = 'test123'
    filelist = 'list.txt'
    sendqunmail()