from tkinter import messagebox

sms_status = "PENDING"

messagebox_text = f"""{sms_status} שימו לב, מצב הודעת הסמס שזוהה הוא
         www.callr.com ניתן לקבל מידע נוסף באתר
Idan05423 :סיסמא  |   spider3d_1 :שם משתמש """

messagebox.showerror("שגיאה בשליחת סמס",messagebox_text)
