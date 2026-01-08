import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_research_email(summary_text, paper_title, paper_url):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    # Create the email container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"🚀 Daily Research: {paper_title}"

    # Create a nice HTML body
    html = f"""
    <html>
      <body>
        <h2 style="color: #2E4053;">{paper_title}</h2>
        <p><strong>AI Summary:</strong></p>
        <div style="background-color: #F4F6F7; padding: 15px; border-left: 5px solid #2E4053;">
          {summary_text}
        </div>
        <br>
        <a href="{paper_url}" style="background-color: #28B463; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Read Full Paper</a>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)