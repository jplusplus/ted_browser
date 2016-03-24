# -*- coding: utf-8 -*-

from csvkit import DictReader

DOCUMENTS_URL = 'http://ted.openspending.org/data/ted-documents.csv'
CONTRACTS_URL = 'http://ted.openspending.org/data/ted-contracts.csv'


class Ted(object):
    """ Represents tabular ted data from
        http://ted.openspending.org/#get-the-data
    """

    _filename = None
    _data = None

    def __init__(self, filename=None):
        """ Data will be loaded     in memory until needed. """
        self._filename = filename

    def _load(self, lambda_):
        """ Load data, applying a filter on the fly """
        self._data = []
        if self._filename is None:
            # TODO: Fetch the file from the site
            raise NotImplementedError(
                    "You still need to download the file(s) manually"
                  )
        else:
            with open(self._filename, 'rb') as file_:
                reader = DictReader(file_, delimiter=',')
                self._data = filter(lambda_, reader)

    def apply_filter(self, filter_, *args, **kwargs):
        """ Load the data if not already loaded,
            and apply a filter.
        """
        if filter_ == 'country':
            """ This filter checks if any of the 'country_cols' columns
                starts with `country`
            """
            country = args[0]
            country_cols = ["contract_authority_country",
                            "contract_location_nuts",
                            "contract_operator_country",
                            "document_orig_nuts_code",
                            "document_iso_country",
                            ]
            filter_function = lambda row, country=country: True if country in [v[:2].upper() for k, v in row.iteritems() if k in country_cols] else False
        elif filter_ == 'security':
            """ This filter singles out rows with security related CPV codes, i.e.
                the 35XXXXX cluster, except flags and flagpoles
            """
            filter_function = lambda row: True if int(row["contract_cpv_code"]) >= 3500000 and int(row["contract_cpv_code"]) < 35821000 else False

        if self._data is None:
            self._load(filter_function)
        else:
            self._data = filter(filter_function, self._data)

    def _get_column(self, col_head):
        return [row[col_head] for row in self._data]

    def get_companies(self):
        if self._data is None:
            # Return everything
            self._load(lambda row: row)

        companies = self._get_column('contract_operator_official_name')
        return list(set(companies))

    def dump(self):
        if self._data is None:
            # Return everything
            self._load(lambda row: row)
        return self._data
