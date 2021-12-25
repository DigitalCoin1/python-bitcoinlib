# Copyright (C) 2012-2018 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.


import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.11.1dev'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\x2d\x3f\xa2\xf5'
    DEFAULT_PORT = 55680
    RPC_PORT = 55681
    DNS_SEEDS = (('seed1.sperocoin.org', 'seed2.sperocoin.org'),
                 ('seed3.sperocoin.org', 'seed4.sperocoin.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':63,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}
    BECH32_HRP = 'spr'

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'),
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tb'

class SigNetParams(bitcoin.core.CoreSigNetParams):
    MESSAGE_START = b'\x0a\x03\xcf\x40'
    DEFAULT_PORT = 38333
    RPC_PORT = 38332
    DNS_SEEDS = (("signet.bitcoin.sprovoost.nl", "seed.signet.bitcoin.sprovoost.nl"))

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18443
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'bcrt'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
