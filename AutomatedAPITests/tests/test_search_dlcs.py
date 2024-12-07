from make_request import make_request


class TestSearch:
    def test_search_dlcs(self):
        response = make_request(path_parameter='additions')
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
