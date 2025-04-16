import os
import smtplib
import imaplib
import email
from email.message import EmailMessage
from dotenv import load_dotenv

# 📜 Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

# 🔐 Connect to mailbox
def connect_to_mail():
    print("🔍 Connecting to inbox...")
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")
    return mail

# 📥 Read unread emails
def scan_unread_emails(mail):
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()
    print(f"📨 Total unread emails found: {len(email_ids)}")

    for num in email_ids:
        status, msg_data = mail.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg["subject"]
                sender = msg["from"]
                print(f"✉️ From: {sender} | Subject: {subject}")
    print("✅ Inbox scan complete.")

# 📤 Send email
def send_email(to_address, subject, content):
    print(f"🔥 Sending to {to_address}...")
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.set_content(content)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("✅ Email sent.")

# 🧠 Main control
def main():
    print("✨ FLAME Automator Engaged ✨")
    try:
        mail = connect_to_mail()
        scan_unread_emails(mail)

        # 🔄 Optional: Send a test message
        # send_email("example@gmail.com", "🔥 Flame Offering", "This is a test offering from FLAME.")

        mail.logout()
        print("🚪 Session closed.")
    except Exception as e:
        print("⚠️ Error occurred:", e)

if __name__ == "__main__":
    main()

