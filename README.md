# The Internship Program Developer Exam 2019
https://bitbucket.org/theinternshipio/exam-2019/src/master/README.md?mode=edit&spa=0&at=master&fileviewer=file-view-default

## ข้อสอบมีทั้งหมด 2 ตอน

## กรุณาอ่านให้ครบทั้ง _ข้อสอบ_ และ _วิธีการส่ง_

## ตอนที่ 1

เขียนโปรแกรมเพื่อเล่นเกม Hangman ใน Terminal/Console (Command Line Interface) โดยมีความสามารถ อย่างน้อยต่อไปนี้
เลือกหมวดหมู่ของคำได้ โดยเก็บคำในแต่ละหมวดหมู่แยกเป็นไฟล์ หมวดหมู่ละ 1 ไฟล์ โปรแกรมที่ส่งมาให้ตรวจจะต้องมีหมวดหมู่อย่างน้อย 2 หมวดหมู่ และมีคำในหมวดหมู่อย่างน้อยหมวดหมู่ละ 5 คำ
“คำ” ที่ใช้เล่นเกม อาจประกอบด้วยช่องว่าง ตัวเลข และสัญลักษณ์ แต่จะไม่เป็นส่วนหนึ่งของการเล่นเกม จะต้องแสดงผลทันที (เช่น คำอาจจะเป็น “Mong 31!!” ก็จะแสดงผลว่า \_ \_ \_ \_ 31!! เป็นต้น) การเล่นเกมจะใช้ตัวอักษรภาษาอังกฤษเท่านั้น โดยเป็น case-insensitive ทั้งหมด
คำแต่ละคำ จะต้องประกอบด้วย “คำใบ้”
มีการแสดงตัวอักษรที่เดาผิด
มีการคำนวนคะแนนจากการเล่นเดาคำในแต่ละรอบ โดยจะคำนวนคะแนนอย่างไร ขึ้นกับนักศึกษา (คิดเกณฑ์/อัลกอริทึมการให้คะแนนเองได้เลย)

ตัวอย่างการรันโปรแกรม

```
Select Category:
English Premiere League Teams (2018/2019)
Historical World Leaders
Famous Songs

> 2

Hint: “World War II”

_ _ _ _ _ _ _ _    score 0, remaining wrong guess 10
> d
_ _ _ _ _ _ _ _    score 0, remaining wrong guess 9, wrong guessed: d
> r
_ _ r _ _ _ _ _    score 15, remaining wrong guess 9, wrong guessed: d
>
```

## ตอนที่ 2

เขียนโปรแกรมแปลงข้อมูลสภาพอากาศ จาก Format XML เป็น json ใน Terminal/Console (Command Line Interface) โดยมีคุณสมบัติดังนี้
โปรแกรมจะรับ Input เป็นไฟล์สภาพอากาศสกุล xml และรีเทิร์น Output เป็น ไฟล์สภาพอากาศสกุล json
ข้อมูลสภาพอากาศทั้งสอง Format จะเป็นไปตามตัวอย่างข้อมูล XML และ Json ที่โจทย์กำหนด

ตัวอย่างการรันโปรแกรม

```
> head -n 5 weather.xml
<?xml version="1.0" encoding="UTF-8"?>
<current>
  <city id="2643741" name="City of London">
    <coord lon="-0.09" lat="51.51" />
    <country>GB</country>
...

> weather weather.xml
weather.json

> head -n 5 weather.json
{
  "city": {
    "id": "2643741",
    "name": "City of London",
    "coord": {
...
```

### สิ่งที่นักศึกษาต้องส่ง:
1. Source Code ของโปรแกรม โดยนักศึกษาสามารถใช้ภาษาโปรแกรมใดๆ ก็ได้ ไม่ว่าภาษานั้นจะเป็นภาษาที่ได้รับความนิยมหรือไม่ก็ตาม (แต่ให้ตั้งนามสกุลไฟล์ให้ถูกต้องด้วย)
2. ไฟล์ README ที่ประกอบด้วยชื่อ นามสกุล e-mail เบอร์โทรศัพท์ และวิธีการ compile/build/run โปรแกรม


