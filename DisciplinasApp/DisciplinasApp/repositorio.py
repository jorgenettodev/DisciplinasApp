class DisciplinasRepo:
    def __init__(self):
        # é basicamente uma lista baseada em dicionário
        # python que contém 3 temas, cada um com 3 módulos.

        self.repo = {
            "Webservices":
                ["Conceitos de Web services",
                 "Utilizando SOAP em Java",
                 "Utilizando REST em Java"],
            "Programação Servidor com Java":
            ["Webserver Tomcat",
             "App Server GlassFish",
             "Servlet e JSP"],
            "JPA e JEE":
            ["Tecnologia JPA",
             "Enterprise Java Beans",
             "Arquitetura MVC"]
        }

    # Retorna os temas
    def getTemas(self):
        return self.repo.keys()

    # Retorna os módulos de um tema
    def getModulosTema(self, tema):
        return self.repo[tema]