import json
import binascii


def hex_to_unknown(hex_string):
    try:
        # Convert the hex string to a byte object and then decode it to a string
        decoded_bytes = binascii.unhexlify(hex_string)
        decoded_string = decoded_bytes.decode('utf-8', 'ignore')  # ignore errors for invalid UTF-8
        return decoded_string
    except Exception as e:
        print(f"Error during hex to unknown conversion: {e}")
        return None


def unknown_to_hex(unknown_string):
    try:
        # Convert the unknown string (ASCII) to bytes and then to hex
        hex_string = binascii.hexlify(unknown_string.encode('utf-8')).decode('utf-8')
        return hex_string
    except Exception as e:
        print(f"Error during unknown to hex conversion: {e}")
        return None


def json_to_hex(json_object):
    # Convert the JSON object to a string and then to hex
    json_string = json.dumps(json_object, separators=(',', ':'))
    return unknown_to_hex(json_string)


def hex_to_json(hex_string):
    # Convert hex to bytes and then decode to string
    decoded_string = hex_to_unknown(hex_string)
    if decoded_string:
        try:
            return json.loads(decoded_string)  # Convert string back to JSON object
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from string: {e}")
            return None
    return None


def process_dataset(dataset):
    try:
        # Convert hex to unknown string
        unknown_converted = hex_to_unknown(dataset['hex'])
        if unknown_converted:
            print(f"Hex to Unknown Conversion: True")

        # Convert unknown back to hex
        hex_converted = unknown_to_hex(unknown_converted)
        if hex_converted:
            print(f"Unknown to Hex Conversion: True")

        # Convert serialized ASCII JSON to hex and back to a JSON object
        ascii_json = dataset['ascii_text']
        ascii_json_hex = json_to_hex(ascii_json)
        print(f"Serialized ASCII to JSON string: {json.dumps(ascii_json)}")
        print(f"Converted ASCII JSON string to hex: {ascii_json_hex}")

        # Convert the hex back to the original JSON object
        hex_and_ascii_match = hex_to_json(dataset['hex']) == ascii_json
        print(f"Hex and ASCII match: {hex_and_ascii_match}")

        print(f"Dataset {dataset} processed successfully.")

    except KeyError as e:
        print(f"KeyError: Missing key {e} in dataset")
    except Exception as e:
        print(f"Error processing dataset: {e}")


def main():
    # Loading the JSON dataset
    try:
        with open('package.json', 'r') as f:
            datasets = json.load(f)

        # Iterate through the datasets and process each one
        for index, dataset in datasets.items():
            print(f"Processing Dataset {index}...")
            process_dataset(dataset)

    except Exception as e:
        print(f"Error reading the JSON file: {e}")


if __name__ == "__main__":
    main()
