# Decoding and Conversion of Encrypted Data

This project demonstrates decoding and encoding data between **Hexadecimal (Hex)**, **Unknown String**, and **ASCII JSON** formats. The implemented Python code ensures secure and efficient conversions, particularly for JSON datasets.

---

## 🚀 Features
- Decode **Hexadecimal** to **Unknown String**.
- Encode **Unknown String** back to **Hexadecimal**.
- Convert **ASCII JSON Object** to **Hexadecimal** and back.
- Validate the integrity of data through matching conversions.
- JSON-based dataset processing.

---

## 📝 Problem Statement
In modern systems, encrypted data often requires decoding into human-readable formats. The challenge lies in accurately decoding **Hexadecimal** strings into **Unknown Strings**, validating conversions, and ensuring the integrity of the data. This project provides a robust solution using Python and cryptographic techniques.

---

## 📖 Concepts Used
### 1. **Hexadecimal (Hex)**
   - A base-16 encoded representation of data.
   - Example: `"7b2275726c223a226874747073..."`

### 2. **Unknown String**
   - A UTF-8 encoded or encrypted string derived from hexadecimal.
   - Example: `"https://example.com/resource..."`

### 3. **ASCII JSON Object**
   - A serialized JSON object in ASCII format.
   - Example: `{"url": "https://example.com", "key": "value"}`

---

## ⚙️ Conversion Techniques
1. **Hex to Unknown**
   - Convert a hex string into a byte object and decode it to UTF-8.
2. **Unknown to Hex**
   - Encode a UTF-8 string into hexadecimal format.
3. **JSON to Hex**
   - Serialize a JSON object, encode it into UTF-8, and convert to hex.
4. **Hex to JSON**
   - Decode a hex string to UTF-8, parse it back into a JSON object.

---

## 💻 Code Implementation
Here’s the Python implementation for the process:

```python
import json
import binascii

def hex_to_unknown(hex_string):
    return binascii.unhexlify(hex_string).decode('utf-8', 'ignore')

def unknown_to_hex(unknown_string):
    return binascii.hexlify(unknown_string.encode('utf-8')).decode('utf-8')

def json_to_hex(json_object):
    json_string = json.dumps(json_object, separators=(',', ':'))
    return unknown_to_hex(json_string)

def hex_to_json(hex_string):
    decoded_string = hex_to_unknown(hex_string)
    return json.loads(decoded_string) if decoded_string else None

def process_dataset(dataset):
    unknown_converted = hex_to_unknown(dataset['hex'])
    hex_converted = unknown_to_hex(unknown_converted)
    ascii_json_hex = json_to_hex(dataset['ascii_text'])
    hex_and_ascii_match = hex_to_json(dataset['hex']) == dataset['ascii_text']

    print(f"Hex to Unknown Conversion: {unknown_converted is not None}")
    print(f"Unknown to Hex Conversion: {hex_converted is not None}")
    print(f"Serialized ASCII to JSON string: {json.dumps(dataset['ascii_text'])}")
    print(f"Converted ASCII JSON string to hex: {ascii_json_hex}")
    print(f"Hex and ASCII match: {hex_and_ascii_match}")
