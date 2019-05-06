import os
import subprocess

import click
from flask import Flask, request, make_response
from werkzeug.routing import Rule
from pprint import pformat
import logging

logging.basicConfig(format="%(asctime)-15s | %(message)s", level='INFO')
app = Flask("dumbwebhook")


def all_methods_allowed_rule_wrapper(rule, **kwargs):
    kwargs['methods'] = None
    return Rule(rule, **kwargs)


app.url_rule_class = all_methods_allowed_rule_wrapper


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    request_data = request.data
    request_data_size = len(request_data)
    should_display_request_data = request_data_size <= app.config['max_len_to_display']

    if app.config['use_json']:
        try:
            request_json = request.json
        except ValueError:
            data_to_display = request_data
        else:
            data_to_display = request_json

    display_message = "Request data length: {}".format(request_data_size)
    if should_display_request_data:
        display_message += "\n{}".format(pformat(data_to_display))

    logging.info(display_message)

    return make_response("OK", 200)



@click.command()
@click.option('--max-len-to-display', default=5000)
@click.option('--use-json', type=bool, default=True)
@click.option('--port', type=int, default=6000)
def run(max_len_to_display, use_json, port):
    app.config['max_len_to_display'] = max_len_to_display
    app.config['use_json'] = use_json
    app.run(port=port)


if __name__ == '__main__':
    run()
