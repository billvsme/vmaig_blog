#coding:utf-8
from django import forms
from vmaig_auth.models import VmaigUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
import base64
import logging

logger = logging.getLogger(__name__)



#参考自django.contrib.auth.forms.UserCreationForm

class VmaigUserCreationForm(forms.ModelForm):

    #错误信息
    error_messages = {
        'duplicate_username': u"此用户已存在.",
        'password_mismatch': u"两次密码不相等.",
        'duplicate_email':u'此email已经存在.'
    }

    username = forms.RegexField(max_length=30,regex=r'^[\w.@+-]+$',
        #错误信息 invalid 表示username不合法的错误信息, required 表示没填的错误信息
        error_messages={
            'invalid':  u"该值只能包含字母、数字和字符@/./+/-/_",
            'required': u"用户名未填"})
    email = forms.EmailField(error_messages={
        'invalid':  u"email格式错误",
        'required': u'email未填'})
    password1 = forms.CharField(widget=forms.PasswordInput,
        error_messages={
            'required': u"密码未填"
            })
    password2 = forms.CharField(widget=forms.PasswordInput,
        error_messages={
            'required': u"确认密码未填"
            })

    class Meta:
        model = VmaigUser
        fields = ("username","email")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            VmaigUser._default_manager.get(username=username)
        except VmaigUser.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages["duplicate_username"]
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                    self.error_messages["password_mismatch"]
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data["email"]

        #判断是这个email 用户是否存在
        try:
            VmaigUser._default_manager.get(email=email)
        except VmaigUser.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages["duplicate_email"]
        )
       
        

    def save(self, commit=True):
        user = super(VmaigUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class  VmaigPasswordRestForm(forms.Form):

    #错误信息
    error_messages = {
        'email_error': u"此用户不存在或者用户名与email不对应.",
    }


    username = forms.RegexField(max_length=30,regex=r'^[\w.@+-]+$',
        #错误信息 invalid 表示username不合法的错误信息, required 表示没填的错误信息
        error_messages={
            'invalid':  u"该值只能包含字母、数字和字符@/./+/-/_",
            'required': u"用户名未填"})
    email = forms.EmailField(
        error_messages={
        'invalid':  u"email格式错误",
        'required': u'email未填'})

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if username and email:
            try:
                self.user = VmaigUser.objects.get(username=username,email=email,is_active=True)
            except VmaigUser.DoesNotExist:
                raise forms.ValidationError(
                    self.error_messages["email_error"]
                )

        return self.cleaned_data

    def save(self,from_email=None,request=None,token_generator=default_token_generator):
        email = self.cleaned_data['email']
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain
        uid = base64.urlsafe_b64encode(force_bytes(self.user.pk)).rstrip(b'\n=')
        token = token_generator.make_token(self.user)
        protocol = 'http'

        title = u"重置 %s 的密码" % site_name
        message = u"你收到这封信是因为你请求重置你在 网站 %s 上的账户密码\n\n" % site_name  + \
                  u"请访问该页面并输入新密码:\n\n" + \
                  protocol+'://'+domain+'/'+'resetpassword'+'/'+uid+'/'+token+'/'+'  \n\n' + \
                  u"你的用户名，如果已经忘记的话:  %s\n\n" % self.user.username + \
                  u"感谢使用我们的站点!\n\n" + \
                  u"%s 团队\n\n\n" % site_name

        try:
            send_mail(title, message, from_email, [self.user.email])
        except Exception as e:
            logger.error(u'[UserControl]用户重置密码邮件发送失败:[%s]/[%s]' % (username,email))

                    


