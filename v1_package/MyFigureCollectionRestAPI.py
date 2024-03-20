from flask import Flask, Response, render_template
import json
import os
from functools import lru_cache
from v1_package.figure_data import get_fig_data
from v1_package.entry_data import get_entry_data, get_entry_max_page_number
from v1_package.owned_collection_data import get_owned_figure_by_uname, get_owned_collection_max_page
from v1_package.ordered_collection_data import get_ordered_figure_by_uname, get_ordered_collection_max_page
from v1_package.wished_collection_data import get_wished_figure_by_uname, get_wished_collection_max_page
from v1_package.latest_figure_data import get_latest_figure, get_latest_max_page
from v1_package.onfire_data import get_onfire_figure
from v1_package.most_wished_data import get_most_wished_figure
from v1_package.most_ordered_data import get_most_ordered_figure
from v1_package.most_owned_data import get_most_owned_figure
from v1_package.most_rated_data import get_most_rated_figure
from v1_package.most_viewed_data import get_most_viewed_figure
from v1_package.releases_data import get_releases_date_figure, get_releases_date_max_page_number
from v1_package.profile import get_profile_data

class KuroRest:
    def __init__(self):
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
        static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
        self.app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
        self.app.add_url_rule('/', 'main', self.main)
        self.app.add_url_rule('/v1/items/<item_id>', 'get_item_data', self.get_item_data)
        self.app.add_url_rule('/v1/entry/<entry_id>/<page_number>', 'get_entry', self.get_entry)
        self.app.add_url_rule('/v1/profile/<username>/collection/owned/<page_number>', 'get_owned_collection_by_uname', self.get_owned_collection_by_uname)
        self.app.add_url_rule('/v1/profile/<username>/collection/ordered/<page_number>', 'get_ordered_collection_by_uname', self.get_ordered_collection_by_uname)
        self.app.add_url_rule('/v1/profile/<username>/collection/wished/<page_number>', 'get_wished_collection_by_uname', self.get_wished_collection_by_uname)
        self.app.add_url_rule('/v1/items/latest/<page_number>', 'get_latest_figure', self.get_latest_figure)
        self.app.add_url_rule('/v1/items/onfire', 'get_onfire', self.get_onfire)
        self.app.add_url_rule('/v1/items/most_wished', 'get_most_wished', self.get_most_wished)
        self.app.add_url_rule('/v1/items/most_ordered', 'get_most_ordered', self.get_most_ordered)
        self.app.add_url_rule('/v1/items/most_owned', 'get_most_owned', self.get_most_owned)
        self.app.add_url_rule('/v1/items/most_rated', 'get_most_rated', self.get_most_rated)
        self.app.add_url_rule('/v1/items/most_viewed', 'get_most_viewed', self.get_most_viewed)
        self.app.add_url_rule('/v1/items/releases/<year>/<month>/<page_number>', 'get_releases', self.get_releases)
        self.app.add_url_rule('/v1/profile/<username>', 'get_profile', self.get_profile)
    
    def run(self, debug=True, port=9192):
        self.app.run(debug=debug, port=port)

    def main(self):
        return render_template('index.html')
    
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
    def get_latest_figure(page_number):
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
    def get_most_wished():
        most_wished_figure_data = get_most_wished_figure()

        most_wished_figure_data_json = json.dumps(most_wished_figure_data, indent=4)

        return Response(most_wished_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_most_ordered():
        most_ordered_figure_data = get_most_ordered_figure()

        most_ordered_figure_data_json = json.dumps(most_ordered_figure_data, indent=4)

        return Response(most_ordered_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_most_owned():
        most_owned_figure_data = get_most_owned_figure()

        most_owned_figure_data_json = json.dumps(most_owned_figure_data, indent=4)

        return Response(most_owned_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_most_rated():
        most_rated_figure_data = get_most_rated_figure()

        most_rated_figure_data_json = json.dumps(most_rated_figure_data, indent=4)

        return Response(most_rated_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_most_viewed():
        most_viewed_figure_data = get_most_viewed_figure()

        most_viewed_figure_data_json = json.dumps(most_viewed_figure_data, indent=4)

        return Response(most_viewed_figure_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_releases(year, month, page_number):
        releases_data_data = get_releases_date_figure(year, month, page_number)
        max_page_number = get_releases_date_max_page_number(year, month, page_number)

        releases_data_data['max_page_number'] = max_page_number
        releases_data_data_json = json.dumps(releases_data_data, indent=4)

        return Response(releases_data_data_json, mimetype='application/json')
    
    @staticmethod
    @lru_cache(maxsize=128)
    def get_profile(username):
        profile_data = get_profile_data(username)

        profile_data_json = json.dumps(profile_data, indent=4)

        return Response(profile_data_json, mimetype='application/json')


# http://127.0.0.1:9192/v1/items/945912 {TEST ITEM}
# http://127.0.0.1:9192/v1/entry/7620/1 {TEST ENTRY}
# http://127.0.0.1:9192/v1/profile/LalaBunnyLand/collection/owned/1 {TEST OWNED}
# http://127.0.0.1:9192/v1/profile/LalaBunnyLand/collection/ordered/1 {TEST ORDERED}
# http://127.0.0.1:9192/v1/profile/bukanyayan/collection/wished/1 {TEST WISHED}
# http://127.0.0.1:9192/v1/items/latest/1 {TEST LATEST}
# http://127.0.0.1:9192/v1/items/onfire {TEST ONFIRE}
# http://127.0.0.1:9192/v1/items/most_wished {TEST MOST WISHED}
# http://127.0.0.1:9192/v1/items/most_ordered {TEST MOST ORDERED}
# http://127.0.0.1:9192/v1/items/most_owned {TEST MOST OWNED}
# http://127.0.0.1:9192/v1/items/most_rated {TEST MOST RATED}
# http://127.0.0.1:9192/v1/items/most_viewed {TEST MOST VIEWED}
# http://127.0.0.1:9192/v1/items/releases/2024/3/1 {TEST RELEASES}
# http://127.0.0.1:9192/v1/profile/LalaBunnyLand {TEST PROFILE}
