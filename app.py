from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from forms import RegistrationForm, LoginForm, KDPForm, CSVFILE
from werkzeug import generate_password_hash, check_password_hash
import  cv2, time,os
import urllib.request
import requests
from bs4 import  BeautifulSoup
#from flask.ext.images import resized_img_src
#import  Flask-Images
##from selenium import webdriver
##from selenium.webdriver.common.by import By
##from selenium.webdriver.common.keys import Keys
##from selenium.webdriver.support.ui import Select
##from selenium.common.exceptions import NoSuchElementException
##from selenium.common.exceptions import NoAlertPresentException
##import unittest, time, re







#Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/jannat/Desktop/WEBAPPDESCRIPTION/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#images = Images(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', {self.password})"

class KDP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    BookTitle = db.Column(db.String(20), unique=True, nullable=False)
    Subtitle  = db.Column(db.String(20), unique=True, nullable=False)
    Series_Information  = db.Column(db.String(20), unique=True, nullable=False)
    Edition_number  = db.Column(db.String(20), unique=True, nullable=False)
    AuthorFirstName = db.Column(db.String(20), unique=True, nullable=False)
    AuthorLastName = db.Column(db.String(20), unique=True, nullable=False)
    ContributorFirstName = db.Column(db.String(20), unique=True, nullable=False)
    ContributorLastName = db.Column(db.String(20), unique=True, nullable=False)
    Description  = db.Column(db.String(20), unique=True, nullable=False)
    Keywords1  = db.Column(db.String(20), unique=True, nullable=False)
    Keywords2  = db.Column(db.String(20), unique=True, nullable=False)
    Keywords3  = db.Column(db.String(20), unique=True, nullable=False)
    Keywords4  = db.Column(db.String(20), unique=True, nullable=False)
    Keywords5   = db.Column(db.String(20), unique=True, nullable=False)
    Keywords6   = db.Column(db.String(20), unique=True, nullable=False)
    Keywords7   = db.Column(db.String(20), unique=True, nullable=False)


    def __repr__(self):
        return f"KDP('{self.BookTitle}','{self.Subtitle}','{self. Series_Information}','{self.Edition_number }','{self.AuthorFirstName}','{self.AuthorLastName}','{self.ContributorFirstName}','{self.ContributorLastName}','{self.Description}','{self.Keywords1}','{self.Keywords2}','{self.Keywords3}','{self.Keywords4}','{self.Keywords5}','{self.Keywords6}','{self.Keywords7}')"
    
class CSVFILE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    therange = db.Column(db.String(200),unique=True, nullable=False)
    
    def __repr__(self):
        return f"CSVFILE('{self.title}', '{self.therange}')"
    


   


@app.route("/kdp", methods=['GET', 'POST'])
def kdp():
    form = KDPForm()
    if form.validate_on_submit():
        kdpinformations = KDP(BookTitle=form.BookTitle.data,Subtitle =form.Subtitle.data,Series_Information=form.Series_Information.data,Edition_number=form.Edition_number.data,AuthorFirstName=form.AuthorFirstName.data,AuthorLastName =form.AuthorLastName.data,ContributorFirstName =form.ContributorFirstName.data,ContributorLastName =form.ContributorLastName.data,Description =form.Description.data,Keywords1 =form.Keywords1.data,Keywords2 =form.Keywords2.data,Keywords3 =form.Keywords3.data,Keywords4 =form.Keywords4.data,Keywords5 =form.Keywords5.data,Keywords6 =form.Keywords6.data,Keywords7 =form.Keywords7.data)
        db.session.add(kdpinformations)
        db.session.commit()
        return redirect(url_for('kdp2'))
    return render_template('kdp.html', title='kdp', form=form )

@app.route("/kdp2")
def kdp2():
    form = KDPForm()
    page = request.args.get('page', 1, type=int)
    kdpinformationst = KDP.query.paginate(page=page, per_page=5)
    #kdpinformationst = KDPP.query.all()
    return render_template('kdp2.html', title='kdp2', form=form, kdpinformationst=kdpinformationst )





