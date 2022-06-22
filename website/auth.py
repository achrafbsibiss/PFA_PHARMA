
from flask import Blueprint,render_template

auth = Blueprint('auth',__name__,template_folder='templates')

@auth.route('/inscreption')
def inscription():
    return render_template("insc_phar.html",
                        custom_css="insc_phar")



@auth.route('/pharmacie')
def pharmacie():
    return render_template("client.html",
                                custom_css="client")


@auth.route('/abouts_ass')
def sing_up():
    return render_template("aboutas.html",
                            custom_css="aboutas")




@auth.route('/info')
def info():
    return render_template("maps_click.html",
                            custom_css="maps_click")