import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, BigInteger
from setting import Base
from setting import ENGINE

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))

class save_data_list(Base):
    __tablename__ = 'save_data_list'
    id = Column('id', Integer, primary_key = True)
    exchange_name = Column('exchange_name', String(200))
    symbol_name = Column('symbol_name', String(300))
    table_name = Column('table_name', String(300))

class tickdata_ftx_btc(Base):
    __tablename__ = 'tickdata_ftx_btc'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_bch_perp(Base):
    __tablename__ = 'tickdata_ftx_bch_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_ada_perp(Base):
    __tablename__ = 'tickdata_ftx_ada_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_bat_perp(Base):
    __tablename__ = 'tickdata_ftx_bat_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))


class tickdata_ftx_bnb_perp(Base):
    __tablename__ = 'tickdata_ftx_bnb_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))


class tickdata_ftx_bsv_perp(Base):
    __tablename__ = 'tickdata_ftx_bsv_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))


class tickdata_ftx_dash_perp(Base):
    __tablename__ = 'tickdata_ftx_dash_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))


class tickdata_ftx_defi_perp(Base):
    __tablename__ = 'tickdata_ftx_defi_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_doge_perp(Base):
    __tablename__ = 'tickdata_ftx_doge_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_dot_perp(Base):
    __tablename__ = 'tickdata_ftx_dot_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_eos_perp(Base):
    __tablename__ = 'tickdata_ftx_eos_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_etc_perp(Base):
    __tablename__ = 'tickdata_ftx_etc_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_ftt_perp(Base):
    __tablename__ = 'tickdata_ftx_ftt_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_iota_perp(Base):
    __tablename__ = 'tickdata_ftx_iota_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_link_perp(Base):
    __tablename__ = 'tickdata_ftx_link_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_ltc_perp(Base):
    __tablename__ = 'tickdata_ftx_ltc_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_neo_perp(Base):
    __tablename__ = 'tickdata_ftx_neo_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_omg_perp(Base):
    __tablename__ = 'tickdata_ftx_omg_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_qtum_perp(Base):
    __tablename__ = 'tickdata_ftx_qtum_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_shib_perp(Base):
    __tablename__ = 'tickdata_ftx_shib_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_sol_perp(Base):
    __tablename__ = 'tickdata_ftx_sol_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_uni_perp(Base):
    __tablename__ = 'tickdata_ftx_uni_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_usdt_perp(Base):
    __tablename__ = 'tickdata_ftx_usdt_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_xem_perp(Base):
    __tablename__ = 'tickdata_ftx_xem_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_xrp_perp(Base):
    __tablename__ = 'tickdata_ftx_xrp_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))

class tickdata_ftx_xlm_perp(Base):
    __tablename__ = 'tickdata_ftx_xlm_perp'
    id = Column('id', Integer, primary_key = True)
    timestamp = Column('timestamp', BigInteger)
    price= Column('price', Float)
    amount = Column('amount', Float)
    direction= Column('direction', String(100))





def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)
