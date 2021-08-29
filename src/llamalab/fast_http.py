def simple_server(host: str = "0.0.0.0", port: int = 9999, **kwargs):
    import flask

    s = flask.Flask(__name__)

    @s.route("/", methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
    def home( ):
        print(
            (r := {
                "method": flask.request.method,
                "server": flask.request.server,
                "path": flask.request.path,
                "host": flask.request.host,
                "host_url": flask.request.host_url,
                "url": flask.request.url,
                "headers": {x: y for x, y in flask.request.headers.items()},
                "args": {x: y for x, y in flask.request.args.items()},
                "form": {x: y for x, y in flask.request.form.items()},
                "files": {x: y for x, y in flask.request.files.items()},
                "cookies": {x: y for x, y in flask.request.cookies.items()},
                "endpoint": flask.request.endpoint
            })
        )

        return r

    s.run(host, port, **kwargs)
