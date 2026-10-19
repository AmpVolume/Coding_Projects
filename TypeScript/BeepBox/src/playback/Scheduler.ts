import { Song } from "../model/Song";
import { AudioEngine } from "../audio/AudioEngine";
import { PlaybackCursor } from "./PlaybackCursor";



export class Scheduler {



    song:Song;


    audio:AudioEngine;


    cursor:PlaybackCursor;



    lookAhead:number;



    constructor(
        song:Song,
        audio:AudioEngine,
        cursor:PlaybackCursor
    ){

        this.song=song;

        this.audio=audio;

        this.cursor=cursor;


        this.lookAhead=0.1;

    }





    update(){


        const currentBeat =
        this.cursor.beat;



        for(
            const channel of this.song.channels
        ){


            for(
                const pattern of channel.patterns
            ){


                for(
                    const note of pattern.notes
                ){


                    if(
                        note.start >= currentBeat &&
                        note.start <
                        currentBeat + this.lookAhead
                    ){



                        this.audio.playNote(
                            note.pitch,
                            note.duration
                        );


                    }


                }


            }


        }



    }


}