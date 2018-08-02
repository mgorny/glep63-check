# glep63-check -- tests for other key issues
# (c) 2018 Michał Górny
# Released under the terms of 2-clause BSD license.

import datetime

from glep63.base import (PublicKey, Key, UID, KeyAlgo, Validity,
        KeyWarning, KeyIssue, SubKeyWarning, SubKeyIssue, UIDIssue)

import tests.key_base


class ExpiredKeyTest(tests.key_base.BaseKeyTest):
    KEY_FILE = 'other/expired-key.gpg'

    GPG_COLONS = '''
pub:e:4096:1:DB44A8BC23B67AF4:946681246:946767646::-:::sc::::::23::0:
fpr:::::::::723AADD29743D410B5CAD9CEDB44A8BC23B67AF4:
uid:e::::946681246::0DAFDC73F43FC173C2216BA2BB4928391676BF2F::GLEP63 test key <nobody@gentoo.org>::::::::::0:
sub:e:4096:1:D4E7C940C84DD0DA:946681260:1545865383:::::s::::::23:
fpr:::::::::A23A271C81A008C088BB0A2CD4E7C940C84DD0DA:
'''

    KEY = PublicKey(
        validity=Validity.EXPIRED,
        key_length=4096,
        key_algo=KeyAlgo.RSA,
        keyid='DB44A8BC23B67AF4',
        creation_date=datetime.datetime(1999, 12, 31, 23, 0, 46),
        expiration_date=datetime.datetime(2000, 1, 1, 23, 0, 46),
        key_caps='sc',
        curve='',
        subkeys=[
            Key(
                validity=Validity.EXPIRED,
                key_length=4096,
                key_algo=KeyAlgo.RSA,
                keyid='D4E7C940C84DD0DA',
                creation_date=datetime.datetime(1999, 12, 31, 23, 1),
                expiration_date=datetime.datetime(2018, 12, 26, 23, 3, 3),
                key_caps='s',
                curve='',
            ),
        ],
        uids=[
            UID(
                validity='e',
                creation_date=datetime.datetime(1999, 12, 31, 23, 0, 46),
                expiration_date=None,
                uid_hash='0DAFDC73F43FC173C2216BA2BB4928391676BF2F',
                user_id='GLEP63 test key <nobody@gentoo.org>',
            ),
        ],
    )

    COMMON_ISSUE = KeyIssue(
        key=KEY,
        machine_desc='validity:expired',
        long_desc='',
    )

    EXPECTED_RESULTS = {
        'glep63-1-rsa2048': [COMMON_ISSUE],
        'glep63-1-rsa2048-ec25519': [COMMON_ISSUE],
        'glep63-1-strict': [COMMON_ISSUE],
        'glep63-2': [COMMON_ISSUE],
        'glep63-2-draft-20180707': [COMMON_ISSUE],
    }


class RevokedKeyTest(tests.key_base.BaseKeyTest):
    KEY_FILE = 'other/revoked-key.gpg'

    GPG_COLONS = '''
pub:r:4096:1:CD407D01E7D00880:946682289:978218289::-:::sc::::::23::0:
fpr:::::::::F0769AC027B2117ECFAB7F1BCD407D01E7D00880:
uid:r::::946682289::0DAFDC73F43FC173C2216BA2BB4928391676BF2F::GLEP63 test key <nobody@gentoo.org>::::::::::0:
sub:r:4096:1:F9FDA2910B574DA4:946682301:978218301:::::s::::::23:
fpr:::::::::A76730D5141B96EFAA7B3E4AF9FDA2910B574DA4:
'''

    KEY = PublicKey(
        validity=Validity.REVOKED,
        key_length=4096,
        key_algo=KeyAlgo.RSA,
        keyid='CD407D01E7D00880',
        creation_date=datetime.datetime(1999, 12, 31, 23, 18, 9),
        expiration_date=datetime.datetime(2000, 12, 30, 23, 18, 9),
        key_caps='sc',
        curve='',
        subkeys=[
            Key(
                validity=Validity.REVOKED,
                key_length=4096,
                key_algo=KeyAlgo.RSA,
                keyid='F9FDA2910B574DA4',
                creation_date=datetime.datetime(1999, 12, 31, 23, 18, 21),
                expiration_date=datetime.datetime(2000, 12, 30, 23, 18, 21),
                key_caps='s',
                curve='',
            ),
        ],
        uids=[
            UID(
                validity='r',
                creation_date=datetime.datetime(1999, 12, 31, 23, 18, 9),
                expiration_date=None,
                uid_hash='0DAFDC73F43FC173C2216BA2BB4928391676BF2F',
                user_id='GLEP63 test key <nobody@gentoo.org>',
            ),
        ],
    )

    COMMON_ISSUE = KeyIssue(
        key=KEY,
        machine_desc='validity:revoked',
        long_desc='',
    )

    EXPECTED_RESULTS = {
        'glep63-1-rsa2048': [COMMON_ISSUE],
        'glep63-1-rsa2048-ec25519': [COMMON_ISSUE],
        'glep63-1-strict': [COMMON_ISSUE],
        'glep63-2': [COMMON_ISSUE],
        'glep63-2-draft-20180707': [COMMON_ISSUE],
    }


