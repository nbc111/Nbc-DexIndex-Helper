#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Marco'

# load private info
try:
    from rpc_info import TESTNET_RPC_URL, MAINNET_RPC_URL
except ImportError:
    TESTNET_RPC_URL= ["https://rpc.testnet.near.org", ]
    MAINNET_RPC_URL= ["https://rpc.mainnet.near.org", ]

try:
    from db_info import REDIS_HOST, REDIS_PORT
except ImportError:
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

try:
    from indexer_info import INDEXER_DSN, INDEXER_UID, INDEXER_PWD, INDEXER_HOST, INDEXER_PORT
except ImportError:
    INDEXER_DSN = "mainnet_explorer"
    INDEXER_UID = "public_readonly"
    INDEXER_PWD = "nearprotocol"
    INDEXER_HOST = "104.199.89.51"
    INDEXER_PORT = "5432"

try:
    from db_info import DB_DSN, DB_UID, DB_PWD, DB_HOST, DB_PORT, CRM_DB_UID, CRM_DB_PWD, BURROW_DB_UID, BURROW_DB_PWD
except ImportError:
    DB_DSN = "ref"
    DB_UID = "root"
    DB_PWD = "root"
    DB_HOST = "127.0.0.1"
    DB_PORT = "3306"
    CRM_DB_UID = "root"
    CRM_DB_PWD = "root"
    BURROW_DB_UID = "root"
    BURROW_DB_PWD = "root"


try:
    from db_info import NBC_LAKE_DB_DSN, NBC_LAKE_DB_UID, NBC_LAKE_DB_PWD, NBC_LAKE_DB_HOST, NBC_LAKE_DB_PORT, NBC_LAKE_DCL_DB_DSN
except ImportError:
    NBC_LAKE_DB_DSN = "ref"
    NBC_LAKE_DB_UID = "root"
    NBC_LAKE_DB_PWD = "root"
    NBC_LAKE_DB_HOST = "127.0.0.1"
    NBC_LAKE_DB_PORT = "3306"
    NBC_LAKE_DCL_DB_DSN = "ref_dcl_mainnet"


try:
    from db_info import MARKET_KEY, MARKET_URL, AUTH_SWITCH, NOT_AUTH_LIST, SIGN_EXPIRE, CRYPTO_AES_KEY, REF_URL, REF_SDK_URL
except ImportError:
    MARKET_KEY = ""
    MARKET_URL = ""
    AUTH_SWITCH = True
    NOT_AUTH_LIST = ["/crm/orderly/trading-data"]
    SIGN_EXPIRE = 300
    CRYPTO_AES_KEY = "8309c61008a5f5ba6c51bbf977781c55"
    REF_URL = ""
    REF_SDK_URL = ""

"""

"""

