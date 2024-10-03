AUTHENTICATION_SOURCES = ['oauth2', 'internal']
OAUTH2_AUTO_CREATE_USER = True
OAUTH2_CONFIG = [{
	'OAUTH2_NAME' : 'authentik',
	'OAUTH2_DISPLAY_NAME' : '<display-name>',
	'OAUTH2_CLIENT_ID' : '<client-id>',
	'OAUTH2_CLIENT_SECRET' : '<client-secret>',
	'OAUTH2_TOKEN_URL' : 'https://authentik.company/application/o/token/',
	'OAUTH2_AUTHORIZATION_URL' : 'https://authentik.company/application/o/authorize/',
	'OAUTH2_API_BASE_URL' : 'https://authentik.company/',
	'OAUTH2_USERINFO_ENDPOINT' : 'https://authentik.company/application/o/userinfo/',
	'OAUTH2_SERVER_METADATA_URL' : 'https://authentik.company/application/o/<app-slug>/.well-known/openid-configuration',
	'OAUTH2_SCOPE' : 'openid email profile',
	'OAUTH2_ICON' : '<fontawesome-icon>',
	'OAUTH2_BUTTON_COLOR' : '<button-color>'
}]