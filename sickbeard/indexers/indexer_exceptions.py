#!/usr/bin/env python2
#encoding:utf-8
#project:indexer_api
#license:unlicense (http://unlicense.org/)

"""Custom exceptions used or raised by indexer_api"""

from lib.tvdb_api.tvdb_exceptions import \
    tvdb_exception, tvdb_attributenotfound, tvdb_episodenotfound, tvdb_error, \
    tvdb_seasonnotfound, tvdb_shownotfound, tvdb_userabort

indexerExcepts = ["indexer_exception", "indexer_error", "indexer_userabort", "indexer_shownotfound",
                  "indexer_seasonnotfound", "indexer_episodenotfound", "indexer_attributenotfound"]

tvdbExcepts = ["tvdb_exception", "tvdb_error", "tvdb_userabort", "tvdb_shownotfound",
               "tvdb_seasonnotfound", "tvdb_episodenotfound", "tvdb_attributenotfound"]

# link API exceptions to our exception handler
indexer_exception = tvdb_exception
indexer_error = tvdb_error
indexer_userabort = tvdb_userabort
indexer_attributenotfound = tvdb_attributenotfound
indexer_episodenotfound = tvdb_episodenotfound
indexer_seasonnotfound = tvdb_seasonnotfound
indexer_shownotfound = tvdb_shownotfound