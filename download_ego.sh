#!/bin/bash
DIRECTORY="ego_data"
GAMES="cards
chess
jenga
puzzle"

wget http://vision.soic.indiana.edu/egohands_files/egohands_all_frames.zip

if [ ! -d "$DIRECTORY" ]; then
     mkdir "$DIRECTORY"
     unzip egohands_all_frames.zip -d ./"$DIRECTORY"
fi

rm egohands_all_frames.zip

cd ./$DIRECTORY

for game in $GAMES
do
    #mkdir "$game"
    #mv "$game"_* ./$game
    cd ./$game
    for f in "$game"_*/;
    do 
        mv -v "$f" "${f/"$game"_/}";
    done;
    cd ..
done