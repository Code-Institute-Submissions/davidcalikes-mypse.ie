from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    """
    Overrides DefaultAccountAdapter save_user method to include extra fields
    code used is from:
    https://stackoverflow.com/questions/66735981/django-allauth-custom-signup-form-doesnt-save-all-of-the-fields
    """
    def save_user(self, request, user, form, commit=True):

        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        role = data.get("role")
        username = data.get("username")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if role:
            user_field(user, "role", role)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
