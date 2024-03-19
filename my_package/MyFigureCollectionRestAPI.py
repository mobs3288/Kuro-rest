from flask import Flask, Response
import json
from functools import lru_cache
from my_package.figure_data import get_fig_data
from my_package.entry_data import get_entry_data, get_entry_max_page_number
from my_package.owned_collection_data import get_owned_figure_by_uname, get_owned_collection_max_page
from my_package.ordered_collection_data import get_ordered_figure_by_uname, get_ordered_collection_max_page
from my_package.wished_collection_data import get_wished_figure_by_uname, get_wished_collection_max_page
from my_package.latest_figure_data import get_latest_figure, get_latest_max_page

class KuroRest:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/items/<item_id>', 'get_item_data', self.get_item_data)
        self.app.add_url_rule('/entry/<entry_id>/<page_number>', 'get_entry', self.get_entry)
        self.app.add_url_rule('/profile/<username>/collection/owned/<page_number>', 'get_owned_collection_by_uname', self.get_owned_collection_by_uname)
        self.app.add_url_rule('/profile/<username>/collection/ordered/<page_number>', 'get_ordered_collection_by_uname', self.get_ordered_collection_by_uname)
        self.app.add_url_rule('/profile/<username>/collection/wished/<page_number>', 'get_wished_collection_by_uname', self.get_wished_collection_by_uname)
        self.app.add_url_rule('/latest/<page_number>', 'latest_figure', self.latest_figure)
    
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


# http://127.0.0.1:9192/items/945912 {TES ITEM}
# http://127.0.0.1:9192/entry/7620/1 {TES ENTRY}
# http://127.0.0.1:9192/profile/LalaBunnyLand/collection/owned/1 {TES OWNED}
# http://127.0.0.1:9192/profile/LalaBunnyLand/collection/ordered/1 {TES ORDERED}
# http://127.0.0.1:9192/profile/bukanyayan/collection/wished/1 {TES WISHED}
# http://127.0.0.1:9192/latest/1 {TES LATEST}