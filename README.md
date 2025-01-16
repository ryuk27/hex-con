# Decoding and Conversion of Encrypted Data

This project demonstrates the conversion of data between **Hexadecimal (Hex)**, **Unknown String**, and **ASCII Text** formats. It aims to showcase how cryptographic principles can be applied to decode and encode data securely for practical applications.

---

## 🚀 Features
- Conversion of **Hexadecimal** to **Unknown String**.
- Decoding of **Unknown String** to **ASCII Text**.
- Reverse conversion of **ASCII Text** to **Hexadecimal**.
- Python-based implementation of encoding and decoding techniques.
- Cryptographic relevance for secure data transmission.

---

## 📝 Problem Statement
Data is often transmitted in encrypted formats like **unknown strings** to ensure security. These strings must be decoded to a readable format (e.g., **ASCII**) using **Hexadecimal** as an intermediary format. This project provides a solution to this problem using Python, enabling secure and efficient data conversion.

---

## 📖 Concepts Used
### 1. **Unknown String**
- An encrypted or encoded text format, unreadable by humans.
- Example: `"d8ab19d5c7a0f27c..."`

### 2. **Hexadecimal (Hex)**
- A base-16 format that represents binary data in a human-readable way.
- Example: `"7b2275726c223a226874747073..."`

### 3. **ASCII Text**
- A human-readable character encoding standard.
- Example: `{"url": "https://example.com", "hash": "0777fff783810100..."}`

---

## ⚙️ Conversion Process
1. **Hexadecimal to Unknown String**
   - Decode the hex string into bytes.
2. **Unknown String to ASCII Text**
   - Parse the bytes into a readable JSON or text format.
3. **ASCII Text to Hexadecimal**
   - Encode the ASCII string back into hexadecimal for secure storage or transmission.

---

## 🛠️ Technologies Used
- **Python**: Programming language for implementation.
- **JSON**: Data serialization format.
- **Cryptographic Libraries**: For encoding and decoding functions.

---

## 💻 Code Example
Here’s a Python snippet for the conversion process:

```python
import json

def hex_to_unknown(hex_string):
    return bytes.fromhex(hex_string).decode('utf-8')

def unknown_to_ascii(unknown_string):
    return json.loads(unknown_string)

def ascii_to_hex(ascii_string):
    return ascii_string.encode('utf-8').hex()

# Example Usage
hex_data = "7b2275726c223a226874747073..."
unknown = hex_to_unknown(hex_data)
ascii_text = unknown_to_ascii(unknown)
hex_again = ascii_to_hex(ascii_text)
print(f"Original Hex: {hex_data}")
print(f"Decoded ASCII: {ascii_text}")
print(f"Re-encoded Hex: {hex_again}")
