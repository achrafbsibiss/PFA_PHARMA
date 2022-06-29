
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__,template_folder='templates')

@auth.route('/inscreption', methods=['GET','POST'] )
def inscription():
    if request.method == 'POST':
        Name = request.form.get('Name')
        email = request.form.get('email')
        Number = request.form.get('Number')
        position = request.form.get('linke')

        if len(email) < 4:
            flash('Email must be great than 4 charachter',category='error')
        elif len(Name) < 5:
            flash('Name must be great than 5 charachter',category='error')
        elif len(Number) == 10 or len(Number) == 11 :
            flash('Number must be great than 9 charachter',category='error')
        else: 
            flash ('your pharmacie i se created!', category='succes')

    
    return render_template("insc_phar.html",
                        custom_css="insc_phar")


 
@auth.route('/pharmacie', methods=['GET','POST'])
def pharmacie():
    return render_template("client.html",
                                custom_css="client")


@auth.route('/abouts_ass')
def sing_up():
    return render_template("aboutas.html",
                            custom_css="aboutas")



@auth.route('/contact')
def cont():
    return render_template("contact.html",
                            custom_css="contact")


@auth.route('/info')
def info():
    return render_template("maps_click.html",
                            custom_css="maps_click")