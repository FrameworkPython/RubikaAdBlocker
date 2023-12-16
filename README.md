
  
# ربات ضد تبلیغات روبیکا


این ربات برای جلوگیری از تبلیغات در گروه‌های روبیکا طراحی شده است. با استفاده از الگوهای ممنوعه، این ربات پیام‌هایی را که حاوی لینک باشد یا فوروارد شده باشد را حذف می‌کند.

  
## **قابلیت ها**

این ربات به صورت Full Asynchronous نوشته شده است و میتواند همزمان در چند گروه فعال باشد. 
این ربات میتواند پیام های تبلیغاتی را خیلی سریع و در کسری از ثانیه پاک نماید.
  <div dir="rtl">

- **حالت سختگیر**
- برای فعال کردن این حالت، میتوانید از دستور `حالت سختگیر` استفاده کنید،بعد از فعال شدن این حالت، کاربرانی که لینک یا فوروارد ارسال کنند بدون اخطار از گروه حذف خواهند شد، برای غیرفعال سازی این حالت میتوانید از دستور `حالت سختگیر غیرفعال` استفاده نمایید.

     https://github.com/FrameworkPython/RubikaAdBlocker/assets/149888152/77e74e74-da54-4799-88ce-7b1251b75c53

</div>

- **گرفتن و یا پاکسازی لیست سیاه**
- با دستور `لیست سیاه` میتوانید لیست سیاه گروه را دریافت نمایید، برای پاکسازی لیست سیاه میتوانید از دستور `پاکسازی لیست سیاه` استفاده نمایید.


     https://github.com/FrameworkPython/RubikaAdBlocker/assets/149888152/1d072a57-8aef-4c64-9cc7-8d2e1ee9301d


- **گرفتن لینک گروه**
- با دستور `لینک` میتوانید لینک گروه مورد نظر را دریافت نمایید.



  https://github.com/FrameworkPython/RubikaAdBlocker/assets/149888152/6b0d1831-d965-4e4e-9329-bac9afc17e6f


- **تنظیم  یا خاموش کردن سیستم اخطار**
- با دستور `اخطار x` میتونید تعداد اخطار در گروه رو تنطیم کنید، به جای x تعداد اخطار رو وارد کنید.مثال:`اخطار ۴`. برای غیرفعال کردن سیستم اخطار میتونید دستور `اخطار خاموش` رو وارد کنید


  https://github.com/FrameworkPython/RubikaAdBlocker/assets/149888152/45e77bc7-81a7-4791-9200-ff1509e8d647


- **گرفتن وضعیت و یا پاک کردن اخطار کاربرها**
- با ریپلی بر روی کاربر مورد نظر و ارسال دستور `وضعیت اخطار` میتونید ببینید کاربر مورد نظر چند اخطار دارد. برای پاک کردن اخطار های کاربر،‌ روی وی کلیک نموده و دستور `پاک کردن اخطار` رو وارد کنید.


  https://github.com/FrameworkPython/RubikaAdBlocker/assets/149888152/74d306ca-eb55-452f-84c2-5f55ff463ec7

  
  
## نصب و راه‌اندازی



https://github.com/FrameworkPython/RubikaAdBlocker/assets/149888152/38d13bee-eb2b-4d3c-bc4e-7ecaf9c5fa75





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

برای دیدن ویدیو آموزشی نحوه اجرا و استفاده کردن از ربات روی [لینک](https://uupload.ir/view/inshot_20231203_161800858_1_ob17.mp4/) کلیک کنید.



## توسعه 
اگر می‌خواهید به توسعه این ربات کمک کنید، لطفا ابتدا یک شاخه از مخزن ایجاد کنید و تغییرات خود را در آن اعمال کنید. سپس، یک درخواست ادغام برای اعمال تغییرات خود به مخزن اصلی ارسال کنید.

## مجوز 

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر، لطفا فایل LICENSE را مطالعه کنید.

