# -*- coding: utf-8 -*-
from spyne import Application, rpc, ServiceBase, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt

from DisciplinasApp.repositorio import DisciplinasRepo

disciplinas = DisciplinasRepo

class DisciplinasService(ServiceBase):
    # decorador rpc transforma a função em um soap web service.
    @rpc(_returns=Iterable(Unicode)) # retorna uma iterable (lista) em unidcode (texto)
    def getTemas(ctx):
        for i in disciplinas.getTemas():
            yield i

    @rpc(Unicode, _returns=Iterable(Unicode))
    def getModulosTema(ctx, tema):
        for i in disciplinas.getModulosTema(tema):
            yield i

application = Application([DisciplinasService],
                          tns='disciplinas.app.ws',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
)

disciplinas_ws = csrf_exempt(DjangoApplication(application))