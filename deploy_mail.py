#-*- coding:utf-8 -*-
import smtplib
from corelib.consts import CODE_DIR, TMPL_SUBJECT, TMPL_ROLLBACK, TMPL_NORMAL, TMPL_NO_COMMITS_DEPLOY, TMPL_FIRST_TIME_DEPLOY
from corelib.github import get_pull_requests
from corelib.url import get_repo_url
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from up.settings import DEVELOP_MODE

def get_smtp_server(from_addr='service@umeng.com'):
    gmail_user = from_addr
    gmail_pwd = '1qaz2wsx'
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.esmtp_features["auth"] = "LOGIN PLAIN"
    smtp_server.debuglevel = 5
    smtp_server.starttls()
    smtp_server.ehlo('www.umeng.com')
    smtp_server.login(gmail_user, gmail_pwd)
    return smtp_server

def send_mail(subject, content, from_addr='service@umeng.com', to='cist@umeng.com', cc=None):
    smtp_server = get_smtp_server()
    toaddrs = [to]
    if cc:
        toaddrs.append(cc)
    text_msg = MIMEText(content, 'html', 'utf-8')
    attach = MIMEMultipart()
    attach['from'] = from_addr
    attach['to'] = ','.join(toaddrs)
    attach['subject'] = Header(subject, 'utf-8')
    attach.attach(text_msg)
    #send mail without attachment
    smtp_server.sendmail(from_addr, toaddrs, attach.as_string())
    smtp_server.close()

    return True

def send_service_mail_to_admin(subject, content):
    return send_mail(subject, content)

def get_deployed_content_and_send_mail(username, project_name, repo, pull_requests, is_reset_mode):
    subject, content = get_mail_content(username, project_name, repo, pull_requests, is_reset_mode)
    if not DEVELOP_MODE:
        send_deploy_mail(subject, content)
    return content

def get_mail_content(deployer, project_name, repo, pull_requests, is_reset_mode):
    subject = TMPL_SUBJECT % project_name
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    title = TMPL_NORMAL % (date, deployer)
    diff = get_pull_request_urls(pull_requests, repo)
    if is_reset_mode:
        title = TMPL_ROLLBACK % (date, deployer)
        #did the reset, change cur&last version, so we can get the diff in right order
    #TODO: read the pull requests from the Log instead of local('git log')
    content = ''.join([title, diff])
    return subject, content

def get_pull_request_urls(pull_requests, repo):
    def get_url(pull_request, repo):
        url ='<a href="%s/pull/%s" target="_blank" >%s</a>' % (get_repo_url(repo), pull_request['pull_request_id'], pull_request['subject'])
        return url
    urls = [get_url(pull_request, repo) for pull_request in pull_requests]
    urls = '<br>'.join(urls)
    return urls

def send_deploy_mail(subject, content):
    return send_service_mail_to_admin(subject, content)
