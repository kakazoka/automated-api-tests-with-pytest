from make_request import make_request


class TestSearch:
    def test_search_development_team(self):
        response = make_request(path_parameter='development-team')
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0
