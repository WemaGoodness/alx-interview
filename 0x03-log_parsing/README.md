# 0x03. Log Parsing

This project implements a Python script that parses log data from standard input and computes specific metrics. The script reads logs line by line and outputs the total file size and counts of specific HTTP status codes after every 10 lines or upon receiving a keyboard interrupt (CTRL + C).

## Project Overview

The script is designed to handle log data in real-time, processing each line of input to extract important information such as the file size and status codes. The metrics computed include:

- **Total file size**: The cumulative size of all files processed.
- **Status code counts**: The number of occurrences of specific HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).

The script prints these metrics after processing every 10 lines and also when interrupted by a keyboard signal (CTRL + C).

## Usage

The script reads from standard input and expects log lines to be in a specific format. The script can be used in a pipeline with other commands or scripts that generate log lines.
