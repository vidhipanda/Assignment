import ssl
import socket
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

# get SSL certificate of a domain
def get_ssl_expiry_date(domain, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((domain, port)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as sslsock:
            ssl_info = sslsock.getpeercert()
            expiry_date_str = ssl_info['notAfter']
            # Convert the expiration date to a datetime object
            expiry_date = datetime.datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y GMT')
            return expiry_date

# check expiration in days
def check_certificate_expiry(domain, port=443):
    expiry_date = get_ssl_expiry_date(domain, port)
    today = datetime.datetime.utcnow()
    days_until_expiry = (expiry_date - today).days
    return days_until_expiry

# send an email alert
def send_email_alert(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())

# send Slack alert
def send_slack_alert(slack_webhook_url, message):
    payload = {
        "text": message
    }
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code != 200:
        raise ValueError(f"Slack alert failed with {response.status_code}, response: {response.text}")

# Main function
def check_ssl_certificates(domains, port=443, alert_threshold=15, email_alert=False, slack_alert=False, **kwargs):
    for domain in domains:
        try:
            days_until_expiry = check_certificate_expiry(domain, port)
            print(f"Domain: {domain}, SSL Certificate expires in {days_until_expiry} days.")
            
            # If certificate is expiring in less than 15 days, send an alert
            if days_until_expiry < alert_threshold:
                message = f"SSL Certificate for {domain} is expiring in {days_until_expiry} days!"
                print(message)
                
                if email_alert:
                    send_email_alert(
                        subject=f"SSL Certificate Expiration Alert for {domain}",
                        body=message,
                        **kwargs
                    )
                
                if slack_alert:
                    send_slack_alert(slack_webhook_url=kwargs['slack_webhook_url'], message=message)

        except Exception as e:
            print(f"Failed to check SSL certificate for {domain}: {str(e)}")

if __name__ == "__main__":
    domains = ['example.com', 'example.org']
    port = 443 
    alert_threshold = 15 

    # For email alerts:
    email_alert = True
    send_email_kwargs = {
        'to_email': 'xyz@example.com',
        'from_email': 'abc@example.com',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 465,
        'smtp_user': 'xyz@example.com',
        'smtp_password': '#######'
    }

    # For Slack alerts:
    slack_alert = True
    slack_webhook_url = 'https://hooks.slack.com/services/your/slack/webhook'

    # Check SSL certificates
    check_ssl_certificates(
        domains,
        port,
        alert_threshold,
        email_alert=email_alert,
        slack_alert=slack_alert,
        slack_webhook_url=slack_webhook_url,
        **send_email_kwargs
    )
