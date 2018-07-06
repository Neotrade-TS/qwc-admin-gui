from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional


class ResourceForm(FlaskForm):
    """Main form for Resource GUI"""
    type = SelectField('Type', choices=[
        ('map', "Map"),
        ('layer', "Layer"),
        ('attribute', "Attribute")
    ])
    name = StringField('Name', validators=[DataRequired()])
    parent_id = SelectField(
        'Parent resource', coerce=int, validators=[Optional()]
    )

    submit = SubmitField('Save')
