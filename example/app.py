from microjet import *

app = App()

page = Container(

    Navbar(

        NavbarBrand("MicroJet"),

        NavbarMenu(
            NavbarItem("Docs", href="/docs"),
            NavbarItem("Components", href="/components"),
            NavbarItem("GitHub", href="https://github.com/codegear&l&2011/MicroJet"),
        )

    ),
Toast(
    "The App Is Working!!",
    variant="success",
    
),
    Card(

        

    #Image(
#        #src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0eLXMZJpj7CuIUoSfKGTHJn3hMFWaPIksjvSQ-27RT9T4wKuBshaJJeY&s=10",

#        height="280px",
#        width="100%",

#        rounded="xl",

#        fit="cover",

#        shadow=True
#    ),
    Logo(150),

    Text(
        "The Install Worked Sucessfully,Congrats!!",
        variant="large",font_size=35
    ),
    Text("What will you do next?", variant="lead"),
    Text(
    "1. Get started by editing app.py",
    variant="default"
    ),
    Text(
    "2. Read our DocsJet for learning MicroJet",
    variant="default"
    ),
Button("Get Started",align="center"),
Button("Documentation", variant="outline",align="center"),
    ),
    Text(""),
    Text(
        "© 2026 MicroJet • Developed for developers by Code Gear Pvt Ltd "
    )

)

app.route("/", page)

app.run()