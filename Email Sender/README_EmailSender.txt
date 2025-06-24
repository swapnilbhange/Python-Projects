# 📧 Python Email Sender using SMTP

This script allows you to send a plain text email using Gmail's SMTP server directly from the terminal. It uses Python's built-in `smtplib` for communication with the email server.

---

## 🚀 Features

- Send emails via Gmail SMTP
- Accepts recipient address and message content from the user
- Secure connection using TLS encryption
- Lightweight and easy to run

---

## 🛠️ How to Use

1. Open your terminal or command prompt.
2. Make sure Python 3 is installed.
3. Save the script as `send_email.py`.
4. Edit the file to replace:
   ```python
   server.login('senderemail@gmail.com', '1234')
   ```
   with your actual Gmail and **App Password**.
5. Run the script:

```bash
python send_email.py
```

6. Enter:
   - The recipient's email address
   - The content/message to be sent

---

## 📦 Requirements

- Python 3.x
- Internet access
- A Gmail account with:
  - 2-Step Verification enabled
  - App Password generated (not your Gmail password)

---

## 🔒 Security Notice

- ⚠️ Never hardcode passwords in real-world scripts.
- ✅ Use environment variables or a secure secrets manager.
- ❌ Avoid using your main Gmail password.

---

## 📝 Example Prompt

```plaintext
Enter the Email of Recipient:
someone@example.com
Enter the Content of mail:
Hello, this is an automated message from Python!
```

---

## 💡 Future Enhancements

- Support for email subject, CC, and attachments
- Add HTML content formatting
- Error handling and logging
- GUI for user-friendly usage

---

Use this script to automate alerts, reports, or notifications via email!