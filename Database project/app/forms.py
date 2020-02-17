from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FormField, TextAreaField, FileField
from wtforms.fields.html5 import DateField



class LoginForm(FlaskForm):
    username = StringField('Username', render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', render_kw={'placeholder': 'Password'})
    remember_me = BooleanField('Remember me') # TODO: ar fi frumos sa nu uit sa implementez asta, momentan folosirea la "cookies" e cam vaga
    submit = SubmitField('Sign In')
    secret_question=PasswordField('Secret Question', render_kw={'placeholder': 'Type here the name of your favorite animal in cause of forgetting your pass'})

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', render_kw={'placeholder': 'First Name'})
    last_name = StringField('Last Name', render_kw={'placeholder': 'Last Name'})
    username = StringField('Username', render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', render_kw={'placeholder': 'Password'})
    confirm_password = PasswordField('Confirm Password', render_kw={'placeholder': 'Confirm Password'})
    secret_question= StringField("Secret question", render_kw={'placeholder': 'The name of your favorite animal'})
    submit = SubmitField('Sign Up')

class ChangePass(FlaskForm):
    username = StringField('Username', render_kw={'placeholder': 'Username'})
    password = PasswordField('New Password', render_kw={'placeholder': 'New Password'})
    confirm_password = PasswordField('Confirm New Password', render_kw={'placeholder': 'Confirm New Password'})
    secret_question= StringField("Secret question", render_kw={'placeholder': 'The name of your favorite animal'})
    submit = SubmitField('Change Password')
    
class IndexForm(FlaskForm):
    login = FormField(LoginForm)
    register = FormField(RegisterForm)
    change_pass=FormField(ChangePass)
class PostForm(FlaskForm):
    content = TextAreaField('New Post', render_kw={'placeholder': 'What are you thinking about?'})
    image = FileField('Image')
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('New Comment', render_kw={'placeholder': 'What do you have to say?'})
    submit = SubmitField('Comment')

class FriendsForm(FlaskForm):
    username = StringField('Friend\'s username', render_kw={'placeholder': 'Username'})
    submit = SubmitField('Add Friend')

class ProfileForm(FlaskForm):
    education = StringField('Education', render_kw={'placeholder': 'Highest education'})
    employment = StringField('Employment', render_kw={'placeholder': 'Current employment'})
    music = StringField('Favorite song', render_kw={'placeholder': 'Favorite song'})
    movie = StringField('Favorite movie', render_kw={'placeholder': 'Favorite movie'})
    nationality = StringField('Nationality', render_kw={'placeholder': 'Your nationality'})
    birthday = DateField('Birthday')
    submit = SubmitField('Update Profile')