class NoSigningSubKeyTest(tests.key_base.BaseKeyTest):
    KEY_FILE = 'other/no-signing-subkey.gpg'

    GPG_COLONS = '''
pub:-:4096:1:D2BADCAF3ECE4634:1533216330:1564752330::-:::scSC::::::23::0:
fpr:::::::::4A1ECCE29043E1723862D7EFD2BADCAF3ECE4634:
uid:-::::1533216330::0DAFDC73F43FC173C2216BA2BB4928391676BF2F::GLEP63 test key <nobody@gentoo.org>::::::::::0:
'''

    KEY = PublicKey(
        validity=Validity.NO_VALUE,
        key_length=4096,
        key_algo=KeyAlgo.RSA,
        keyid='D2BADCAF3ECE4634',
        creation_date=datetime.datetime(2018, 8, 2, 13, 25, 30),
        expiration_date=datetime.datetime(2019, 8, 2, 13, 25, 30),
        key_caps='scSC',
        curve='',
        subkeys=[
        ],
        uids=[
            UID(
                validity='-',
                creation_date=datetime.datetime(2018, 8, 2, 13, 25, 30),
                expiration_date=None,
                uid_hash='0DAFDC73F43FC173C2216BA2BB4928391676BF2F',
                user_id='GLEP63 test key <nobody@gentoo.org>',
            ),
        ],
    )

    COMMON_ISSUE = KeyIssue(
        key=KEY,
        machine_desc='subkey:none',
        long_desc='',
    )

    EXPECTED_RESULTS = {
        'glep63-1-rsa2048': [COMMON_ISSUE],
        'glep63-1-rsa2048-ec25519': [COMMON_ISSUE],
        'glep63-1-strict': [COMMON_ISSUE],
        'glep63-2': [COMMON_ISSUE],
        'glep63-2-draft-20180707': [COMMON_ISSUE],
    }


class MultipurposeSubKeyTest(tests.key_base.BaseKeyTest):
    KEY_FILE = 'other/multipurpose-subkey.gpg'

    GPG_COLONS = '''
pub:-:4096:1:D2BADCAF3ECE4634:1533216330:1564752330::-:::scESC::::::23::0:
fpr:::::::::4A1ECCE29043E1723862D7EFD2BADCAF3ECE4634:
uid:-::::1533216330::0DAFDC73F43FC173C2216BA2BB4928391676BF2F::GLEP63 test key <nobody@gentoo.org>::::::::::0:
sub:-:4096:1:EC398A2746705B74:1533216464:1564752464:::::es::::::23:
fpr:::::::::2E9DB9ECD909BDD449B0E4D8EC398A2746705B74:
'''

    KEY = PublicKey(
        validity=Validity.NO_VALUE,
        key_length=4096,
        key_algo=KeyAlgo.RSA,
        keyid='D2BADCAF3ECE4634',
        creation_date=datetime.datetime(2018, 8, 2, 13, 25, 30),
        expiration_date=datetime.datetime(2019, 8, 2, 13, 25, 30),
        key_caps='scESC',
        curve='',
        subkeys=[
            Key(
                validity=Validity.NO_VALUE,
                key_length=4096,
                key_algo=KeyAlgo.RSA,
                keyid='EC398A2746705B74',
                creation_date=datetime.datetime(2018, 8, 2, 13, 27, 44),
                expiration_date=datetime.datetime(2019, 8, 2, 13, 27, 44),
                key_caps='es',
                curve='',
            ),
        ],
        uids=[
            UID(
                validity='-',
                creation_date=datetime.datetime(2018, 8, 2, 13, 25, 30),
                expiration_date=None,
                uid_hash='0DAFDC73F43FC173C2216BA2BB4928391676BF2F',
                user_id='GLEP63 test key <nobody@gentoo.org>',
            ),
        ],
    )

    COMMON_ISSUES = [
        SubKeyWarning(
            key=KEY,
            subkey=KEY.subkeys[0],
            machine_desc='subkey:multipurpose',
            long_desc='',
        ),
        KeyIssue(
            key=KEY,
            machine_desc='subkey:none',
            long_desc='',
        ),
    ]

    EXPECTED_RESULTS = {
        'glep63-1-rsa2048': COMMON_ISSUES,
        'glep63-1-rsa2048-ec25519': COMMON_ISSUES,
        'glep63-1-strict': COMMON_ISSUES,
        'glep63-2': COMMON_ISSUES,
        'glep63-2-draft-20180707': COMMON_ISSUES,
    }