# การส่งคำตอบ
สร้าง Repository บน Git Hosting เจ้าใดก็ได้ (Github, GitLab, Bitbucket หรือ อื่น ๆ)

1. นำ Source Code, README ตอนที่ 1 ใส่ใน Folder ชื่อ _hangman_
2. นำ Source Code, README ตอนที่ 2 ใส่ใน Folder ชื่อ _weather_
3. อัพโหลดขึ้น Repository ปรับ Permission เป็น Public ให้เรียบร้อยแล้ว
4. Submit URL ของ Repository ลงกล่องคำตอบ [ตามลิ้งที่สมัคร](https://theinternship.typeform.com/to/TPKi4v)

หมายเหตุ:
นักศึกษาไม่จำเป็นต้องออกแบบส่วนติดต่อกับผู้ใช้เหมือนกับตัวอย่าง สามารถออกแบบได้ตามใจชอบ
หากนักศึกษามีการใช้โค้ดที่ไม่ได้คิดเอง มีการคัดลอกมาจากที่อื่น ไม่ว่าจะคัดลอกจากหนังสือ เว็บไซต์ รวมถึงให้เพื่อนช่วยคิดให้ ให้นักศึกษาระบุแหล่งที่มาประกอบใน README อย่างชัดเจน หากผู้ตรวจโปรแกรมตรวจพบเอง จะตัดสิทธิ์การสมัคร The Internship 2019 ในทุกตำแหน่งที่นักศึกษาสมัคร


### ตัวอย่างข้อมูล XML

```
<?xml version="1.0" encoding="UTF-8"?>
<current>
  <city id="2643741" name="City of London">
    <coord lon="-0.09" lat="51.51" />
    <country>GB</country>
    <sun rise="2015-06-30T03:46:57" set="2015-06-30T20:21:12" />
  </city>
  <temperature value="72.34" min="66.2" max="79.88" unit="fahrenheit" />
  <humidity value="43" unit="%" />
  <pressure value="1020" unit="hPa" />
  <wind>
    <speed value="7.78" name="Moderate breeze" />
    <direction value="140" code="SE" name="SouthEast" />
  </wind>
  <clouds value="0" name="clear sky" />
  <visibility value="10000" />
  <precipitation mode="no" />
  <weather number="800" value="Sky is Clear" icon="01d" />
  <lastupdate value="2015-06-30T08:36:14" />
</current>
```

### ตัวอย่างข้อมูล Json

```
{
  "city": {
    "id": "2643741",
    "name": "City of London",
    "coord": {
      "lon": "-0.09",
      "lat": "51.51"
    },
    "country": "GB",
    "sun": {
      "rise": "2015-06-30T03:46:57",
      "set": "2015-06-30T20:21:12"
    }
  },
  "temperature": {
    "value": "72.34",
    "min": "66.2",
    "max": "79.88",
    "unit": "fahrenheit"
  },
  "humidity": {
    "value": "43",
    "unit": "%"
  },
  "pressure": {
    "value": "1020",
    "unit": "hPa"
  },
  "wind": {
    "speed": {
      "value": "7.78",
      "name": "Moderate breeze"
    },
    "direction": {
      "value": "140",
      "code": "SE",
      "name": "SouthEast"
    }
  },
  "clouds": {
    "value": "0",
    "name": "clear sky"
  },
  "visibility": {
    "value": "10000"
  },
  "precipitation": {
    "mode": "no"
  },
  "weather": {
    "number": "800",
    "value": "Sky is Clear",
    "icon": "01d"
  },
  "lastupdate": {
    "value": "2015-06-30T08:36:14"
  }
}
```
