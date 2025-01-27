# X12 EDI Interface Engine Solution

A fully integrated X12 EDI processing system built in Python. This solution reads, parses, validates, and transforms X12 EDI files into XML. It also includes secure data handling, concurrent processing, and customizable email notifications for success and error events.

---

## Features

- **EDI Source Connector**: Reads X12 EDI files from local storage, FTP, or SFTP.
- **X12 EDI Parser**: Parses X12 EDI files into an internal JSON/XML format.
- **Validation Engine**: Validates parsed data against X12 standards and trading partner rules.
- **Transformation Engine**: Transforms parsed data into XML.
- **EDI Transformer**: Exposes parsing and transformation capabilities via a user-friendly interface.
- **Integration Layer**: Sends transformed data to backend systems securely.
- **Encryption Module**: Encrypts and decrypts data at rest and in transit.
- **Thread Pool Manager**: Handles multiple threads for concurrent processing.
- **Error Handling and Logging**: Logs errors and provides detailed reports.
- **Email Notification Module**: Sends customizable email notifications for success and error events.

---

## Folder Structure

```
x12-edi-engine/
├── src/
│   ├── edi_source_connector.py
│   ├── x12_edi_parser.py
│   ├── validation_engine.py
│   ├── transformation_engine.py
│   ├── edi_transformer.py
│   ├── integration_layer.py
│   ├── encryption_module.py
│   ├── thread_pool_manager.py
│   ├── error_handler.py
│   ├── email_notification.py
│   ├── workflow_manager.py
│   └── __init__.py
├── tests/
│   ├── test_edi_source_connector.py
│   ├── test_x12_edi_parser.py
│   ├── test_validation_engine.py
│   ├── test_transformation_engine.py
│   ├── test_edi_transformer.py
│   ├── test_integration_layer.py
│   ├── test_encryption_module.py
│   ├── test_thread_pool_manager.py
│   ├── test_error_handler.py
│   ├── test_email_notification.py
│   └── test_workflow_manager.py
├── config/
│   ├── smtp_config.json
│   └── api_config.json
├── logs/
│   └── edi_errors.log
├── requirements.txt
├── README.md
└── main.py
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/x12-edi-engine.git
   cd x12-edi-engine
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure SMTP and API Settings**:
   - Update `config/smtp_config.json` with your SMTP server details.
   - Update `config/api_config.json` with your backend API endpoint and API key.

4. **Run the Solution**:
   ```bash
   python main.py
   ```

---

## Usage

### Example: Processing an X12 EDI File
```python
from src.workflow_manager import WorkflowManager
from src.email_notification import EmailNotification

# Configure Email Notifier
smtp_host = "smtp.example.com"
smtp_port = 587
sender_email = "your_email@example.com"
sender_password = "your_password"
recipient_emails = ["recipient1@example.com", "recipient2@example.com"]

email_notifier = EmailNotification(smtp_host, smtp_port, sender_email, sender_password)

# Process File
workflow_manager = WorkflowManager(email_notifier)
result = workflow_manager.process_file("example_810.edi", recipient_emails)

# Display Result
print("Processing Result:", result)
```

---

## Dependencies

- Python 3.8+
- Libraries:
  - `pyx12` (for X12 parsing)
  - `paramiko` (for SFTP support)
  - `cryptography` (for encryption)
  - `requests` (for API integration)
  - `smtplib` and `email` (for email notifications)
  - `concurrent.futures` (for thread pool management)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Configuration

### SMTP Configuration (`config/smtp_config.json`)
```json
{
  "smtp_host": "smtp.example.com",
  "smtp_port": 587,
  "sender_email": "your_email@example.com",
  "sender_password": "your_password"
}
```

### API Configuration (`config/api_config.json`)
```json
{
  "api_endpoint": "https://example.com/api",
  "api_key": "your_api_key"
}
```

---

## Logs

All errors and processing logs are stored in `logs/edi_errors.log`.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---