@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/csvfile", methods=['GET', 'POST'])
def csvfile():
    form = CSVFILE()
    if form.validate_on_submit():
        stockfile = CSVFILE(title=form.title.data, therange=form.therange.data)
        db.session.add(stockfile)
        db.session.commit()
    return redirect(url_for('csvfile'))
    return render_template('csvfile.html', form=form, stockfile=stockfile)


listsource = []
@app.route("/extern")
def extern():
    url = "https://codeforces.com/"
    #url = "https://www.amazon.com/"
    response = urllib.request.urlopen(url)
    html_data = response.read()
    soup = BeautifulSoup(html_data, 'html.parser')
    #text1 = soup.find('a').get('href')
    text1 = soup.findAll('img')
    for img in text1 :
        source = img.get('src')
        listsource.append(source)
    #text = text1.prettify()
    return render_template('extern.html', text=text1, soup=soup, listsource=listsource )

@app.route("/nativehtml")
def nativehtml():
    url = "https://codeforces.com/"
    #url = "https://www.amazon.com/"
    #url = "https://www.amazon.com/gift-cards/b/?ie=UTF8&node=2238192011&ref_=nav_cs_gc"
    response = urllib.request.urlopen(url)
    html_data = response.read()
    soup = BeautifulSoup(html_data, 'html.parser')
    #text1 = soup.find('a').get('href')
    text1 = soup.findAll('img')
    for img in text1 :
        source = img.get('src')
        listsource.append(source)
    return render_template('nativehtml.html', listsource=listsource )



@app.route("/about")
def about():
    form = RegistrationForm()
    page = request.args.get('page', 1, type=int)
    allusers = User.query.paginate(page=page, per_page=5)
    #allusers = User.query.all()
    return render_template('about.html', title='About', form=form, allusers=allusers )
    



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        my_user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(my_user)
        db.session.commit()
        
        return redirect(url_for('about'))
    return render_template('register.html', title='Register', form=form )
        

    


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        somevisitor = User.query.filter_by(email=form.email.data).first()
        if somevisitor:
            if  check_password_hash(somevisitor.password, form.password.data):
                return redirect(url_for('about'))
        return '<h1> invalid username or password </h1>'
       
    return render_template('login.html', title='Login', form=form)



##@app.route("/webengine")
##def webengine():
##    driver = webdriver.Chrome("chromewebdriver\chromedriver.exe")
##    #driver = webdriver.Chrome("C:\Users\jannat\Desktop\WEBAPPDESCRIPTION\chromewebdriver\chromedriver.exe")
##    #driver = webdriver.firefox()
##    return driver.get("https://www.amazon.com/s?k=journal+woodworker&i=stripbooks-intl-ship&ref=nb_sb_noss")
##    #driver.maximize_window()
##    #time.sleep(5)
    


if __name__ == '__main__':
    app.run(debug=True)
































##
##class KDP(db.Model):
##    id = db.Column(db.Integer, primary_key=True)
##    BookTitle = db.Column(db.String(20), unique=True, nullable=False)
##    Subtitle  = db.Column(db.String(20), unique=True, nullable=False)
##    Series_Information  = db.Column(db.String(20), unique=True, nullable=False)
##    Edition_number  = db.Column(db.String(20), unique=True, nullable=False)
##    AuthorFirstName = db.Column(db.String(20), unique=True, nullable=False)
##    AuthorLastName = db.Column(db.String(20), unique=True, nullable=False)
##    ContributorFirstName = db.Column(db.String(20), unique=True, nullable=False)
##    ContributorLastName = db.Column(db.String(20), unique=True, nullable=False)
##    Description  = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords1  = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords2  = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords3  = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords4  = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords5   = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords6   = db.Column(db.String(20), unique=True, nullable=False)
##    Keywords7   = db.Column(db.String(20), unique=True, nullable=False)
##
##
##    def __repr__(self):
##        return f"KDP('{self.BookTitle}','{self.Subtitle}','{self. Series_Information}','{self.Edition_number }','{self.AuthorFirstName}','{self.AuthorLastName}','{self.ContributorFirstName}','{self.ContributorLastName}','{self.Description}','{self.Keywords1}','{self.Keywords2}','{self.Keywords3}','{self.Keywords4}','{self.Keywords5}','{self.Keywords6}','{self.Keywords7}')"
##    
    


    

