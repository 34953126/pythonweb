import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="34953126@qq.com"    #用户名(qq邮箱)
mail_pass="xxxxxxxxxxxxxxx"   #口令(QQ授权码)

sender = "34953126@qq.com"
receivers = ['1925452697@qq.com','2265125920@qq.com'] #接收邮件，可以设置其他邮箱

#三个参数：第一个为文本内容，第二个plain 设置文本格式，第三个utf-8 设置编码
message = MIMEText('Python Ybb 邮件发送测试中...','plain','utf-8')
message['From'] = Header("半寸时光",'utf-8')  #发送者
message['To'] = Header("幸运者",'utf-8')      #接收者

subject = "Python SMTP 邮件发送测试"
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25) #25为SMTP端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error:无法发送邮件")