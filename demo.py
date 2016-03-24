from modules.ted import Ted

ted = Ted('test.csv')

ted.apply_filter('country', 'DE')
ted.apply_filter('security')

companies = ted.get_companies()
print companies
