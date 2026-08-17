# Zoom Chat Log Parser

A Python utility that parses unstructured Zoom chat log text files and transforms the extracted chat messages into structured CSV data.

The parser uses Regular Expressions to identify chat timestamps, sender, recipient, message type, and message content while also capturing input-file date metadata.

---

## What It Does

The utility processes a Zoom chat log through the following flow:

```text
Zoom Chat TXT File
        ↓
Read File
        ↓
Regex-based Parsing
        ↓
Data Transformation
        ↓
Structured Records
        ↓
CSV Output
```

For each parsed chat message, the output contains:

* Input file created date
* Input file last modified date
* Chat time
* Sender
* Recipient
* Message type
* Message

---

## Example Input

The parser expects chat entries following a structure similar to:

```text
10:15:32 From Alice to Bob:
Hello Bob, can you share the report?

10:16:04 From Bob to Alice:
Sure, I'll send it shortly.
```

The Regular Expression extracts the timestamp, sender, recipient, optional message type, and message content from each entry.

---

## Example Output

The extracted information is written to a CSV file with the following columns:

```text
Input_file_created_date
Input_file_last_modified_date
Chat_time
From
To
Message_type
Message
```

Example:

| Chat_time | From  | To    | Message_type | Message                              |
| --------- | ----- | ----- | ------------ | ------------------------------------ |
| 10:15:32  | Alice | Bob   |              | Hello Bob, can you share the report? |
| 10:16:04  | Bob   | Alice |              | Sure, I'll send it shortly.          |

---

## Technologies

* Python
* Regular Expressions (`re`)
* File Handling
* CSV
* `datetime`
* `os`

---

## Processing

The project is organized into focused functions:

### `transform_data()`

Parses the input text using Regular Expressions and transforms each matched chat entry into a structured dictionary.

### `write_to_csv()`

Writes the transformed records into a CSV file using Python's `csv.DictWriter`.

### `text_parser()`

Coordinates reading the input text file, transforming its contents, and generating the CSV output.

### `main()`

Collects the input and output paths and starts the parsing process.

---

## Getting Started

### Requirements

* Python 3.10+
* No external Python packages are required.

### Run the utility

From the project directory:

```bash
python main.py
```

The program will request:

```text
text_file_in_path >>
csv_file_out_path >>
```

Example:

```text
text_file_in_path >> "C:\Users\User\zoom_chat_input\meeting_saved_chat (1).txt"
csv_file_out_path >> "C:\Users\User\zoom_chat_output"
```

The generated CSV file is named using the current date:

```text
YYYY-MM-DD.csv
```

---

## Purpose

This project demonstrates practical Python-based text processing and data transformation by converting semi-structured chat logs into structured, analytics-friendly CSV data.

It highlights the use of Regular Expressions, file handling, structured Python data types, metadata extraction, and CSV generation in a small end-to-end data processing workflow.
