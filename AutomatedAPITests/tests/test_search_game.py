from make_request import make_request


class TestSearch:
    def test_search_game(self):
        response = make_request()
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
