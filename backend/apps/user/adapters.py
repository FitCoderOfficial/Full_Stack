from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login
from allauth.socialaccount.models import SocialAccount
from django.conf import settings

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        print("pre_social_login called")
        print("Provider:", sociallogin.account.provider)
        print("Extra data:", sociallogin.account.extra_data)
        # 소셜 로그인이 완료된 후에 호출됩니다.
        user = sociallogin.user
        if user.id:
            # 기존 사용자: 이미 존재하는 경우
            return

        # 새로운 사용자: 소셜 어카운트 정보를 바탕으로 User 모델 업데이트
        social_account = SocialAccount.objects.filter(provider=sociallogin.account.provider, uid=sociallogin.account.uid).first()
        if social_account:
            # 프로필 이미지 URL 가져오기
            if social_account.provider == 'google':
                picture_url = social_account.extra_data.get('picture')
                
            elif social_account.provider == 'facebook':
                picture_url = social_account.extra_data.get('picture', {}).get('data', {}).get('url')
                
                
            # User 모델의 이미지 필드 업데이트
            if picture_url:
                user.picture_url = picture_url
                user.save()
