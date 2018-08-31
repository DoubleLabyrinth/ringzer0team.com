#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5

PrivateKey = '-----BEGIN RSA PRIVATE KEY-----\n'                                    \
             'MIICXgIBAAKBgQDwkrxVrZ+KCl1cX27SHDI7EfgnFJZ0qTHUD6uEeSoZsiVkcu0/\n'   \
             'XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3Lqqwcuhgypd3Sf/bH3z4tC25\n'   \
             'eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIUtmpouI1IXqxjrDx2SQIDAQAB\n'   \
             'AoGBAOwd6PFitnpiz90w4XEhMX/elCOvRjh8M6bCNoKP9W1A9whO8GJHRnDgXio6\n'   \
             '/2XXktBU5OfCVJk7uei6or4J9BvXRxQpn1GvOYRwwQa9E54GS0Yu1XxTPtnBlqKZ\n'   \
             'KRbmVNpv7eZyZfYG+V+/f53cgu6M4U3SE+9VTlggfZ8iSqGBAkEA/XvFz7Nb7mIC\n'   \
             'qzQpNmpKeN4PBVRJBXqHTj0FcqQ5POZTX6scgE3LrxVKSICmm6ungenPXQrdEQ27\n'   \
             'yNQsfASFGQJBAPL2JsjakvTVUIe2JyP99CxF5WuK2e0y6N2sU3n9t0lde9DRFs1r\n'   \
             'mhbIyIGZ0fIkuwZSOqVGb0K4W1KWypCd8LECQQCRKIIc8R9iIepZVGONb8z57mA3\n'   \
             'sw6l/obhfPxTrEvC3js8e+a0atiLiOujHVlLqD8inFxNcd0q2OyCk05uLsBxAkEA\n'   \
             'vWkRC3z7HExAn8xt7y1Ickt7c7+n7bfGuyphWbVmcpeis0SOVk8QrbqSNhdJCVGB\n'   \
             'TIhGmBq1GnrHFzffa6b1wQJAR7d8hFRtp7uFx5GFFEpFIJvs/SlnXPvOIBmzBvjU\n'   \
             'yGglag8za2A8ArHZwA1jXcFPawuJEmeZWo+5/MWp0j+yzQ==\n'                   \
             '-----END RSA PRIVATE KEY-----\n'

Rsa = RSA.import_key(PrivateKey)
PublicKey = Rsa.publickey().export_key('PEM')

# remove header
PublicKey = PublicKey.replace(b'-----BEGIN PUBLIC KEY-----', b'')
# remove tailer
PublicKey = PublicKey.replace(b'-----END PUBLIC KEY-----', b'')
# remove '\n'
PublicKey = PublicKey.replace(b'\n', b'')

print(PublicKey.decode())
print('MD5 = %s' % MD5.new(PublicKey).hexdigest())
