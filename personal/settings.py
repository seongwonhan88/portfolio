TITLE = 'title'
BANNER = 'banner'
EMAIL = 'email'
FORM = 'form'
DISCLAIMER = 'disclaimer'
STYLE = 'style'
STATES = 'states'

EMAIL_ADDRESS = 'seongwonhan88@gmail.com'
SUBJECT_DEFAULT = 'Hello Seongwon,'

DEFAULT_REPLY_TEMPLATE = 'email/default_reply.html'
DEFAULT_NOTICE_TEMPLATE = 'email/default_notice.html'

TITLE_HOME = 'Home'
BANNER_HOME = 'My name is <em>Seongwon</em>. <br class="rsp-break"> I\'m a <em>Web Developer</em> living in Ann Arbor, MI'

TITLE_CONTACT = 'Contact Me'
BANNER_CONTACT = 'Let\'s <em>get in touch!</em>'
CHOICES = [('general', 'General Interest'), ('project', 'Project Offer'), ('bug', 'Bug Report')]

TITLE_SAMPLE_API = 'Sample API'
BANNER_SAMPLE_API = 'Check the latest <em>COVID19 updates</em>'
COVID_SAMPLE_API = 'https://github.com/novelcovid/api'
DISCLAIMER_SAMPLE_API = f'Disclaimer: The original data is pulled from ' \
                        f'<a href="{COVID_SAMPLE_API}">{COVID_SAMPLE_API}</a>. <br> ' \
                        f'The back-end server is working as a middleware to filter data by each state.'
