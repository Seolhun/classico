from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# # # # # # # # # # # # # # # #
# Setting Db using orm
db_engine = create_engine('mysql://hooney:blue1220@@127.0.0.1/classico', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))


# board = Board('게시판 제목1', '게시판 내용1', 'shooney')
# board2 = Board('게시판 제목2', '게시판 내용2', 'shooney')
# db_session.add(board)
# db_session.add(board2)
# db_session.commit()
#
# Board.query.all()
# Board.query.filter_by(title='게시판 제목1').first()