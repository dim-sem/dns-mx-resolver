#!/usr/bin/env python
import dns.resolver

email_address = 'gmail.com'
mx = []
for mx_record in dns.resolver.query(email_address,'MX'):
    mx.append(mx_record.to_text().split(' ')[1][:-1])
print sorted(mx)