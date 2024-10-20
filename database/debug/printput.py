from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.schema import (
    Book, Song, Lyricist, SongWriter, Arranger, Artist,
    SongLyricistAssociation, SongWriterAssociation, 
    SongArrangerAssociation, SongArtistAssociation
)

# エンジンを作成
engine = create_engine('sqlite:///ompooscores.db', echo=True)

# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()

# 出力用のファイルを開く
with open("output.txt", "w", encoding="utf-8") as f:
    try:
        # Bookテーブルのデータを取得
        books = session.query(Book).all()
        f.write("Books:\n")
        for book in books:
            f.write(f"ID: {book.id}, Name: {book.book_name}, Product Code: {book.product_code}\n")
        
        # Songテーブルのデータを取得
        songs = session.query(Song).all()
        f.write("\nSongs:\n")
        for song in songs:
            f.write(f"ID: {song.id}, Name: {song.song_name}, Book ID: {song.book_id}, Memo: {song.memo}, Grade: {song.grade}\n")
        
        # Artistテーブルのデータを取得
        artists = session.query(Artist).all()
        f.write("\nArtists:\n")
        for artist in artists:
            f.write(f"ID: {artist.id}, Name: {artist.Artist_name}\n")
        
        # Lyricistテーブルのデータを取得
        lyricists = session.query(Lyricist).all()
        f.write("\nLyricists:\n")
        for lyricist in lyricists:
            f.write(f"ID: {lyricist.id}, Name: {lyricist.lyricist_name}\n")
        
        # SongWriterテーブルのデータを取得
        song_writers = session.query(SongWriter).all()
        f.write("\nSong Writers:\n")
        for writer in song_writers:
            f.write(f"ID: {writer.id}, Name: {writer.song_writer_name}\n")
        
        # Arrangerテーブルのデータを取得
        arrangers = session.query(Arranger).all()
        f.write("\nArrangers:\n")
        for arranger in arrangers:
            f.write(f"ID: {arranger.id}, Name: {arranger.arranger_name}\n")

        print("データの書き込みが完了しました。")
    
    except Exception as e:
        print(f"Error occurred: {e}")
        f.write(f"\nError occurred: {e}\n")

    finally:
        # セッションをクローズしてリソースを解放
        session.close()
