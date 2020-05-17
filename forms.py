from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo






class CSVFILE(FlaskForm):
    title = StringField('title',
                           validators=[DataRequired(), Length(min=2, max=20)])
    therange = StringField('therange', validators=[DataRequired(),Length(min=2, max=200)])
    #therange = DecimalField('therange', validators=[NumberRange(min=0, max=100, message='bla')])
    
    submit = SubmitField('Send')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class KDPForm(FlaskForm):
    BookTitle = StringField('BookTitle',
                           validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Sign Up')
    Subtitle   = StringField('Subtitle ',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Series_Information = StringField('Series_Information',
                           validators=[DataRequired(), Length(min=2, max=50)])
    
    Edition_number = StringField('Edition_number',
                           validators=[DataRequired(), Length(min=2, max=50)])

    
    AuthorFirstName = StringField('AuthorFirstName',
                           validators=[DataRequired(), Length(min=2, max=50)])

    AuthorLastName = StringField('AuthorLastName',
                           validators=[DataRequired(), Length(min=2, max=50)])

    ContributorFirstName = StringField('ContributorFirstName ',
                           validators=[DataRequired(), Length(min=2, max=50)])
  
    ContributorLastName = StringField('ContributorLastName',
                           validators=[DataRequired(), Length(min=2, max=50)])

    Description = TextAreaField('Description',
                           validators=[DataRequired(), Length(min=2, max=200)])
    #Publishing Rights
             #* I own the copyright and I hold necessary publishing rights. What are publishing rights?
             #* This is a public domain work What is a public domain work?

    Keywords1 = StringField('Keywords1',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Keywords2 = StringField('Keywords2',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Keywords3 = StringField('Keywords3',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Keywords4 = StringField('Keywords4',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Keywords5 = StringField('Keywords5',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Keywords6 = StringField('Keywords6',
                           validators=[DataRequired(), Length(min=2, max=50)])
    Keywords7 = StringField('Keywords7',
                           validators=[DataRequired(), Length(min=2, max=50)])
    #Categories     2CHOICES
    #Adult Content
    #No
    #Yes
    
    
  
    
  
    submit = SubmitField('Sign Up')
