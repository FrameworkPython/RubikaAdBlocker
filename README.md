# ربات ضد تبلیغات روبیکا


این ربات برای جلوگیری از تبلیغات در گروه‌های روبیکا طراحی شده است. با استفاده از الگوهای ممنوعه، این ربات پیام‌هایی را که حاوی لینک باشد یا فوروارد شده باشد را حذف می‌کند.

## قابلیت ها

این ربات به صورت Full Asynchronous نوشته شده است و میتواند همزمان در چند گروه فعال باشد. 
این ربات میتواند پیام های تبلیغاتی را خیلی سریع و در کسری از ثانیه پاک نماید.

## نصب و راه‌اندازی

برای نصب و راه‌اندازی این ربات، ابتدا فایل اسکریپت را دانلود نمایید:

```bash
git clone https://github.com/FrameworkPython/RubikaAdBlocker
```
سپس باید وارد پوشه اسکریپت شده و کتابخانه های مورد نیاز را نصب نمایید:
```bash
cd RubikaAdBlocker
```
```bash
pip install -r requirements.txt
```
بعد از نصب شدن کتابخانه ها، شما باید guid گپ هایی که میخواید ربات داخلش فعال بشه رو در لاین ۳۵ به جای guid1,guid2 وارد کنید.
بعد از ذخیره تغییرات ، میتوانید ربات را اجرا نمایید:
```bash
python bot.py
```
## ویدیو آموزشی 
[![تست سلام](https://s30.picofile.com/file/8470116218/01437084.jpg)[https://google.com]
## توسعه 
اگر می‌خواهید به توسعه این ربات کمک کنید، لطفا ابتدا یک شاخه از مخزن ایجاد کنید و تغییرات خود را در آن اعمال کنید. سپس، یک درخواست ادغام برای اعمال تغییرات خود به مخزن اصلی ارسال کنید.

## مجوز 

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر، لطفا فایل LICENSE را مطالعه کنید.
