## Features
- Encrypted user authorizaton
- Database initialization
- New user signup
- User login/logout
- User settings
- Modern user interface
- Bulma framework
- Limited custom css/js
- Easily customizable

## CTF-Features
- Bad implementation of mail-based 2FA
- Only the default account (admin:admin) is admin, no way to elevate privileges
- Target is to login as first account by bypassing 2FA

## Setup
``` 
git clone https://github.com/xJasonxy/weak2fa-for-ctf
cd weak2fa-for-ctf
pip install -r requirements.txt
python app.py
```