from flask import Flask, Response
import json
from functools import lru_cache
from my_package.figure_data import get_fig_data
from my_package.entry_data import get_entry_data, get_entry_max_page_number
from my_package.owned_collection_data import get_owned_figure_by_uname, get_owned_collection_max_page
from my_package.ordered_collection_data import get_ordered_figure_by_uname, get_ordered_collection_max_page
from my_package.wished_collection_data import get_wished_figure_by_uname, get_wished_collection_max_page
from my_package.latest_figure_data import get_latest_figure, get_latest_max_page
from my_package.onfire_data import get_onfire_figure
from my_package.most_wished_data import get_most_wished_figure
from my_package.most_ordered_data import get_most_ordered_figure
from my_package.most_owned_data import get_most_owned_figure
from my_package.most_rated_data import get_most_rated_figure
from my_package.most_viewed_data import get_most_viewed_figure
from my_package.releases_data import get_releases_date_figure, get_releases_date_max_page_number
from my_package.profile import get_profile_data

class KuroRest:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/items/<item_id>', 'get_item_data', self.get_item_data)
        self.app.add_url_rule('/entry/<entry_id>/<page_number>', 'get_entry', self.get_entry)
        self.app.add_url_rule('/profile/<username>/collection/owned/<page_number>', 'get_owned_collection_by_uname', self.get_owned_collection_by_uname)
        self.app.add_url_rule('/profile/<username>/collection/ordered/<page_number>', 'get_ordered_collection_by_uname', self.get_ordered_collection_by_uname)
        self.app.add_url_rule('/profile/<username>/collection/wished/<page_number>', 'get_wished_collection_by_uname', self.get_wished_collection_by_uname)
        self.app.add_url_rule('/items/latest/<page_number>', 'latest_figure', self.latest_figure)
        self.app.add_url_rule('/items/onfire', 'get_onfire', self.get_onfire)
        self.app.add_url_rule('/items/most_wished', 'most_wished', self.most_wished)
        self.app.add_url_rule('/items/most_ordered', 'most_ordered', self.most_ordered)
        self.app.add_url_rule('/items/most_owned', 'most_owned', self.most_owned)
        self.app.add_url_rule('/items/most_rated', 'most_rated', self.most_rated)
        self.app.add_url_rule('/items/most_viewed', 'most_viewed', self.most_viewed)
        self.app.add_url_rule('/items/releases/<year>/<month>/<page_number>', 'releases', self.releases)
        self.app.add_url_rule('/profile/<username>', 'profile', self.profile)
    
    def run(self, debug=True, port=9192):
        self.app.run(debug=debug, port=port)
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_item_data(item_id):
        fig_data = get_fig_data(item_id)
        fig_data_json = json.dumps(fig_data, indent=4)
        return Response(fig_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_entry(entry_id, page_number):
        entry_data = get_entry_data(entry_id, page_number)
        max_page_number = get_entry_max_page_number(entry_id)

        entry_data['max_page_number'] = max_page_number
        entry_data_json = json.dumps(entry_data, indent=4)

        return Response(entry_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_owned_collection_by_uname(username, page_number):
        owned_data = get_owned_figure_by_uname(username, page_number)
        max_page_number = get_owned_collection_max_page(username)

        owned_data['max_page_number'] = max_page_number
        owned_data_json = json.dumps(owned_data, indent=4)

        return Response(owned_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_ordered_collection_by_uname(username, page_number):
        ordered_data = get_ordered_figure_by_uname(username, page_number)
        max_page_number = get_ordered_collection_max_page(username)

        ordered_data['max_page_number'] = max_page_number
        ordered_data_json = json.dumps(ordered_data, indent=4)

        return Response(ordered_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_wished_collection_by_uname(username, page_number):
        wished_data = get_wished_figure_by_uname(username, page_number)
        max_page_number = get_wished_collection_max_page(username)

        wished_data['max_page_number'] = max_page_number
        wished_data_json = json.dumps(wished_data, indent=4)

        return Response(wished_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def latest_figure(page_number):
        latest_figure_data = get_latest_figure(page_number)
        max_page_number = get_latest_max_page()

        latest_figure_data['max_page_number'] = max_page_number
        latest_figure_data_json = json.dumps(latest_figure_data, indent=4)

        return Response(latest_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_onfire():
        onfire_figure_data = get_onfire_figure()

        onfire_figure_data_json = json.dumps(onfire_figure_data, indent=4)

        return Response(onfire_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def most_wished():
        most_wished_figure_data = get_most_wished_figure()

        most_wished_figure_data_json = json.dumps(most_wished_figure_data, indent=4)

        return Response(most_wished_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def most_ordered():
        most_ordered_figure_data = get_most_ordered_figure()

        most_ordered_figure_data_json = json.dumps(most_ordered_figure_data, indent=4)

        return Response(most_ordered_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def most_owned():
        most_owned_figure_data = get_most_owned_figure()

        most_owned_figure_data_json = json.dumps(most_owned_figure_data, indent=4)

        return Response(most_owned_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def most_rated():
        most_rated_figure_data = get_most_rated_figure()

        most_rated_figure_data_json = json.dumps(most_rated_figure_data, indent=4)

        return Response(most_rated_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def most_viewed():
        most_viewed_figure_data = get_most_viewed_figure()

        most_viewed_figure_data_json = json.dumps(most_viewed_figure_data, indent=4)

        return Response(most_viewed_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def releases(year, month, page_number):
        releases_data_data = get_releases_date_figure(year, month, page_number)
        max_page_number = get_releases_date_max_page_number(year, month, page_number)

        releases_data_data['max_page_number'] = max_page_number
        releases_data_data_json = json.dumps(releases_data_data, indent=4)

        return Response(releases_data_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def profile(username):
        profile_data = get_profile_data(username)

        profile_data_json = json.dumps(profile_data, indent=4)

        return Response(profile_data_json, mimetype='application/json')


# http://127.0.0.1:9192/items/945912 {TEST ITEM}
# http://127.0.0.1:9192/entry/7620/1 {TEST ENTRY}
# http://127.0.0.1:9192/profile/LalaBunnyLand/collection/owned/1 {TEST OWNED}
# http://127.0.0.1:9192/profile/LalaBunnyLand/collection/ordered/1 {TEST ORDERED}
# http://127.0.0.1:9192/profile/bukanyayan/collection/wished/1 {TEST WISHED}
# http://127.0.0.1:9192/items/latest/1 {TEST LATEST}
# http://127.0.0.1:9192/items/onfire {TEST ONFIRE}
# http://127.0.0.1:9192/items/most_wished {TEST MOST WISHED}
# http://127.0.0.1:9192/items/most_ordered {TEST MOST ORDERED}
# http://127.0.0.1:9192/items/most_owned {TEST MOST OWNED}
# http://127.0.0.1:9192/items/most_rated {TEST MOST RATED}
# http://127.0.0.1:9192/items/most_viewed {TEST MOST VIEWED}
# http://127.0.0.1:9192/items/releases/2024/3/1 {TEST RELEASES}
# http://127.0.0.1:9192/profile/LalaBunnyLand {TEST PROFILE}
