import sys
import os
import requests
import subprocess
import pyfiglet

# =========================
# GITHUB CDN BASE
# =========================
BASE_URL = "https://raw.githubusercontent.com/codegear-2011/MicroJet/main/microjet"


# =========================
# FETCH FILE FROM GITHUB
# =========================
def fetch_file(path):
    url = f"{BASE_URL}/{path}"

    try:
        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            return r.text

        print(f"  Not found: {path}")
        return None

    except Exception as e:
        print("  Network error:", e)
        return None


# =========================
# CREATE NEW PROJECT
# =========================
def create_project(name, mode="comp"):

    print(f" Creating project: {name}  (mode: -{mode})")

    os.makedirs(name, exist_ok=True)

    # ── Component Mode ────────────────────────────────────────────────────────
    if mode == "comp":
        core_files = ["app.py", "router.py", "server.py", "__init__.py"]

        default_app = """from microjet import *

app = App()

app.route("/", Text("Hello MicroJet"))

app.run()
"""

    # ── Template Mode (JetPage enabled) ───────────────────────────────────────
    elif mode == "temp":
        core_files = [
            "app.py",
            "router.py",
            "server.py",
            "template.py",
            "__init__.py",
        ]

        default_app = """from microjet import *

app = App(template_dir="templates")

app.route(
    "/",
    "index.html",
    title = "Welcome to MicroJet",
)

app.run()
"""

    else:
        print(f"  Unknown mode: -{mode}. Use -comp or -temp")
        return

    # ── Download core files into microjet/ ────────────────────────────────────
    for file in core_files:
        print(f"  Downloading: {file}")
        content = fetch_file(file)

        if content:
            path = os.path.join(name, "microjet", file)
            os.makedirs(os.path.dirname(path), exist_ok=True)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    # ── Write default app.py ──────────────────────────────────────────────────
    with open(os.path.join(name, "app.py"), "w", encoding="utf-8") as f:
        f.write(default_app)

    # ── Template mode: create templates/ with starters ────────────────────────
    if mode == "temp":
        templates_dir = os.path.join(name, "templates")
        os.makedirs(templates_dir, exist_ok=True)

        with open(os.path.join(templates_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write("""{# MicroJet starter template #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%jp title %></title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-900 flex items-center justify-center min-h-screen">
    <div class="text-center p-12">
        <h1 class="text-4xl font-bold mb-4"><%jp title %></h1>
        <p class="text-gray-400 mt-2">Edit templates/index.html to get started.</p>
    </div>
</body>
</html>
""")

        with open(os.path.join(templates_dir, "base.html"), "w", encoding="utf-8") as f:
            f.write("""{# Base layout — reuse across pages #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%jp title %></title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 text-slate-900">

    <nav class="bg-white shadow px-8 py-4">
        <span class="font-bold text-lg"><%jp site_name %></span>
    </nav>

    <main class="max-w-4xl mx-auto p-8">
        <%jp content %>
    </main>

    <footer class="text-center text-sm text-gray-400 py-6">
        Powered by MicroJet
    </footer>

</body>
</html>
""")

        print("  Created: templates/index.html")
        print("  Created: templates/base.html")

    # ── Done ──────────────────────────────────────────────────────────────────
    print(f"\n Project '{name}' created successfully!")
    _print_tree(name, mode)
    print(f"   cd {name}")
    print(f"   jet run\n")


def _print_tree(name, mode):
    if mode == "temp":
        print(f"""
  {name}/
  ├── app.py
  ├── templates/
  │   ├── index.html
  │   └── base.html
  └── microjet/
      ├── app.py
      ├── router.py
      ├── server.py
      ├── template.py
      └── __init__.py
""")
    else:
        print(f"""
  {name}/
  ├── app.py
  └── microjet/
      ├── app.py
      ├── router.py
      ├── server.py
      └── __init__.py
""")


# =========================
# ADD COMPONENT
# =========================
def add_component(name):
    print(f"Downloading component: {name}")

    root            = get_project_root()
    components_path = os.path.join(root, "components")
    os.makedirs(components_path, exist_ok=True)

    content = fetch_file(f"components/{name}.py")

    if not content:
        print("Component not found")
        return

    file_path = os.path.join(components_path, f"{name}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved: {file_path}")
    update_exports_safe(components_path)
    print("Project's Component Database Synced")


# =========================
# ADD TEMPLATE (JetPage)
# =========================
def add_template(name):
    print(f"Downloading template: {name}")

    root          = get_project_root()
    templates_dir = os.path.join(root, "templates")
    os.makedirs(templates_dir, exist_ok=True)

    content = fetch_file(f"templates/{name}.html")

    if not content:
        print("Template not found on Microjet server")
        return

    file_path = os.path.join(templates_dir, f"{name}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved: templates/{name}.html")


# =========================
# RUN APP  (hot reload)
# =========================

def _is_template_project() -> bool:
    return os.path.isdir(os.path.join(os.getcwd(), "templates"))


def _spawn() -> subprocess.Popen:
    return subprocess.Popen(
        [sys.executable, "app.py"],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def _run_with_hot_reload():
    try:
        from watchdog.observers import Observer
        from watchdog.events    import FileSystemEventHandler
        _run_watchdog(Observer, FileSystemEventHandler)
    except ImportError:
        print("  ⚠  watchdog not installed — using simple poll watcher")
        print("     pip install watchdog   for faster hot reload\n")
        _run_poll()


def _run_watchdog(Observer, FileSystemEventHandler):
    import time

    class _Handler(FileSystemEventHandler):
        _changed = False

        def on_modified(self, event):
            if event.is_directory:
                return
            if event.src_path.endswith((".py", ".html")):
                rel = os.path.relpath(event.src_path)
                print(f"\n    Changed: {rel} — restarting...\n")
                _Handler._changed = True

    handler  = _Handler()
    observer = Observer()
    observer.schedule(handler, path=".", recursive=True)
    observer.start()
    current = _spawn()

    try:
        while True:
            time.sleep(0.5)
            if _Handler._changed:
                _Handler._changed = False
                current.terminate()
                try:
                    current.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    current.kill()
                current = _spawn()
            elif current.poll() is not None:
                print("\n  ⚠  Server stopped. Fix the error and save to reload.\n")
                current = _spawn()
    except KeyboardInterrupt:
        print("\n  Shutting down...\n")
        observer.stop()
        current.terminate()

    observer.join()


def _run_poll():
    import time
    import glob

    def _mtimes():
        files = (glob.glob("**/*.py",   recursive=True) +
                 glob.glob("**/*.html", recursive=True))
        return {f: os.path.getmtime(f) for f in files}

    current  = _spawn()
    snapshot = _mtimes()

    try:
        while True:
            time.sleep(1)
            now     = _mtimes()
            changed = [f for f, t in now.items() if snapshot.get(f) != t]

            if changed:
                print(f"\n    Changed: {changed[0]} — restarting...\n")
                current.terminate()
                try:
                    current.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    current.kill()
                current  = _spawn()
                snapshot = _mtimes()
            elif current.poll() is not None:
                print("\n  ⚠  Server stopped. Fix the error and save to reload.\n")
                current  = _spawn()
                snapshot = _mtimes()
    except KeyboardInterrupt:
        print("\n  Shutting down...\n")
        current.terminate()


def run_app():
    result = pyfiglet.figlet_format("MICROJET", font="sub-zero")
    print(result)

    mode_label = "MicroJet's JetPage" if _is_template_project() else "MicroJet Classic"

    print(f"""
------------------------------------------------
Microjet Development Server
Version: 1.0
Mode   : {mode_label}

Starting server...

Server running at http://127.0.0.1:2011/
Hot reload active — save any .py or .html file to restart
Press CTRL+C to stop
------------------------------------------------
""")

    if not os.path.exists("app.py"):
        print("  app.py not found")
        return

    _run_with_hot_reload()


# =========================
# HELP MENU
# =========================
def help_menu():
    result = pyfiglet.figlet_format("MicroJet", font="sub-zero")
    print(result)
    print("""
 MicroJet CLI Commands:

  Project Creation:
    jet new <project> -comp     → Component-based project
    jet new <project> -temp     → Template-based project (JetPage enabled)

  Components:
    jet add <component>         → Download & add a UI component

  Templates (JetPage):
    jet template add <name>     → Download a pre-built HTML template
    jet template list           → List available templates

  General:
    jet run                     → Run your app (hot reload included)
    jet help                    → Show this menu

  JetPage Template Syntax (.html files):
    <%jp variable %>            → Print a variable
    <%jp expression %>          → Any Python expression
    <%jp: for x in items %>     → For loop
    <%jp: if condition %>       → If block
    <%jp: elif condition %>     → Elif branch
    <%jp: else %>               → Else branch
    <%jp: end %>                → Close any block
    {# comment #}               → Template comment (not rendered)

  Usage in app.py:
    app.route("/", "index.html", title="Home")     → Template route
    app.route("/", Text("Hello"))                  → Component route
""")


# =========================
# TEMPLATE SUBCOMMANDS
# =========================
def template_commands(args):
    if len(args) < 3:
        print("  Usage: jet template <add|list> [name]")
        return

    sub = args[2]

    if sub == "add":
        if len(args) < 4:
            print("  Template name missing.  jet template add <name>")
            return
        add_template(args[3])

    elif sub == "list":
        print("""
 Available templates (jet template add <name>):

    index       → Simple landing page
    dashboard   → Admin dashboard layout
    blog        → Blog post list page
    detail      → Single item detail page
    form        → Contact / login form page
""")
    else:
        print(f"  Unknown template command: {sub}")


# =========================
# UTILS
# =========================
def update_exports_safe(components_path):
    init_file = os.path.join(components_path, "__init__.py")
    os.makedirs(components_path, exist_ok=True)
    exports   = []

    for file in os.listdir(components_path):
        file_path = os.path.join(components_path, file)
        if file.endswith(".py") and file != "__init__.py" and os.path.isfile(file_path):
            module_name = file[:-3]
            class_name  = module_name.capitalize()
            exports.append(f"from .{module_name} import {class_name}")

    with open(init_file, "w", encoding="utf-8") as f:
        if exports:
            f.write("\n".join(sorted(exports)) + "\n")
        else:
            f.write("# auto generated exports\n")

    print("Project's Component Database Synced")


def get_project_root():
    current = os.getcwd()
    if os.path.exists(os.path.join(current, "app.py")):
        return current
    return current


# =========================
# MAIN CLI
# =========================
def main():
    args = sys.argv

    if len(args) < 2:
        help_menu()
        return

    cmd = args[1]

    if cmd == "new":
        if len(args) < 3:
            print("  Project name missing")
            return

        project_name = args[2]
        mode         = "comp"

        if len(args) >= 4:
            flag = args[3].lstrip("-")
            if flag in ("comp", "temp"):
                mode = flag
            else:
                print(f"  Unknown flag: {args[3]}. Use -comp or -temp")
                return

        create_project(project_name, mode)

    elif cmd == "add":
        if len(args) < 3:
            print("  Component name missing")
            return
        add_component(args[2])

    elif cmd == "template":
        template_commands(args)

    elif cmd == "run":
        run_app()

    elif cmd == "help":
        help_menu()

    else:
        print("  Unknown command")
        help_menu()


if __name__ == "__main__":
    main()
