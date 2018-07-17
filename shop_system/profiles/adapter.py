from allauth.account.adapter import DefaultAccountAdapter


class UserAccountAdapter(DefaultAccountAdapter):

	def save_user(self, request, user, form, commit=True):
		user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)
		user.role = 'user'	
		user.save()
		return user