##class mylistimage(db.Model):
##    id = db.Column(db.Integer, primary_key=True)
##    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
##
##    def __repr__(self):
##        return f"mylistimage('{self. image_file}')"

    



     #page = request.args.get('page', 1, type=int)
     #titleimage = User.query.paginate(page=page, per_page= 6)
     #titleimage = User.query.all()
    
##    my_dir = "C:/Users/jannat/Desktop/WEBAPPDESCRIPTION/static/images"
##    listimage = []
##    for files in os.walk(my_dir):
##        listimage.append(files)
##        for myimage in listimage :
##            themylistimage=myimage[2]
##            for image_file in themylistimage :
##                titleimage = mylistimage(image_file=image_file)
##                db.session.add(titleimage)
##                db.session.commit()
##                titleimage = User.query.all()
##            return redirect(url_for('home'))
##    return render_template('home.html', titleimage = titleimage)
    
            
                
            
            
##            for titleimage in mylistimage :
##                db.session.add(User.titleimage)
##                db.session.commit()
##                return redirect(url_for('home'))
    



##    video = cv2.VideoCapture(0)
##    check, frame = video.read()
##    key = cv2.waitKey(1)
##    cv2.imshow("Capturing", frame)
##    #image = cv2.imwrite('vvg.png', video)
##    video.release()
##    cv2.destroyAllWindows()

##@app.route("/kdp2")
##def kdp2():
##    form = KDPForm()
##    #page = request.args.get('page', 1, type=int)
##    #allusers = User.query.paginate(page=page, per_page=5)
##    kdpinformationst = KDP.query.all()
##    return render_template('kdp2.html', title='kdp2', form=form, kdpinformationst=kdpinformationst )
##    
##
##
##@app.route("/kdp", methods=['GET', 'POST'])
##def kdp():
##    #global  kdpinformations
##    form = KDPForm()
##    if form.validate_on_submit():
##        kdpinformations = KPD(BookTitle=form.BookTitle.data,Subtitle =form.Subtitle.data,Series_Information=form.Series_Information.data,Edition_number=form.Edition_number.data,AuthorFirstName=form.AuthorFirstName.data,AuthorLastName =form.AuthorLastName.data,ContributorFirstName =form.ContributorFirstName.data,ContributorLastName =form.ContributorLastName.data,Description =form.Description.data,Keywords1 =form.Keywords1.data,Keywords2 =form.Keywords2.data,Keywords3 =form.Keywords3.data,Keywords4 =form.Keywords4.data,Keywords5 =form.Keywords5.data,Keywords6 =form.Keywords6.data,Keywords7 =form.Keywords7.data)
##        #kdpinformations = KDP.query.all()
##        db.session.add(kdpinformations)
##        db.session.commit()
##        return redirect(url_for('kdp2'))
##    return render_template('kdp.html', title='kdp', form=form )
##
## 


 #def __repr__(self):
       # return f"KDPP({self.BookTitle})"

#db.session.rollback()
#flash('Error generating contact ', 'danger')

    #-------------------------------------------------------------
    #sss = INSERT INTO user (username, email, password) VALUES('{form.username.data}', '{form.email.data}', '{form.password.data}')
    #us = User(username='{form.username}',email='{form.email.data}',password='{form.password.data}')
    #db.session.add(sss)
    #db.session.commit()
    #----------------------------------------------------------------
     #description = request.form.get('username')
     #test_name = request.form.get('password')
    #----------------------------------------------------------------
     #conn = sqlite3.connect(DATABASE)
    #cur = conn.cursor()
    #cur.execute(sql, (description, test_name))
    #-------------------------------------------------------------------------------
##    # return  '<h1>' + form.username.data + '' + form.email.data + ' ' + form.password.data + '</h1>'
##    #-------------------------------------------------------------------------------------------
##     if form.email.data == 'yes@gmail.com' and form.password.data == 'notyet':
##            flash('You have been logged in!', 'success')
##            return redirect(url_for('home'))
##        else:
##            flash('Login Unsuccessful. Please check username and password', 'danger')
##    
##    
##