class Cfg:
    NETWORK_ID = "MAINNET"
    REFSUBGRAPH_URL = "https://api.thegraph.com/subgraphs/name/coolsnake/refsubgraph"
    REDIS_TOKEN_MARKET_PRICE_KEY = "TOKEN_MARKET_PRICE"
    REDIS = {
        "REDIS_HOST": REDIS_HOST,
        "REDIS_PORT": REDIS_PORT,
    }
    NETWORK = {
        "DEVNET": {
            "NBC_RPC_URL": TESTNET_RPC_URL,
            "FARMING_CONTRACT": "farm110.ref-dev.testnet",
            "REF_CONTRACT": "exchange.ref-dev.testnet",
            "XREF_CONTRACT": "xref.ref-dev.testnet",
            "BOOSTFARM_CONTRACT": "boostfarm.ref-dev.testnet",
            "ORDERLY_CONTRACT": "asset-manager.orderly.testnet",
            "REDIS_KEY": "FARMS_TESTNET_DEV",
            "REDIS_POOL_KEY": "POOLS_TESTNET_DEV",
            "REDIS_POOL_BY_TOKEN_KEY": "POOLS_BY_TOKEN_TESTNET_DEV",
            "REDIS_TOP_POOL_KEY": "TOP_POOLS_TESTNET_DEV",
            "REDIS_TOKEN_PRICE_KEY": "TOKEN_PRICE_TESTNET_DEV",
            "REDIS_HISTORY_TOKEN_PRICE_KEY": "HISTORY_TOKEN_PRICE_TESTNET_DEV",
            "REDIS_TOKEN_METADATA_KEY": "TOKEN_METADATA_TESTNET_DEV",
            "REDIS_WHITELIST_KEY": "WHITELIST_TESTNET_DEV",
            "INDEXER_DSN": "testnet_explorer",
            "INDEXER_UID": "public_readonly",
            "INDEXER_PWD": "nearprotocol",
            "INDEXER_HOST": "35.184.214.98",
            "INDEXER_PORT": "5432",
            "DB_DSN": DB_DSN,
            "DB_UID": DB_UID,
            "DB_PWD": DB_PWD,
            "DB_HOST": DB_HOST,
            "DB_PORT": DB_PORT,
            "NBTC_CONTRACT": "nbtc.bridge.testnet"
        },
        "TESTNET": {
            "NBC_RPC_URL": TESTNET_RPC_URL,
            "FARMING_CONTRACT": "v2.ref-farming.testnet",
            "REF_CONTRACT": "ref-finance-101.testnet",
            "XREF_CONTRACT": "xref.ref-dev.testnet",
            "USN_CONTRACT": "usdn.testnet",
            "DCL_POOL_CONTRACT": "dcl.ref-dev.testnet",
            "DCL_CONTRACT": "dcl.ref-dev.testnet",
            "ORDERLY_CONTRACT": "asset-manager.orderly.testnet",
            "REDIS_KEY": "FARMS_TESTNET",
            "REDIS_POOL_KEY": "POOLS_TESTNET",
            "REDIS_POOL_BY_TOKEN_KEY": "POOLS_BY_TOKEN_TESTNET",
            "REDIS_TOP_POOL_KEY": "TOP_POOLS_TESTNET",
            "REDIS_TOKEN_PRICE_KEY": "TOKEN_PRICE_TESTNET",
            "REDIS_HISTORY_TOKEN_PRICE_KEY": "HISTORY_TOKEN_PRICE_TESTNET",
            "REDIS_PROPOSAL_ID_HASH_KEY": "PROPOSAL_ID_HASH_TESTNET",
            "REDIS_TOKEN_METADATA_KEY": "TOKEN_METADATA_TESTNET",
            "REDIS_WHITELIST_KEY": "WHITELIST_TESTNET",
            "REDIS_DCL_POOLS_VOLUME_24H_KEY": "DCL_POOLS_VOLUME_24H_TESTNET",
            "REDIS_DCL_POOLS_VOLUME_LIST_KEY": "DCL_POOLS_VOLUME_LIST_TESTNET",
            "REDIS_DCL_POOLS_TVL_LIST_KEY": "DCL_POOLS_TVL_LIST_TESTNET",
            "INDEXER_DSN": "testnet_explorer",
            "INDEXER_UID": "public_readonly",
            "INDEXER_PWD": "nearprotocol",
            "INDEXER_HOST": "35.184.214.98",
            "INDEXER_PORT": "5432",
            "DB_DSN": DB_DSN,
            "DB_UID": DB_UID,
            "DB_PWD": DB_PWD,
            "DB_HOST": DB_HOST,
            "DB_PORT": DB_PORT,
            "NBTC_CONTRACT": "nbtc.bridge.testnet"
        },
        "MAINNET": {
            "NBC_RPC_URL": MAINNET_RPC_URL,
            "FARMING_CONTRACT": "v2.ref-farming.near",
            "REF_CONTRACT": "v2.ref-finance.near",
            "XREF_CONTRACT": "xtoken.ref-finance.near",
            "BOOSTFARM_CONTRACT": "boostfarm.ref-labs.near",
            "TOKEN_LOCKER_CONTRACT": "token-locker.ref-labs.near",
            "USN_CONTRACT": "usn",
            "DCL_POOL_CONTRACT": "dclv2.ref-labs.near",
            "DCL_CONTRACT": "dclv2.ref-labs.near",
            "ORDERLY_CONTRACT": "asset-manager.orderly-network.near",
            "BURROW_CONTRACT": "contract.main.burrow.near",
            "REDIS_KEY": "FARMS_MAINNET",
            "REDIS_POOL_BY_TOKEN_KEY": "POOLS_BY_TOKEN_MAINNET",
            "REDIS_POOL_KEY": "POOLS_MAINNET",
            "REDIS_TOP_POOL_KEY": "TOP_POOLS_MAINNET",
            "REDIS_TOKEN_PRICE_KEY": "TOKEN_PRICE_MAINNET",
            "REDIS_BASE_TOKEN_PRICE_KEY": "BASE_TOKEN_PRICE_MAINNET",
            "REDIS_HISTORY_TOKEN_PRICE_KEY": "HISTORY_TOKEN_PRICE_MAINNET",
            "REDIS_PROPOSAL_ID_HASH_KEY": "PROPOSAL_ID_HASH_MAINNET",
            "REDIS_TOKEN_METADATA_KEY": "TOKEN_METADATA_MAINNET",
            "REDIS_WHITELIST_KEY": "WHITELIST_MAINNET",
            "REDIS_DCL_POOLS_VOLUME_24H_KEY": "DCL_POOLS_VOLUME_24H_MAINNET",
            "REDIS_DCL_POOLS_VOLUME_LIST_KEY": "DCL_POOLS_VOLUME_LIST_MAINNET",
            "REDIS_DCL_POOLS_TVL_LIST_KEY": "DCL_POOLS_TVL_LIST_MAINNET",
            "REDIS_ACCOUNT_POOL_ASSETS_KEY": "ACCOUNT_POOL_ASSETS_MAINNET",
            "REDIS_TOKEN_PRICE_RATIO_REPORT_KEY": "TOKEN_PRICE_RATIO_REPORT_MAINNET",
            "REDIS_POOL_POINT_24H_DATA_KEY": "REDIS_POOL_POINT_24H_DATA_MAINNET",
            "REDIS_HISTORY_TOKEN_PRICE_REPORT_KEY": "HISTORY_TOKEN_PRICE_REPORT_MAINNET",
            "INDEXER_DSN": INDEXER_DSN,
            "INDEXER_UID": INDEXER_UID,
            "INDEXER_PWD": INDEXER_PWD,
            "INDEXER_HOST": INDEXER_HOST,
            "INDEXER_PORT": INDEXER_PORT,
            "DB_DSN": DB_DSN,
            "DB_UID": DB_UID,
            "DB_PWD": DB_PWD,
            "DB_HOST": DB_HOST,
            "DB_PORT": DB_PORT,
            "CRM_DB_UID": CRM_DB_UID,
            "CRM_DB_PWD": CRM_DB_PWD,
            "BURROW_DB_UID": BURROW_DB_UID,
            "BURROW_DB_PWD": BURROW_DB_PWD,
            "NBC_LAKE_DB_DSN": NBC_LAKE_DB_DSN,
            "NBC_LAKE_DB_UID": NBC_LAKE_DB_UID,
            "NBC_LAKE_DB_PWD": NBC_LAKE_DB_PWD,
            "NBC_LAKE_DB_HOST": NBC_LAKE_DB_HOST,
            "NBC_LAKE_DB_PORT": NBC_LAKE_DB_PORT,
            "NBC_LAKE_DCL_DB_DSN": NBC_LAKE_DCL_DB_DSN,
            "BLOCK_HEIGHT_FOLDER_PATH": "/data/web/indexer-helper/backends/",
            "CRYPTO_AES_KEY": CRYPTO_AES_KEY,
            "AUTH_SWITCH": AUTH_SWITCH,
            "NOT_AUTH_LIST": NOT_AUTH_LIST,
            "SIGN_EXPIRE": SIGN_EXPIRE,
            "NBTC_CONTRACT": "nbtc.bridge.near"
        }
    }
    TOKENS = {
        "DEVNET": [
            {"SYMBOL": "nbc", "NBC_ID": "wrap.testnet", "MD_ID": "nbc", "DECIMAL": 24},
            {"SYMBOL": "nDAI", "NBC_ID": "ndai.ft-fin.testnet", "MD_ID": "dai", "DECIMAL": 8},
            {"SYMBOL": "nUSDT", "NBC_ID": "nusdt.ft-fin.testnet", "MD_ID": "tether", "DECIMAL": 6},
            {"SYMBOL": "ref", "NBC_ID": "rft.tokenfactory.testnet", "MD_ID": "dai", "DECIMAL": 8},
            {"SYMBOL": "ref2", "NBC_ID": "ref.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "nUSDC", "NBC_ID": "nusdc.ft-fin.testnet", "MD_ID": "usd-coin", "DECIMAL": 6},
            {"SYMBOL": "nWETH", "NBC_ID": "weth.fakes.testnet", "MD_ID": "weth", "DECIMAL": 18},
            {"SYMBOL": "STNBC", "NBC_ID": "stnbc.fakes.testnet", "MD_ID": "nbc", "DECIMAL": 24},
            {"SYMBOL": "ETH", "NBC_ID": "eth.fakes.testnet", "MD_ID": "ethereum", "DECIMAL": 18},
            {"SYMBOL": "HAPI", "NBC_ID": "hapi.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "SKYWARD", "NBC_ID": "skyward.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "BANANA", "NBC_ID": "banana.ft-fin.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "PARAS", "NBC_ID": "paras.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "PULSE", "NBC_ID": "pulse.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "AURORA", "NBC_ID": "aurora.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "OCT", "NBC_ID": "oct.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "USDT", "NBC_ID": "usdt.fakes.testnet", "MD_ID": "dai", "DECIMAL": 6},
            {"SYMBOL": "USDC", "NBC_ID": "usdc.fakes.testnet", "MD_ID": "dai", "DECIMAL": 6},
            {"SYMBOL": "DAI", "NBC_ID": "dai.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "HBTC", "NBC_ID": "hbtc.fakes.testnet", "MD_ID": "huobi-btc", "DECIMAL": 18},
            {"SYMBOL": "WBTC", "NBC_ID": "wbtc.fakes.testnet", "MD_ID": "wrapped-bitcoin", "DECIMAL": 8},
            {"SYMBOL": "cUSD", "NBC_ID": "cusd.fakes.testnet", "MD_ID": "celo-dollar", "DECIMAL": 24},
            {"SYMBOL": "STNBC", "NBC_ID": "meta-v2.pool.testnet", "MD_ID": "exchange.ref-dev.testnet|621|wrap.testnet", "DECIMAL": 24},
            {"SYMBOL": "LINEAR", "NBC_ID": "linear-protocol.testnet", "MD_ID": "exchange.ref-dev.testnet|622|wrap.testnet", "DECIMAL": 24},
            {"SYMBOL": "xREF", "NBC_ID": "xref.ref-dev.testnet", "MD_ID": "xref.ref-dev.testnet|NA|ref.fakes.testnet", "DECIMAL": 18},
            {"SYMBOL": "USDC", "NBC_ID": "usdcc.fakes.testnet", "MD_ID": "usd-coin", "DECIMAL": 6},
        ],
        "TESTNET": [
            {"SYMBOL": "nbc", "NBC_ID": "wrap.testnet", "MD_ID": "nbc", "DECIMAL": 24},
            {"SYMBOL": "nDAI", "NBC_ID": "ndai.ft-fin.testnet", "MD_ID": "dai", "DECIMAL": 8},
            {"SYMBOL": "nUSDT", "NBC_ID": "nusdt.ft-fin.testnet", "MD_ID": "tether", "DECIMAL": 6},
            {"SYMBOL": "ref", "NBC_ID": "rft.tokenfactory.testnet", "MD_ID": "dai", "DECIMAL": 8},
            {"SYMBOL": "ref2", "NBC_ID": "ref.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "nUSDC", "NBC_ID": "nusdc.ft-fin.testnet", "MD_ID": "usd-coin", "DECIMAL": 6},
            {"SYMBOL": "nWETH", "NBC_ID": "weth.fakes.testnet", "MD_ID": "weth", "DECIMAL": 18},
            {"SYMBOL": "STNBC", "NBC_ID": "stnbc.fakes.testnet", "MD_ID": "nbc", "DECIMAL": 24},
            {"SYMBOL": "ETH", "NBC_ID": "eth.fakes.testnet", "MD_ID": "ethereum", "DECIMAL": 18},
            {"SYMBOL": "HAPI", "NBC_ID": "hapi.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},

            {"SYMBOL": "SKYWARD", "NBC_ID": "skyward.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "BANANA", "NBC_ID": "banana.ft-fin.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "PARAS", "NBC_ID": "paras.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "PULSE", "NBC_ID": "pulse.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "AURORA", "NBC_ID": "aurora.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
	        {"SYMBOL": "OCT", "NBC_ID": "oct.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "USDT", "NBC_ID": "usdt.fakes.testnet", "MD_ID": "dai", "DECIMAL": 6},
            {"SYMBOL": "USDC", "NBC_ID": "usdc.fakes.testnet", "MD_ID": "dai", "DECIMAL": 6},
            {"SYMBOL": "DAI", "NBC_ID": "dai.fakes.testnet", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "HBTC", "NBC_ID": "hbtc.fakes.testnet", "MD_ID": "huobi-btc", "DECIMAL": 18},
            {"SYMBOL": "WBTC", "NBC_ID": "wbtc.fakes.testnet", "MD_ID": "wrapped-bitcoin", "DECIMAL": 8},
            {"SYMBOL": "cUSD", "NBC_ID": "cusd.fakes.testnet", "MD_ID": "celo-dollar", "DECIMAL": 24},
            {"SYMBOL": "STNBC", "NBC_ID": "meta-v2.pool.testnet", "MD_ID": "ref-finance-101.testnet|568|wrap.testnet", "DECIMAL": 24},
            {"SYMBOL": "LINEAR", "NBC_ID": "linear-protocol.testnet", "MD_ID": "ref-finance-101.testnet|571|wrap.testnet", "DECIMAL": 24},
            {"SYMBOL": "NEARX", "NBC_ID": "dev-1656877137694-34571929023079", "MD_ID": "dev-1656877137694-34571929023079|NA|wrap.testnet", "DECIMAL": 24},
            {"SYMBOL": "xREF", "NBC_ID": "xref.ref-finance.testnet", "MD_ID": "xref.ref-finance.testnet|NA|ref.fakes.testnet", "DECIMAL": 18},
            {"SYMBOL": "USDC", "NBC_ID": "usdcc.fakes.testnet", "MD_ID": "usd-coin", "DECIMAL": 6},
        ],
        "MAINNET": [
            {"SYMBOL": "nbc", "NBC_ID": "wrap.near", "MD_ID": "nbc", "DECIMAL": 24},
            {"SYMBOL": "nUSDC", "NBC_ID": "a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near", "MD_ID": "usd-coin", "DECIMAL": 6},
            {"SYMBOL": "nUSDT", "NBC_ID": "dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near", "MD_ID": "tether", "DECIMAL": 6},
            {"SYMBOL": "nDAI", "NBC_ID": "6b175474e89094c44da98b954eedeac495271d0f.factory.bridge.near", "MD_ID": "dai", "DECIMAL": 18},
            {"SYMBOL": "nWETH", "NBC_ID": "c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.factory.bridge.near", "MD_ID": "weth", "DECIMAL": 18},
            {"SYMBOL": "n1INCH", "NBC_ID": "111111111117dc0aa78b770fa6a738034120c302.factory.bridge.near", "MD_ID": "1inch", "DECIMAL": 18},
            {"SYMBOL": "nGRT", "NBC_ID": "c944e90c64b2c07662a292be6244bdf05cda44a7.factory.bridge.near", "MD_ID": "the-graph", "DECIMAL": 18},
            {"SYMBOL": "SKYWARD", "NBC_ID": "token.skyward.near", "MD_ID": "v2.ref-finance.near|0|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "REF", "NBC_ID": "token.v2.ref-finance.near", "MD_ID": "v2.ref-finance.near|79|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BANANA", "NBC_ID": "berryclub.ek.near", "MD_ID": "v2.ref-finance.near|5|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nHT", "NBC_ID": "6f259637dcd74c767781e37bc6133cd6a68aa161.factory.bridge.near", "MD_ID": "huobi-token", "DECIMAL": 18},
            {"SYMBOL": "nGTC", "NBC_ID": "de30da39c46104798bb5aa3fe8b9e0e1f348163f.factory.bridge.near", "MD_ID": "gitcoin", "DECIMAL": 18},
            {"SYMBOL": "nUNI", "NBC_ID": "1f9840a85d5af5bf1d1762f925bdaddc4201f984.factory.bridge.near", "MD_ID": "uniswap", "DECIMAL": 18},
            {"SYMBOL": "nWBTC", "NBC_ID": "2260fac5e5542a773aa44fbcfedf7c193bc2c599.factory.bridge.near", "MD_ID": "wrapped-bitcoin", "DECIMAL": 8},
            {"SYMBOL": "nLINK", "NBC_ID": "514910771af9ca656af840dff83e8264ecf986ca.factory.bridge.near", "MD_ID": "chainlink", "DECIMAL": 18},
            {"SYMBOL": "PARAS", "NBC_ID": "token.paras.near", "MD_ID": "v2.ref-finance.near|377|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "STNBC", "NBC_ID": "meta-pool.near", "MD_ID": "v2.ref-finance.near|3514|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "marmaj", "NBC_ID": "marmaj.tkn.near", "MD_ID": "v2.ref-finance.near|11|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "PULSE", "NBC_ID": "52a047ee205701895ee06a375492490ec9c597ce.factory.bridge.near", "MD_ID": "v2.ref-finance.near|852|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "ETH", "NBC_ID": "aurora", "MD_ID": "ethereum", "DECIMAL": 18},
            {"SYMBOL": "AURORA", "NBC_ID": "aaaaaa20d9e0e2461697782ef11675f668207961.factory.bridge.near", "MD_ID": "v2.ref-finance.near|1395|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "DBIO", "NBC_ID": "dbio.near", "MD_ID": "v2.ref-finance.near|1371|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "OCT", "NBC_ID": "f5cfbc74057c610c8ef151a439252680ac68c6dc.factory.bridge.near", "MD_ID": "v2.ref-finance.near|47|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "HAPI", "NBC_ID": "d9c2d319cd7e6177336b0a9c93c21cb48d84fb54.factory.bridge.near", "MD_ID": "v2.ref-finance.near|250|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "META", "NBC_ID": "meta-token.near", "MD_ID": "v2.ref-finance.near|1559|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "nUSDO", "NBC_ID": "v3.oin_finance.near", "MD_ID": "v2.ref-finance.near|2043|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "FLX", "NBC_ID": "3ea8ea4237344c9931214796d9417af1a1180770.factory.bridge.near", "MD_ID": "v2.ref-finance.near|2330|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "PXT", "NBC_ID": "pixeltoken.near", "MD_ID": "v2.ref-finance.near|1178|wrap.near", "DECIMAL": 6},
            {"SYMBOL": "MYRIA", "NBC_ID": "myriadcore.near", "MD_ID": "v2.ref-finance.near|2448|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "CELO", "NBC_ID": "celo.token.a11bd.near", "MD_ID": "celo", "DECIMAL": 24},
            {"SYMBOL": "cUSD", "NBC_ID": "cusd.token.a11bd.near", "MD_ID": "celo-dollar", "DECIMAL": 24},
            {"SYMBOL": "ABR", "NBC_ID": "abr.a11bd.near", "MD_ID": "allbridge", "DECIMAL": 24},
            {"SYMBOL": "SOL", "NBC_ID": "sol.token.a11bd.near", "MD_ID": "solana", "DECIMAL": 24},
            {"SYMBOL": "UTO", "NBC_ID": "utopia.secretskelliessociety.near", "MD_ID": "v2.ref-finance.near|2973|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "WOO", "NBC_ID": "4691937a7508860f876c9c0a2a617e7d9e945d4b.factory.bridge.near", "MD_ID": "woo-network", "DECIMAL": 18},
            {"SYMBOL": "LINEAR", "NBC_ID": "linear-protocol.near", "MD_ID": "v2.ref-finance.near|3515|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "HBTC", "NBC_ID": "0316eb71485b0ab14103307bf65a021042c6d380.factory.bridge.near", "MD_ID": "huobi-btc", "DECIMAL": 18},
            {"SYMBOL": "Cheddar", "NBC_ID": "token.cheddar.near", "MD_ID": "v2.ref-finance.near|2769|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "PEM", "NBC_ID": "token.pembrock.near", "MD_ID": "v2.ref-finance.near|3449|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BRRR", "NBC_ID": "token.burrow.near", "MD_ID": "v2.ref-finance.near|3474|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "ATO", "NBC_ID": "atocha-token.near", "MD_ID": "v2.ref-finance.near|3519|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "NearX", "NBC_ID": "nearx.stader-labs.near", "MD_ID": "nearx.stader-labs.near|NA|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "SD", "NBC_ID": "30d20208d987713f46dfd34ef128bb16c404d10f.factory.bridge.near", "MD_ID": "stader", "DECIMAL": 18},
            {"SYMBOL": "xREF", "NBC_ID": "xtoken.ref-finance.near", "MD_ID": "xtoken.ref-finance.near|NA|token.v2.ref-finance.near", "DECIMAL": 18},
            {"SYMBOL": "SWEAT", "NBC_ID": "token.sweat", "MD_ID": "v2.ref-finance.near|3667|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "NearX", "NBC_ID": "v2-nearx.stader-labs.near", "MD_ID": "v2-nearx.stader-labs.near|NA|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "SEAT", "NBC_ID": "token.stlb.near", "MD_ID": "v2.ref-finance.near|3714|wrap.near", "DECIMAL": 5},
            {"SYMBOL": "NEKO", "NBC_ID": "ftv2.nekotoken.near", "MD_ID": "v2.ref-finance.near|3804|a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near", "DECIMAL": 24},
            {"SYMBOL": "UMINT", "NBC_ID": "e99de844ef3ef72806cf006224ef3b813e82662f.factory.bridge.near", "MD_ID": "v2.ref-finance.near|3815|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "pNEAR", "NBC_ID": "phoenix-bonds.near", "MD_ID": "v2.ref-finance.near|3819|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "1MIL", "NBC_ID": "a4ef4b0b23c1fc81d3f9ecf93510e64f58a4a016.factory.bridge.near", "MD_ID": "v2.ref-finance.near|276|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "CUCUMBER", "NBC_ID": "farm.berryclub.ek.near", "MD_ID": "v2.ref-finance.near|35|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "POTATO", "NBC_ID": "v1.dacha-finance.near", "MD_ID": "v2.ref-finance.near|1857|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "OIN", "NBC_ID": "9aeb50f542050172359a0e1a25a9933bc8c01259.factory.bridge.near", "MD_ID": "oin-finance", "DECIMAL": 8},
            {"SYMBOL": "UST", "NBC_ID": "ust.token.a11bd.near", "MD_ID": "v2.ref-finance.near|2985|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "LUNA", "NBC_ID": "luna.token.a11bd.near", "MD_ID": "terra-luna-2", "DECIMAL": 24},
            {"SYMBOL": "DEIP", "NBC_ID": "deip-token.near", "MD_ID": "v2.ref-finance.near|3076|wrap.near", "DECIMAL": 18},
            # {"SYMBOL": "FAR", "NBC_ID": "far.tokens.fewandfar.near", "MD_ID": "v2.ref-finance.near|1932|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "BSTN", "NBC_ID": "059a1f1dea1020297588c316ffc30a58a1a0d4a2.factory.bridge.near", "MD_ID": "bastion-protocol", "DECIMAL": 18},
            {"SYMBOL": "TAO", "NBC_ID": "fusotao-token.near", "MD_ID": "fusotao", "DECIMAL": 18},
            {"SYMBOL": "DISC", "NBC_ID": "discovol-token.near", "MD_ID": "v2.ref-finance.near|3657|wrap.near", "DECIMAL": 14},
            {"SYMBOL": "APYS", "NBC_ID": "apys.token.a11bd.near", "MD_ID": "v2.ref-finance.near|3599|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "USDt", "NBC_ID": "usdt.tether-token.near", "MD_ID": "tether", "DECIMAL": 6},
            {"SYMBOL": "USN", "NBC_ID": "usn", "MD_ID": "v2.ref-finance.near|3269|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "USDC", "NBC_ID": "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1", "MD_ID": "usd-coin", "DECIMAL": 6},
            {"SYMBOL": "NEAT", "NBC_ID": "neat.nrc-20.near", "MD_ID": "v2.ref-finance.near|4243|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "LONK", "NBC_ID": "token.lonkingnearbackto2024.near", "MD_ID": "v2.ref-finance.near|4314|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "GEAR", "NBC_ID": "gear.enleap.near", "MD_ID": "v2.ref-finance.near|3411|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BLACKDRAGON", "NBC_ID": "blackdragon.tkn.near", "MD_ID": "v2.ref-finance.near|4276|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "SHITZU", "NBC_ID": "token.0xshitzu.near", "MD_ID": "v2.ref-finance.near|4369|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "JUMP", "NBC_ID": "jumptoken.jumpfinance.near", "MD_ID": "v2.ref-finance.near|4292|wrap.near", "DECIMAL": 18},
	    {"SYMBOL": "ZML", "NBC_ID": "ft.zomland.near", "MD_ID": "v2.ref-finance.near|4148|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "LOL", "NBC_ID": "memelol.near", "MD_ID": "v2.ref-finance.near|4389|wrap.near", "DECIMAL": 24},
	    {"SYMBOL": "NDC", "NBC_ID": "ndc.tkn.near", "MD_ID": "v2.ref-finance.near|4353|blackdragon.tkn.near", "DECIMAL": 18},
            {"SYMBOL": "PUMPOPOLY", "NBC_ID": "token.pumpopoly.near", "MD_ID": "v2.ref-finance.near|3066|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "LNR", "NBC_ID": "802d89b6e511b335f05024a65161bce7efc3f311.factory.bridge.near", "MD_ID": "linear-protocol-lnr", "DECIMAL": 18},
            {"SYMBOL": "FRAX", "NBC_ID": "853d955acef822db058eb8505911ed77f175b99e.factory.bridge.near", "MD_ID": "frax", "DECIMAL": 18},
            {"SYMBOL": "sFRAX", "NBC_ID": "a663b02cf0a4b149d2ad41910cb81e23e1c41c32.factory.bridge.near","MD_ID": "staked-frax", "DECIMAL": 18},
            {"SYMBOL": "BENDOG", "NBC_ID": "benthedog.near", "MD_ID": "v2.ref-finance.near|4530|wrap.near", "DECIMAL": 9},
            {"SYMBOL": "UWON", "NBC_ID": "438e48ed4ce6beecf503d43b9dbd3c30d516e7fd.factory.bridge.near", "MD_ID": "v2.ref-finance.near|4528|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "NEARVIDIA", "NBC_ID": "nearnvidia.near", "MD_ID": "v2.ref-finance.near|4547|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "BEAN", "NBC_ID": "bean.tkn.near", "MD_ID": "v2.ref-finance.near|4472|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "SOL", "NBC_ID": "22.contract.portalbridge.near", "MD_ID": "solana", "DECIMAL": 8},
            {"SYMBOL": "USM", "NBC_ID": "usmeme.tg", "MD_ID": "v2.ref-finance.near|4949|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "TOUCHED", "NBC_ID": "touched.tkn.near", "MD_ID": "v2.ref-finance.near|4771|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "KOK", "NBC_ID": "nkok.tkn.near", "MD_ID": "v2.ref-finance.near|4820|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "DGS", "NBC_ID": "dragonsoultoken.near", "MD_ID": "v2.ref-finance.near|4532|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "SLUSH", "NBC_ID": "slush.tkn.near", "MD_ID": "v2.ref-finance.near|4623|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "OTTO", "NBC_ID": "4e807467ba9e3119d5356c5568ef63e9c321b471.factory.bridge.near", "MD_ID": "v2.ref-finance.near|4479|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BABYBLACKDRAGON", "NBC_ID": "babyblackdragon.tkn.near", "MD_ID": "v2.ref-finance.near|4840|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "FAST", "NBC_ID": "edge-fast.near", "MD_ID": "v2.ref-finance.near|5167|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "HAT", "NBC_ID": "hat.tkn.near", "MD_ID": "v2.ref-finance.near|5179|wrap.near", "DECIMAL": 18},
            # {"SYMBOL": "INTEL", "NBC_ID": "intel.tkn.near", "MD_ID": "v2.ref-finance.near|4663|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "USDC", "NBC_ID": "16.contract.portalbridge.near", "MD_ID": "usd-coin", "DECIMAL": 6},
            {"SYMBOL": "DD", "NBC_ID": "dd.tg", "MD_ID": "v2.ref-finance.near|5222|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "NEIRO", "NBC_ID": "neiro.token0.near", "MD_ID": "v2.ref-finance.near|5255|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "CORGI", "NBC_ID": "corgi.token0.near", "MD_ID": "v2.ref-finance.near|5383|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "USDC", "NBC_ID": "17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 6},
            {"SYMBOL": "nUSDC", "NBC_ID": "a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 6},
            {"SYMBOL": "nUSDT", "NBC_ID": "dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 6},
            {"SYMBOL": "nDAI", "NBC_ID": "6b175474e89094c44da98b954eedeac495271d0f.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nWETH", "NBC_ID": "c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "n1INCH", "NBC_ID": "111111111117dc0aa78b770fa6a738034120c302.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nGRT", "NBC_ID": "c944e90c64b2c07662a292be6244bdf05cda44a7.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nHT", "NBC_ID": "6f259637dcd74c767781e37bc6133cd6a68aa161.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nGTC", "NBC_ID": "de30da39c46104798bb5aa3fe8b9e0e1f348163f.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nUNI", "NBC_ID": "1f9840a85d5af5bf1d1762f925bdaddc4201f984.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "nWBTC", "NBC_ID": "2260fac5e5542a773aa44fbcfedf7c193bc2c599.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "nLINK", "NBC_ID": "514910771af9ca656af840dff83e8264ecf986ca.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "ETH", "NBC_ID": "aurora", "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "CELO", "NBC_ID": "celo.token.a11bd.near", "MD_ID": "v2.ref-finance.near|NA|wrap.near",
             "DECIMAL": 24},
            {"SYMBOL": "cUSD", "NBC_ID": "cusd.token.a11bd.near",
             "MD_ID": "v2.ref-finance.near|NA|a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near",
             "DECIMAL": 24},
            {"SYMBOL": "ABR", "NBC_ID": "abr.a11bd.near",
             "MD_ID": "v2.ref-finance.near|NA|a0b86991c6218b36c1d19d4a2e9eb0ce3606eb48.factory.bridge.near",
             "DECIMAL": 24},
            {"SYMBOL": "SOL", "NBC_ID": "sol.token.a11bd.near", "MD_ID": "v2.ref-finance.near|NA|wrap.near",
             "DECIMAL": 24},
            {"SYMBOL": "WOO", "NBC_ID": "4691937a7508860f876c9c0a2a617e7d9e945d4b.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "HBTC", "NBC_ID": "0316eb71485b0ab14103307bf65a021042c6d380.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|2260fac5e5542a773aa44fbcfedf7c193bc2c599.factory.bridge.near",
             "DECIMAL": 18},
            {"SYMBOL": "SD", "NBC_ID": "30d20208d987713f46dfd34ef128bb16c404d10f.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "OIN", "NBC_ID": "9aeb50f542050172359a0e1a25a9933bc8c01259.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|dac17f958d2ee523a2206206994597c13d831ec7.factory.bridge.near",
             "DECIMAL": 8},
            {"SYMBOL": "LUNA", "NBC_ID": "luna.token.a11bd.near", "MD_ID": "v2.ref-finance.near|NA|wrap.near",
             "DECIMAL": 24},
            {"SYMBOL": "BSTN", "NBC_ID": "059a1f1dea1020297588c316ffc30a58a1a0d4a2.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "TAO", "NBC_ID": "fusotao-token.near", "MD_ID": "v2.ref-finance.near|NA|wrap.near",
             "DECIMAL": 18},
            {"SYMBOL": "USDt", "NBC_ID": "usdt.tether-token.near", "MD_ID": "v2.ref-finance.near|NA|wrap.near",
             "DECIMAL": 6},
            {"SYMBOL": "LNR", "NBC_ID": "802d89b6e511b335f05024a65161bce7efc3f311.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "FRAX", "NBC_ID": "853d955acef822db058eb8505911ed77f175b99e.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "sFRAX", "NBC_ID": "a663b02cf0a4b149d2ad41910cb81e23e1c41c32.factory.bridge.near",
             "MD_ID": "v2.ref-finance.near|NA|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "SOL", "NBC_ID": "22.contract.portalbridge.near", "MD_ID": "v2.ref-finance.near|NA|wrap.near",
             "DECIMAL": 8},
            {"SYMBOL": "USDC", "NBC_ID": "16.contract.portalbridge.near",
             "MD_ID": "v2.ref-finance.near|NA|17208628f84f5d6ad33f0da3bbbeb27ffcb398eac501a31bd6ad2011e36133a1",
             "DECIMAL": 6},
            {"SYMBOL": "KAT", "NBC_ID": "kat.token0.near", "MD_ID": "v2.ref-finance.near|5391|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "GP", "NBC_ID": "gp.token0.near", "MD_ID": "v2.ref-finance.near|5422|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "CHILL", "NBC_ID": "chill-129.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5462|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "zNEARnM-USDC", "NBC_ID": "v1.guild-covenant.near", "MD_ID": "v2.ref-finance.near|5442|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "4illia", "NBC_ID": "4illia-222.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5494|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "gnear", "NBC_ID": "gnear-229.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5502|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "mpDAO", "NBC_ID": "mpdao-token.near", "MD_ID": "v2.ref-finance.near|5438|meta-pool.near", "DECIMAL": 6},
            {"SYMBOL": "gnuff", "NBC_ID": "gnuff-283.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5539|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "PUMPKG", "NBC_ID": "pumpkg-332.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5576|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BCC", "NBC_ID": "bcc-242.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5508|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "LUCKY", "NBC_ID": "lucky-273.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5527|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "SIN", "NBC_ID": "sin-339.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5583|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "USDC", "NBC_ID": "3.contract.portalbridge.near", "MD_ID": "usd-coin", "DECIMAL": 6},
            {"SYMBOL": "CHICA", "NBC_ID": "token.bocachica_mars.near", "MD_ID": "v2.ref-finance.near|3886|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BST", "NBC_ID": "509a38b7a1cc0dcd83aa9d06214663d9ec7c7f4a.factory.bridge.near", "MD_ID": "v2.ref-finance.near|3840|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "CZ", "NBC_ID": "cz.token0.near", "MD_ID": "v2.ref-finance.near|5283|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "Darai", "NBC_ID": "darai.tkn.near", "MD_ID": "v2.ref-finance.near|5123|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "Hijack", "NBC_ID": "hijack-252.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5519|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "BULLA", "NBC_ID": "bulla.tkn.near", "MD_ID": "v2.ref-finance.near|5517|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "6bowen", "NBC_ID": "6bowen-227.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5496|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "PURGE", "NBC_ID": "purge-558.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5650|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "ABG", "NBC_ID": "abg-966.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5720|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "DUCT", "NBC_ID": "duct-1078.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5741|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "Bullish", "NBC_ID": "bullish-1254.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5787|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "TruNEAR", "NBC_ID": "staker1.msig1.trufin.near", "MD_ID": "v2.ref-finance.near|5563|wrap.near", "DECIMAL": 24},
            {"SYMBOL": "NOEAR", "NBC_ID": "noear-324.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5574|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "RIN", "NBC_ID": "rin.tkn.near", "MD_ID": "v2.ref-finance.near|5814|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "GOTI", "NBC_ID": "goti.token0.near", "MD_ID": "v2.ref-finance.near|5853|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "MACHO", "NBC_ID": "macho.token0.near", "MD_ID": "v2.ref-finance.near|5857|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "ILPEPE", "NBC_ID": "ilpepe.token0.near", "MD_ID": "v2.ref-finance.near|5836|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "ASI", "NBC_ID": "token.sendertge.near", "MD_ID": "v2.ref-finance.near|5876|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "JLU", "NBC_ID": "jlu-1018.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5728|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "DOM", "NBC_ID": "dom-1568.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5941|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "SPEAR", "NBC_ID": "spear-1565.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5936|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "PLB", "NBC_ID": "plb-1567.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5940|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "NBTC", "NBC_ID": "nbtc.bridge.near", "MD_ID": "v2.ref-finance.near|5949|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "IMG_8327", "NBC_ID": "img_8327-1591.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5982|wrap.near", "DECIMAL": 18},
            {"SYMBOL": "aBTC", "NBC_ID": "31761a152f1e96f966c041291644129144233b0b.factory.bridge.near", "MD_ID": "v2.ref-finance.near|5991|nbtc.bridge.near", "DECIMAL": 18},
            {"SYMBOL": "DONOR", "NBC_ID": "donor-1517.meme-cooking.near", "MD_ID": "v2.ref-finance.near|5903|wrap.near", "DECIMAL": 2},
            {"SYMBOL": "ZEC", "NBC_ID": "zec.omft.near", "MD_ID": "v2.ref-finance.near|6065|wrap.near", "DECIMAL": 8},
            {"SYMBOL": "ETH", "NBC_ID": "eth.bridge.near", "MD_ID": "v2.ref-finance.near|6354|wrap.near", "DECIMAL": 18},
        ],
        "BASE_MAINNET": [
        ],
    }
    MARKET_URL = MARKET_URL
    MARKET_KEY = MARKET_KEY
    REF_URL = REF_URL
    REF_SDK_URL = REF_SDK_URL


if __name__ == '__main__':
    print(type(Cfg))
    print(type(Cfg.TOKENS))
    print(type(Cfg.NETWORK_ID), Cfg.NETWORK_ID)
    print(Cfg.NETWORK["TESTNET"]["NEAR_RPC_URL"])
