from .router import Router
from .server import run_server
from .template import TemplateEngine


class App:
    def __init__(self, template_dir: str = "templates"):
        self.router          = Router()
        self.template_engine = TemplateEngine(template_dir)

    def route(self, path, component_or_template=None, **context):
        """
        Universal route method — three usage styles:

        # 1. Component
        app.route("/", Text("Hello"))

        # 2. Template with context
        app.route("/about", "about.html", title="About", team=[...])

        # 3. Template, no context
        app.route("/contact", "contact.html")
        """
        # Template string — "index.html"
        if isinstance(component_or_template, str):
            template_name = component_or_template
            engine        = self.template_engine

            def _view(request):
                return engine.render(template_name, **context)

            self.router.add_route(path, _view)

        # Component — Text(), Card() etc.
        else:
            self.router.add_route(path, component_or_template)

    def run(self, host: str = "127.0.0.1", port: int = 2011):
        run_server(self.router, host, port)
