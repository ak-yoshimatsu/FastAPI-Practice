import smtplib
from email.mime.text import MIMEText

from fastapi import APIRouter
from pydantic import BaseModel


class Mail(BaseModel):
    fromaddr: str
    toaddr: str
    subject: str
    message: str


router = APIRouter()


@router.post("/")
def test_mail(mail: Mail):
    m = MIMEText(mail.message)
    m["Subject"] = mail.subject
    m["From"] = mail.fromaddr
    m["To"] = mail.toaddr

    s = smtplib.SMTP(host="mailhog", port=1025)
    s.sendmail(mail.fromaddr, mail.toaddr, m.as_string())
    s.close()

    return "done"
