from src.serverCommunication import checkServerStatusConnection

class TestServerConnection:
    """
    Test class for server connection.
    """
    def test_connect_to_server(self):
        """
        Test, successfully connected to server.
        """
        result = checkServerStatusConnection()
        assert result.text == "Connection established"
        assert result.status_code == 200

