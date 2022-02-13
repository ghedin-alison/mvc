from tornado import ioloop, httpserver
from tornado.web import Application

from controlers.produto_controller import Index, Novo, Atualiza, Deleta


class RunApp(Application):

    def __init__(self):
        handlers = [
            ('/', Index),
            ('/produto/novo', Novo),
            (r'/produto/update/(\d+)/status/(\d+)', Atualiza),  # utilizando regex
            (r'/produto/delete/(\d+)', Deleta)  # utilizando regex
        ]

        settings = dict(
            debug=True,
            template_path='views',
            static_path='static',
        )

        Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    httpserver = httpserver.HTTPServer(RunApp())
    httpserver.listen(5000)  # porta
    ioloop.IOLoop.instance().start()
