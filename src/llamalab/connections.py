class Cloud:
    """
    To use Automate Cloud  you need a secret google account key,
    get one here:
    https://llamalab.com/automate/cloud/
    """

    @staticmethod
    def send(secret: str, addressee: str, payload: str, device: str = None, priority: str = "normal"):
        """
        Messages can be sent to Automate from any source capable of making HTTP requests.
        A message is sent using the POST method to URL https://llamalab.com/automate/cloud/message with either a webform or JSON body, see example requests below.
        Check out cURL, a common tool for making HTTP request available on most systems.

        :param secret: From Google account — name of Google account to send message as.
        :param addressee: To Google account — name (e-mail) of recipient Google account.
        :param payload:  Payload — payload passed to the recipient, maximum size is 2 KB.
        :param device:  To device — brand of recipient device, case-sensitive, default is all devices.
        :param priority:  Priority — whether to request “high priority” delivery, possibly awakening the recipient device. Use sparingly as it may be throttled by Google.
        """

        from json import dumps
        from requests import post

        return post(
            "https://llamalab.com/automate/cloud/message", data={
                "secret": secret,
                "to": addressee,
                "device": device,
                "priority": priority,
                "payload": dumps(payload) if type(payload) in [dict, list, set] else payload
            }
        )
