import uuid

from allauth.account import views as allauth_views
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import (
    get_user_model, logout)
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from . import forms2


class MemberLoginView(allauth_views.LoginView):
    template_name = 'member/account/login.html'
    form_class = forms2.MemberLoginForm

    def get_context_data(self, **kwargs):
        context = super(MemberLoginView, self).get_context_data(**kwargs)
        context['page_title'] = _('Login')
        return context


class MemberLogoutView(allauth_views.LogoutView):
    template_name = 'member/account/logout.html'

    def get_context_data(self, **kwargs):
        context = super(MemberLogoutView, self).get_context_data(**kwargs)
        context['page_title'] = _('Logout')
        return context


class MemberAccountInactiveView(allauth_views.AccountInactiveView):
    template_name = 'member/account/account_inactive.html'

    def get_context_data(self, **kwargs):
        context = super(MemberAccountInactiveView, self).get_context_data(**kwargs)
        context['page_title'] = _('Account Inactive')
        return context


class MemberUnregisterView(auth_mixins.AccessMixin, FormView):
    template_name = 'member/account/unregister.html'
    form_class = forms2.MemberUnregisterForm

    def dispatch(self, request, *args, **kwargs):
        # LoginRequiredMixin is not used because of inheritance order
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        self.member = get_user_model().objects.get(pk=self.request.user.id)

        return super(MemberUnregisterView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MemberUnregisterView, self).get_context_data(**kwargs)
        context['page_title'] = _('Unregister')
        context['member'] = self.member
        return context

    def form_valid(self, form):
        response = super(MemberUnregisterView, self).form_valid(form)

        self.member.email = self.member.email + '_' + str(uuid.uuid4())
        self.member.username = self.member.username + '_' + str(uuid.uuid4())
        self.member.password = ''
        self.member.is_active = False
        self.member.is_staff = False
        self.member.is_superuser = False
        self.member.save()

        EmailAddress.objects.filter(user__id=self.member.id).delete()
        SocialAccount.objects.filter(user__id=self.member.id).delete()

        logout(self.request)

        return response

    def get_success_url(self):
        return reverse('home')


class MemberPasswordChangeView(auth_mixins.LoginRequiredMixin, allauth_views.PasswordChangeView):
    template_name = 'member/account/password_change.html'
    form_class = forms2.MemberChangePasswordForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordChangeView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Change')
        return context


class MemberPasswordSetView(auth_mixins.LoginRequiredMixin, allauth_views.PasswordSetView):
    template_name = 'member/account/password_set.html'
    form_class = forms2.MemberSetPasswordForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordSetView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Set')
        return context


class MemberPasswordReset(allauth_views.PasswordResetView):
    template_name = 'member/account/password_reset.html'
    form_class = forms2.MemberResetPasswordForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordReset, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset')
        return context


class MemberPasswordResetDoneView(allauth_views.PasswordResetDoneView):
    template_name = 'member/account/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordResetDoneView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset Done')
        return context


class MemberPasswordResetFromKeyView(allauth_views.PasswordResetFromKeyView):
    template_name = 'member/account/password_reset_from_key.html'
    form_class = forms2.MemberResetPasswordKeyForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordResetFromKeyView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset')
        return context


class MemberPasswordResetFromKeyDoneView(allauth_views.PasswordResetFromKeyDoneView):
    template_name = 'member/account/password_reset_from_key_done.html'

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordResetFromKeyDoneView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset Done')
        return context
