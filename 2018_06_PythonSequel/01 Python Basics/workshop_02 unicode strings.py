# coding: utf-8
from __future__ import print_function

motivational_statement_without_unicode = 'GÖ FÖŘ ÍT!!'
motivational_statement = u'GÖ FÖŘ ÍT!!'
print(motivational_statement)

print(len(motivational_statement_without_unicode))
print(len(motivational_statement))

for character in motivational_statement:
    print(character)
