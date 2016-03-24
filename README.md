Some helper functions for browsing CSV files from http://ted.openspending.org/#get-the-data

## Installation

    pip install

## Usage

    from modules.ted import Ted

    ted = Ted('test.csv')

    ted.apply_filter('country', 'DE')
    ted.apply_filter('security')

    # The company list will be deduped
    companies = ted.get_companies()
    print companies

## Filters

 * `security`: Security related CPV codes, i.e. the 35XXXXX cluster, except flags and flagpoles
 * `country`: Items related to a country (ISO 3166-1 alpha-2)