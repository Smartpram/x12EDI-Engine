class WorkflowManager:
    """
    A class to manage the EDI processing workflow.
    """

    def __init__(self, email_notifier):
        """
        Initializes the Workflow Manager.

        :param email_notifier: EmailNotification instance for sending notifications.
        """
        self.email_notifier = email_notifier

    def process_file(self, file_path, recipient_emails):
        """
        Processes the EDI file and sends email notifications.

        :param file_path: Path to the EDI file.
        :param recipient_emails: List of recipient email addresses.
        :return: Processing result.
        """
        try:
            # Step 1: Read X12 EDI File
            source_config = {"path": file_path}
            encryption_key = Fernet.generate_key()  # Store this securely
            connector = EDISourceConnector("local", source_config, encryption_key)
            x12_data = connector.read_file(file_path)

            # Step 2: Parse X12 EDI Data
            x12_parser = X12EDIParser()
            parsed_data = x12_parser.parse(x12_data)

            # Step 3: Validate Parsed Data
            validation_engine = ValidationEngine()
            errors = validation_engine.validate(parsed_data["data"])
            if errors:
                raise Exception(f"Validation Errors: {errors}")

            # Step 4: Transform to XML
            transformation_engine = TransformationEngine()
            xml_output = transformation_engine.transform_to_xml(parsed_data["data"])

            # Step 5: Send Success Email
            subject, body = EmailTemplates.success_template(file_path, xml_output)
            self.email_notifier.send_email(recipient_emails, subject, body)

            return {"status": "success", "xml_output": xml_output}
        except Exception as e:
            # Step 6: Send Error Email
            subject, body = EmailTemplates.error_template(file_path, str(e))
            self.email_notifier.send_email(recipient_emails, subject, body)
            return {"status": "error", "error": str(e)}
