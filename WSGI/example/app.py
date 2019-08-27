# coding:utf-8


def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content_type', 'text-plain')]
    start_response(status, response_headers)
    return ['Hello world! -by lmz \n']
