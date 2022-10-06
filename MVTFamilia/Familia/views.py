# from logging.config import dictConfig
# from re import template
# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Familia.models import Familia

# Create your views here.


def crear_familiar(request) -> HttpResponse:
    template = loader.get_template("template1.html")
    lucas = Familia(
        nombre="Lucas",
        apellido="Gutierez",
        edad=45,
        rol="padre",
        profesion="herrero",
        fecha_de_nacimiento="1977-08-03",
    )
    miriam = Familia(
        nombre="Miriam",
        apellido="Vazquez",
        edad=47,
        rol="madre",
        profesion="docente en un secundario del Estado",
        fecha_de_nacimiento="1975-02-17",
    )
    milagros = Familia(
        nombre="Milagros",
        apellido="Gutierez",
        edad=15,
        rol="hija",
        profesion="estudiante",
        fecha_de_nacimiento="2007-11-8",
    )
    lucas.save()
    miriam.save()
    milagros.save()
    dict_de_contexto = {
        "lucas_nom": lucas.nombre,
        "lucas_ape": lucas.apellido,
        "lucas_edad": lucas.edad,
        "lucas_rol": lucas.rol,
        "lucas_prof": lucas.profesion,
        "lucas_naci": lucas.fecha_de_nacimiento,
        "miriam_nom": miriam.nombre,
        "miriam_ape": miriam.apellido,
        "miriam_edad": miriam.edad,
        "miriam_rol": miriam.rol,
        "miriam_prof": miriam.profesion,
        "miriam_naci": miriam.fecha_de_nacimiento,
        "milagros_nom": milagros.nombre,
        "milagros_ape": milagros.apellido,
        "milagros_edad": milagros.edad,
        "milagros_rol": milagros.rol,
        "milagros_prof": milagros.profesion,
        "milagros_naci": milagros.fecha_de_nacimiento,
    }
    res = template.render(dict_de_contexto)
    return HttpResponse(res)
