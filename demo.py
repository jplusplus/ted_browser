from modules.ted import Ted

ted = Ted('test.csv')

ted.apply_filter('security')
ted.apply_filter('country', 'DE')

companies = ted.get_companies()
print companies
