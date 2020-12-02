#!/usr/bin/env python
# coding = UTF-8
#Author:Lucky,time:2020/11/23

import os,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

report_path = r"/Users/lucky/Desktop/Auto/Daas_Interface/python_Interface_new/DaasApiTesting/Report"

sender = "904199561@qq.com"
psw = "hfzinplrbdmibcab"
receiver = '904199561@qq.com'
smtp_server = "smtp.qq.com"
Port = "465"

class email_L:

    def get_Report_file(self,report_path):
       '''
        用途：获取最新的API测试报告
        参数介绍：
            report_path：报告存储的路径
       '''
       lists = os.listdir(report_path)
       #print lists
       lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
       # report_file = os.path.join(report_path, lists[-1])
       # print(report_file)

    def get_a(self,report_path):
       path_list = os.listdir(report_path)
       for mail_body in path_list:
           if os.path.splitext(mail_body)[1] == '.html':
               print(report_path+"/"+mail_body)
               return report_path + "/" + mail_body

    def send_mail(self,sender, psw, receiver, smtpserver, report_file, port,status):
       '''
       用途：发送最新的测试报告
       参数介绍：
            sender：发送者
            psw：QQ的授权码
            receive：接收者
            smtpserver：邮件的格式
            report_file：发送的邮件附件
            port：邮箱的端口
       '''
       # with open(report_file, "rb") as f:
       #     mail_body = f.read()
       #     print(mail_body)

       # path_list = os.listdir(report_path)
       # for mail_body in path_list:
       #     if os.path.splitext(mail_body)[1] == '.html':
       #         return mail_body
       mail_body = self.get_a(report_path)

       # 定义邮件内容
       msg = MIMEMultipart()
       body = MIMEText(mail_body,'plain', _charset="utf-8")  #邮件正文的内容
       msg['subject'] = u"【%s】iBer接口自动化测试报告"%status
       msg['from'] = sender
       msg['to'] = psw
       msg.attach(body)

       # 添加附件
       att = MIMEText(open(mail_body, "rb").read() ,'base64', 'utf-8')
       att["Content-Type"] = "application/octet-stream"
       att["Content-Disposition"] = 'attachment;filename = "report.html"'
       msg.attach(att)
       try:
          smtp = smtplib.SMTP_SSL(smtpserver, port)
       except:
          smtp = smtplib.SMTP()
          smtp.connect(smtpserver, port)

       # 用户名和密码
       smtp.login(sender, psw)
       smtp.sendmail(sender, receiver,msg.as_string())
       smtp.quit()

    def test_run(self,status):
        '''如上2个方法的集合整理方法'''

        # report_file = self.get_Report_file(report_path)
        report_file = self.get_a(report_path)
        # 邮箱配置
        # sender = readConfig.sender
        # psw = readConfig.psw
        # smtp_server = readConfig.smtp_server
        # port = readConfig.port
        # receiver = readConfig.receiver
        self.send_mail(sender, psw, receiver.split(','), smtp_server, report_file, Port,status)  # 发送报告
        print(report_file)

if __name__ == "__main__":
    a = email_L()
    a.test_run("PASS")