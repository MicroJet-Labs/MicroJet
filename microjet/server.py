import traceback
import html as _html_escape
from http.server import BaseHTTPRequestHandler, HTTPServer


# ── Page shells ───────────────────────────────────────────────────────────────

_HTML_SHELL = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MicroJet App</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body {{ margin: 0; padding: 0; }}</style>
</head>
<body class="bg-slate-50 text-slate-900">
{content}
</body>
</html>"""


_ERROR_SHELL = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MicroJet — {kind}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-950 text-gray-100 min-h-screen font-mono">

  <div class="bg-red-600 px-6 py-4 flex items-center gap-3">
    <span class="text-2xl">💥</span>
    <div>
      <p class="text-xs text-red-200 uppercase tracking-widest">MicroJet · {status}</p>
      <h1 class="text-lg font-bold leading-tight">{kind}</h1>
    </div>
  </div>

  <div class="px-6 py-5 bg-red-950 border-b border-red-800">
    <p class="text-red-300 text-sm font-semibold mb-1">Error</p>
    <p class="text-white text-base">{message}</p>
  </div>

  <div class="px-6 py-5">
    <p class="text-gray-400 text-xs uppercase tracking-widest mb-3">Traceback</p>
    <pre class="bg-gray-900 rounded-xl p-5 text-sm text-green-300 overflow-x-auto
                leading-relaxed border border-gray-700">{traceback}</pre>
  </div>

  <div class="px-6 pb-8">
    <p class="text-gray-500 text-xs">
      Fix the error and save the file — MicroJet will reload automatically.
    </p>
  </div>

</body>
</html>"""


def _error_page(status: int, kind: str, exc: BaseException) -> str:
    tb_lines = traceback.format_exception(type(exc), exc, exc.__traceback__)
    tb_text  = _html_escape.escape("".join(tb_lines))
    message  = _html_escape.escape(str(exc))
    return _ERROR_SHELL.format(
        status    = status,
        kind      = _html_escape.escape(kind),
        message   = message,
        traceback = tb_text,
    )


# ── Request object ────────────────────────────────────────────────────────────

class _Request:
    def __init__(self, path: str, method: str, headers):
        self.path    = path
        self.method  = method
        self.headers = headers


# ── HTTP Handler ──────────────────────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):
    router = None

    def log_message(self, fmt, *args):
        print(f"  [{self.command}] {self.path}  →  {args[1]}")

    def do_GET(self):
        handler = self.router.get(self.path)

        if handler is None:
            self._send(404, _error_page(
                404, "404 — Page Not Found",
                FileNotFoundError(f"No route registered for '{self.path}'"),
            ))
            return

        try:
            content = self._resolve(handler)
            # Full HTML document — send as-is (template mode)
            if content.lstrip().startswith("<!"):
                self._send(200, content)
            else:
                self._send(200, _HTML_SHELL.format(content=content))

        except FileNotFoundError as exc:
            print(f"\n  ❌ Template not found: {exc}\n")
            self._send(404, _error_page(404, "Template Not Found", exc))

        except SyntaxError as exc:
            print(f"\n  ❌ Template syntax error: {exc}\n")
            self._send(500, _error_page(500, "Template Syntax Error", exc))

        except Exception as exc:
            traceback.print_exc()
            self._send(500, _error_page(500, "Internal Server Error", exc))

    def _resolve(self, handler) -> str:
        # Component — has .render()
        if hasattr(handler, 'render'):
            return handler.render()

        # View function — callable
        if callable(handler):
            req    = _Request(self.path, self.command, self.headers)
            result = handler(req)
            if hasattr(result, 'render'):
                return result.render()
            return str(result)

        return str(handler)

    def _send(self, status: int, body: str):
        encoded = body.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


# ── Server entry point ────────────────────────────────────────────────────────

def run_server(router, host: str = "127.0.0.1", port: int = 2011):
    Handler.router = router
    server = HTTPServer((host, port), Handler)
    print(f"  MicroJet running →  http://{host}:{port}")
    server.serve_forever()
