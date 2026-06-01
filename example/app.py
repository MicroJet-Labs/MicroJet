from atomy import App, Text

app = App()
app.route("/", Text("Welcome to Atomy.py"))
app.run()
