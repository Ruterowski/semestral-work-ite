from src.serverCommunication import checkServerStatusConnection

class TestServerConnection():

    def test_connect_to_server(self):
        result = checkServerStatusConnection()
        assert result.text == "Connection established"
        assert result.status_code == 200

