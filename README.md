
# 🚀 MicroJet - Modern Python Web Framework

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Alpha](https://img.shields.io/badge/Status-Alpha-orange)]()

> একটি হালকা, দ্রুত এবং React-এর মত কম্পোনেন্ট সিস্টেম সহ Python ওয়েব ফ্রেমওয়ার্ক

```
╔════════════════════════════════════════════════════════════╗
║              🌟 MicroJet Framework 🌟                      ║
║           NOTE:This project is in under construction, so please do not use it now.(We will let you know when it will be available here.)            ║
║                                        ║
╚════════════════════════════════════════════════════════════╝
```

## 📋 বিষয়বস্তু

- [বৈশিষ্ট্য](#-বৈশিষ্ট্য)
- [দ্রুত শুরু](#-দ্রুত-শুরু)
- [CLI কমান্ড](#-cli-কমান্ড)
- [উদাহরণ](#-উদাহরণ)
- [আর্কিটেকচার](#-আর্কিটেকচার)
- [ডকুমেন্টেশন](#-ডকুমেন্টেশন)

---

## ✨ বৈশিষ্ট্য

### 🎯 মূল সুবিধা

- **সহজ Routing** - Bottle.py এর মত decorator-based সিস্টেম
- **React-like কম্পোনেন্ট** - পুনর্ব্যবহারযোগ্য, পুনর্সংযোজনযোগ্য UI কম্পোনেন্ট
- **বিল্ট-ইন কম্পোনেন্ট লাইব্রেরি** - Button, Card, Form, NavBar, Alert ইত্যাদি
- **শক্তিশালী CLI** - প্রজেক্ট এবং কম্পোনেন্ট ম্যানেজমেন্ট
- **স্টেটিক ফাইল সাপোর্ট** - CSS, JavaScript, ছবি সেবা করা
- **কোনো ডিপেন্ডেন্সি নেই** - শুধু Python স্ট্যান্ডার্ড লাইব্রেরি!
- **দ্রুত ডেভেলপমেন্ট** - প্রোটোটাইপ দ্রুত তৈরি করুন
- **সহজ ডিপ্লয়মেন্ট** - WSGI সামঞ্জস্যপূর্ণ

---

## 🚀 দ্রুত শুরু

### Step 1: ফাইল ডাউনলোড করুন

```bash
# মূল ফাইলগুলি ডাউনলোড করুন
# - microjet_core.py
# - jet (CLI টুল)
```

### Step 2: নতুন প্রজেক্ট তৈরি করুন

```bash
./jet new my_awesome_app
cd my_awesome_app
```

এটি নিম্নলিখিত স্ট্রাকচার তৈরি করবে:
```
my_awesome_app/
├── app.py              # মূল অ্যাপ্লিকেশন
├── components/         # রিইউজেবল কম্পোনেন্ট
├── static/            # CSS, JS, ছবি
├── jet.json           # প্রজেক্ট কনফিগারেশন
└── README.md          # প্রজেক্ট ডকুমেন্টেশন
```

### Step 3: কম্পোনেন্ট ইনস্টল করুন (Optional)

```bash
./jet install button
./jet install card
./jet install form
./jet install navbar
./jet install alert
```

### Step 4: ডেভেলপমেন্ট সার্ভার চালান

```bash
./jet run
```

আপনার ব্রাউজারে খুলুন: **http://localhost:8000** 🎉

---

## 📱 CLI কমান্ড

```bash
jet new <project_name>    # নতুন প্রজেক্ট তৈরি করুন
jet install <component>   # কম্পোনেন্ট ইনস্টল করুন
jet run                    # ডেভেলপমেন্ট সার্ভার চালান
jet list                   # সব কম্পোনেন্ট দেখুন
jet --help                 # সাহায্য পান
```

### উদাহরণ

```bash
# নতুন ব্লগ প্রজেক্ট তৈরি করুন
$ jet new my_blog

# প্রজেক্টে যান
$ cd my_blog

# কম্পোনেন্ট ইনস্টল করুন
$ jet install navbar
$ jet install card

# সার্ভার চালান
$ jet run
```

---

## 💡 উদাহরণ

### সহজ "Hello World" অ্যাপ

```python
from microjet_core import MicroJet, h1, div

app = MicroJet("Hello App")

@app.route("/")
def home():
    page = div()
    title = h1()
    title.add_child("Hello, MicroJet! 👋")
    page.add_child(title)
    return f"<!DOCTYPE html><html><body>{page.to_html()}</body></html>"

if __name__ == "__main__":
    app.run()
```

### প্যারামিটার সহ রুট

```python
@app.route("/greet/:name")
def greet(name):
    page = div()
    msg = h1()
    msg.add_child(f"Hello, {name}!")
    page.add_child(msg)
    return f"<!DOCTYPE html><html><body>{page.to_html()}</body></html>"

# ব্রাউজারে যান: http://localhost:8000/greet/আলি
```

### কাস্টম কম্পোনেন্ট তৈরি করুন

```python
# components/welcome.py
from microjet_core import HtmlComponent

class WelcomeCard(HtmlComponent):
    def __init__(self, name, props=None):
        super().__init__("div", props or {"className": "welcome-card"})
        self.name = name
    
    def render(self):
        title = HtmlComponent("h2")
        title.add_child(f"স্বাগতম, {self.name}!")
        self.add_child(title)
        return self

# app.py
from components.welcome import WelcomeCard

@app.route("/")
def home():
    card = WelcomeCard("আবদুল")
    card.render()
    return f"<!DOCTYPE html><html><body>{card.to_html()}</body></html>"
```

### API এন্ডপয়েন্ট

```python
@app.route("/api/users")
def get_users():
    return {
        "users": [
            {"id": 1, "name": "আলি"},
            {"id": 2, "name": "ফাতিমা"}
        ]
    }

# http://localhost:8000/api/users এ অ্যাক্সেস করুন
# JSON রেসপন্স পাবেন
```

---

## 🏗️ আর্কিটেকচার

### ফাইল স্ট্রাকচার

```
MicroJet/
├── microjet_core.py       # মূল ফ্রেমওয়ার্ক (~250 লাইন)
├── jet                    # CLI টুল (~350 লাইন)
├── MICROJET_DOCS.md       # বিস্তারিত ডকুমেন্টেশন
├── INSTALLATION.md        # ইনস্টলেশন গাইড
├── example_blog_app.py    # সম্পূর্ণ ব্লগ উদাহরণ
├── setup.py              # প্যাকেজ সেটআপ
└── README.md             # এই ফাইল
```

### কোর কম্পোনেন্ট

#### 1. **Component Class** - বেস ক্লাস
```python
class Component:
    - render()      # রেন্ডার করুন
    - to_html()     # HTML তে রূপান্তর করুন
    - add_child()   # চাইল্ড যোগ করুন
    - set_prop()    # প্রপার্টি সেট করুন
```

#### 2. **HtmlComponent** - HTML উপাদান
```python
class HtmlComponent(Component):
    - tag           # HTML ট্যাগ (div, p, h1, etc.)
    - props         # HTML অ্যাট্রিবিউট
    - children      # চাইল্ড এলিমেন্ট
```

#### 3. **MicroJet Class** - মূল অ্যাপ্লিকেশন
```python
class MicroJet:
    - route()            # রুট নিবন্ধন করুন
    - run()              # সার্ভার চালান
    - register_component() # কম্পোনেন্ট নিবন্ধন করুন
    - static()           # স্টেটিক ফাইল সেবা করুন
```

---

## 📚 ডকুমেন্টেশন

### ফাইল গাইড

| ফাইল | বিবরণ |
|------|--------|
| `MICROJET_DOCS.md` | সম্পূর্ণ ডকুমেন্টেশন এবং API রেফারেন্স |
| `INSTALLATION.md` | ইনস্টলেশন এবং সেটআপ গাইড |
| `example_blog_app.py` | একটি সম্পূর্ণ কাজের ব্লগ অ্যাপ্লিকেশন |

### দ্রুত রেফারেন্স

```python
# রুট নিবন্ধন
@app.route("/")
@app.route("/user/:name")
@app.route("/post/:id", methods=["GET", "POST"])

# কম্পোনেন্ট তৈরি
from microjet_core import div, p, h1, button, form

# কম্পোনেন্ট ব্যবহার
component.add_child(child)
component.set_prop("className", "my-class")
component.to_html()
```

---

## 🎓 শেখার রিসোর্স

### শিক্ষানবিসদের জন্য
1. এই README পড়ুন
2. `example_blog_app.py` চালান
3. `INSTALLATION.md` অনুসরণ করুন

### মধ্যবর্তী ব্যবহারকারীদের জন্য
1. `MICROJET_DOCS.md` এর সব অংশ পড়ুন
2. নিজের কম্পোনেন্ট তৈরি করুন
3. API এন্ডপয়েন্ট যোগ করুন

### উন্নত ব্যবহারকারীদের জন্য
1. `microjet_core.py` এর কোড বিশ্লেষণ করুন
2. কাস্টম মিডলওয়্যার লিখুন
3. নিজের কম্পোনেন্ট লাইব্রেরি তৈরি করুন

---

## 🛠️ প্রি-বিল্ট কম্পোনেন্ট

MicroJet এর সাথে আসা কম্পোনেন্ট:

```
button   - ক্লিকযোগ্য বাটন কম্পোনেন্ট
card     - কন্টেন্ট কার্ড কম্পোনেন্ট
form     - ফর্ম এবং ফিল্ড কম্পোনেন্ট
navbar   - নেভিগেশন বার কম্পোনেন্ট
alert    - নোটিফিকেশন অ্যালার্ট কম্পোনেন্ট
```

প্রতিটি প্রি-বিল্ট কম্পোনেন্ট সম্পূর্ণ কাস্টমাইজেবল এবং স্টাইল করা যায়।

---

## 🌍 বাস্তব বিশ্বের ব্যবহার

MicroJet দিয়ে আপনি তৈরি করতে পারেন:

- 📝 **ব্লগ প্ল্যাটফর্ম** - উদাহরণে দেখুন
- 🛒 **ই-কমার্স সাইট** - প্রোডাক্ট লিস্টিং এবং কার্ট
- 📊 **ড্যাশবোর্ড** - রিয়েল-টাইম ডেটা ভিজুয়ালাইজেশন
- 💬 **সোশ্যাল নেটওয়ার্ক** - পোস্ট এবং কমেন্ট সিস্টেম
- 🎓 **শিক্ষা প্ল্যাটফর্ম** - কোর্স ম্যানেজমেন্ট
- 🎮 **গেমিং পোর্টাল** - লিডারবোর্ড এবং প্রোফাইল

---

## 💻 সিস্টেম রিকোয়ারমেন্ট

- **Python** 3.7 বা তার উপরে
- **OS** - Linux, macOS, Windows সব সাপোর্টেড
- **Disk** - মাত্র ~50 KB
- **Memory** - ন্যূনতম

**কোনো বাহ্যিক ডিপেন্ডেন্সি প্রয়োজন নেই!**

---

## 📊 তুলনা

| ফিচার | Flask | Bottle | FastAPI | MicroJet |
|-------|-------|--------|---------|----------|
| সহজতা | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| কম্পোনেন্ট সিস্টেম | ❌ | ❌ | ❌ | ✅ |
| ডিপেন্ডেন্সি | অনেক | কয়েকটি | কয়েকটি | 0️⃣ |
| শেখা সহজ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| দ্রুত প্রোটোটাইপিং | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🤝 অবদান এবং সাপোর্ট

### অবদান রাখতে পারেন:
- 🐛 বাগ রিপোর্ট করুন
- 💡 নতুন ফিচার পরামর্শ দিন
- 📝 ডকুমেন্টেশন উন্নত করুন
- 🧩 নতুন কম্পোনেন্ট তৈরি করুন
- 🌍 অনুবাদ অবদান রাখুন

### সাহায্য পেতে:
- 📖 ডকুমেন্টেশন পড়ুন
- 💬 ইস্যু খুলুন
- 🔗 আলোচনায় যোগ দিন

---

## 📄 লাইসেন্স

MIT License - সম্পূর্ণ স্বাধীনতা!

আপনি যা চান করতে পারেন:
- ✅ ব্যবহার করুন
- ✅ পরিবর্তন করুন
- ✅ বিতরণ করুন
- ✅ বাণিজ্যিক ব্যবহার করুন

কোনো বিধিনিষেধ নেই!

---

## 🎉 পরবর্তী পদক্ষেপ

1. **শুরু করুন**: `jet new myapp` এবং `jet run`
2. **শিখুন**: ডকুমেন্টেশন পড়ুন এবং উদাহরণ চেষ্টা করুন
3. **তৈরি করুন**: আপনার নিজের প্রজেক্ট তৈরি করুন
4. **শেয়ার করুন**: আপনার সৃষ্টি বিশ্বের সাথে শেয়ার করুন
5. **অবদান রাখুন**: সম্প্রদায়কে সাহায্য করুন

---

## 🌟 বিশেষ ধন্যবাদ

এই প্রজেক্টটি অনুপ্রাণিত হয়েছে:
- **Bottle.py** এর সরলতা দ্বারা
- **React.js** এর কম্পোনেন্ট আর্কিটেকচার দ্বারা
- **Python** এর নমনীয়তা দ্বারা

---

## 📞 যোগাযোগ

- 📧 Email: dev@microjet.dev
- 🐦 Twitter: @microjetdev
- 💬 Discord: MicroJet সম্প্রদায়
- 🌐 Website: https://microjet.dev

---

<div align="center">

### 🚀 MicroJet দিয়ে আপনার পরবর্তী বড় প্রজেক্ট তৈরি করুন!

**সহজ। শক্তিশালী। আনন্দদায়ক।**

![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![Made with](https://img.shields.io/badge/Made%20with-%F0%9F%92%9C%20Python-blue?style=for-the-badge)

</div>
