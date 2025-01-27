import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotification:
    """
    A class to send customizable email notifications.
    """

    def __init__(self, smtp_host, smtp_port, sender_email, sender_password):
        """
        Initializes the Email Notification Module.

        :param smtp_host: SMTP server host.
        :param smtp_port: SMTP server port.
        :param sender_email: Sender email address.
        :param sender_password: Sender email password.
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_emails, subject, body):
        """
        Sends an email to the specified recipients.

        :param recipient_emails: List of recipient email addresses.
        :param subject: Email subject.
        :param body: Email body.
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = ", ".join(recipient_emails)
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()  # Enable TLS encryption
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_emails, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

class EmailTemplates:
    """
    A class to define customizable email templates for success and error notifications.
    """

    @staticmethod
    def success_template(file_name, processed_data):
        """
        Template for successful processing.

        :param file_name: Name of the processed file.
        :param processed_data: Processed data.
        :return: Email subject and body.
        """
        subject = f"Success: EDI File {file_name} Processed"
        body = f"""
        Dear Recipient,

        The EDI file {file_name} has been successfully processed.

        Processed Data:
        {processed_data}

        Best regards,
        Your EDI System
        """
        return subject, body

    @staticmethod
    def error_template(file_name, error_message):
        """
        Template for error notifications.

        :param file_name: Name of the file that failed processing.
        :param error_message: Error message.
        :return: Email subject and body.
        """
        subject = f"Error: EDI File {file_name} Processing Failed"
        body = f"""
        Dear Recipient,

        The EDI file {file_name} could not be processed due to the following error:

        Error Message:
        {error_message}

        Please review the file and try again.

        Best regards,
        Your EDI System
        """
        return subject, body
